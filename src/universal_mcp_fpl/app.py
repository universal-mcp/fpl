from universal_mcp.applications import APIApplication
from universal_mcp.integrations import Integration
from typing import Any
from universal_mcp_fpl.helper import get_player_info, search_players, get_players_resource, find_players_by_name
import datetime
from universal_mcp_fpl.api import api
from universal_mcp_fpl.position_utils import normalize_position
from collections import Counter

from universal_mcp_fpl.fixtures import get_player_gameweek_history, get_blank_gameweeks, get_double_gameweeks, analyze_player_fixtures



class FplApp(APIApplication):
    """
    Base class for Universal MCP Applications.
    """
    def __init__(self, integration: Integration | None = None, **kwargs) -> None:
        super().__init__(name="fpl", integration=integration, **kwargs)

    
    
    def get_player_information(self,
        player_id: int | None = None,
        player_name: str | None = None,
        start_gameweek: int | None = None,
        end_gameweek: int | None = None,
        include_history: bool = True,
        include_fixtures: bool = True
    ) -> dict[str, Any]:
        """Get detailed information and statistics for a specific player

        Args:
            player_id: FPL player ID (if provided, takes precedence over player_name)
            player_name: Player name to search for (used if player_id not provided)
            start_gameweek: Starting gameweek for filtering player history
            end_gameweek: Ending gameweek for filtering player history
            include_history: Whether to include gameweek-by-gameweek history
            include_fixtures: Whether to include upcoming fixtures

        Returns:
            Comprehensive player information including stats and history

        Raises:
            ValueError: Raised when both player_id and player_name are missing.
            KeyError: Raised when player is not found in the database.

        Tags:
            players, important
        """
        return get_player_info(
            player_id,
            player_name,
            start_gameweek,
            end_gameweek,
            include_history,
            include_fixtures
        )

    def search_fpl_players(self,
        query: str,
        position: str | None = None,
        team: str | None = None,
        limit: int = 5
    ) -> dict[str, Any]:
        """Search for FPL players by name with optional filtering

        Args:
            query: Player name or partial name to search for
            position: Optional position filter (GKP, DEF, MID, FWD)
            team: Optional team name filter
            limit: Maximum number of results to return

        Returns:
            List of matching players with details

        Raises:
            ValueError: Raised when query parameter is empty or invalid.
            TypeError: Raised when position or team filters are invalid.

        Tags:
            players, search, important
        """
        return search_players(query, position, team, limit)
    
    def get_gameweek_status(self) -> dict[str, Any]:
        """
        Get precise information about current, previous, and next gameweeks.

        Returns:
            Detailed information about gameweek timing, including exact status.

        Raises:
            RuntimeError: If gameweek data cannot be retrieved.
            ValueError: If gameweek data is malformed or incomplete.

        Tags:
            gameweek, status, timing, important
        """
       
        

        gameweeks = api.get_gameweeks()

        # Find current, previous, and next gameweeks
        current_gw = next((gw for gw in gameweeks if gw.get("is_current")), None)
        previous_gw = next((gw for gw in gameweeks if gw.get("is_previous")), None)
        next_gw = next((gw for gw in gameweeks if gw.get("is_next")), None)

        # Determine exact current gameweek status
        current_status = "Not Started"
        if current_gw:
            deadline = datetime.datetime.strptime(current_gw["deadline_time"], "%Y-%m-%dT%H:%M:%SZ")
            now = datetime.datetime.utcnow()

            if now < deadline:
                current_status = "Upcoming"
                time_until = deadline - now
                hours_until = time_until.total_seconds() / 3600

                if hours_until < 24:
                    current_status = "Imminent (< 24h)"
            else:
                if current_gw.get("finished"):
                    current_status = "Complete"
                else:
                    current_status = "In Progress"

        return {
            "current_gameweek": current_gw and current_gw["id"],
            "current_status": current_status,
            "previous_gameweek": previous_gw and previous_gw["id"],
            "next_gameweek": next_gw and next_gw["id"],
            "season_progress": f"GW {current_gw['id']}/38" if current_gw else "Unknown",
            "exact_timing": {
                "current_deadline": current_gw and current_gw.get("deadline_time"),
                "next_deadline": next_gw and next_gw.get("deadline_time")
            }
        }
    
    def analyze_players(self,
        position: str | None = None,
        team: str | None = None,
        min_price: float | None = None,
        max_price: float | None = None,
        min_points: int | None = None,
        min_ownership: float | None = None,
        max_ownership: float | None = None,
        form_threshold: float | None = None,
        include_gameweeks: bool = False,
        num_gameweeks: int = 5,
        sort_by: str = "total_points",
        sort_order: str = "desc",
        limit: int = 20 
    ) -> dict[str, Any]:
        """Filter and analyze FPL players based on multiple criteria
    
        Args:
            position: Player position (e.g., "midfielders", "defenders")
            team: Team name filter
            min_price: Minimum player price in millions
            max_price: Maximum player price in millions
            min_points: Minimum total points
            min_ownership: Minimum ownership percentage
            max_ownership: Maximum ownership percentage
            form_threshold: Minimum form rating
            include_gameweeks: Whether to include gameweek-by-gameweek data
            num_gameweeks: Number of recent gameweeks to include
            sort_by: Metric to sort results by (default: total_points)
            sort_order: Sort direction ("asc" or "desc")
            limit: Maximum number of players to return
        
        Returns:
            Filtered player data with summary statistics

        Raises:
            ValueError: Raised when query parameter is empty or invalid.
            TypeError: Raised when position or team filters are invalid.

        Tags:
            players, analyze, important    
        """
        # Get cached complete player dataset
        all_players = get_players_resource()
        
        # Normalize position if provided
        normalized_position = normalize_position(position) if position else None
        position_changed = normalized_position != position if position else False
        
        # Apply all filters
        filtered_players = []
        for player in all_players:
            # Check position filter
            if normalized_position and player.get("position") != normalized_position:
                continue
                
            # Check team filter
            if team and not (
                team.lower() in player.get("team", "").lower() or 
                team.lower() in player.get("team_short", "").lower()
            ):
                continue
                
            # Check price range
            if min_price is not None and player.get("price", 0) < min_price:
                continue
            if max_price is not None and player.get("price", 0) > max_price:
                continue
                
            # Check points threshold
            if min_points is not None and player.get("points", 0) < min_points:
                continue
                
            # Check ownership range
            try:
                ownership = float(player.get("selected_by_percent", 0).replace("%", ""))
                if min_ownership is not None and ownership < min_ownership:
                    continue
                if max_ownership is not None and ownership > max_ownership:
                    continue
            except (ValueError, TypeError):
                # Skip ownership check if value can't be converted
                pass
                
            # Check form threshold
            try:
                form = float(player.get("form", 0))
                if form_threshold is not None and form < form_threshold:
                    continue
            except (ValueError, TypeError):
                # Skip form check if value can't be converted
                pass

            player['status'] = "available" if player.get("status") == "a" else "unavailable"
                
            # Player passed all filters
            filtered_players.append(player)
        
        # Sort results
        reverse = sort_order.lower() != "asc"
        try:
            # Handle numeric sorting properly
            numeric_fields = ["points", "price", "form", "selected_by_percent", "value"]
            if sort_by in numeric_fields:
                filtered_players.sort(
                    key=lambda p: float(p.get(sort_by, 0)) 
                    if p.get(sort_by) is not None else 0,
                    reverse=reverse
                )
            else:
                filtered_players.sort(
                    key=lambda p: p.get(sort_by, ""), 
                    reverse=reverse
                )
        except (KeyError, ValueError):
            # Fall back to points sorting
            filtered_players.sort(
                key=lambda p: float(p.get("points", 0)), 
                reverse=True
            )
        
        # Calculate summary statistics
        total_players = len(filtered_players)
        average_points = sum(float(p.get("points", 0)) for p in filtered_players) / max(1, total_players)
        average_price = sum(float(p.get("price", 0)) for p in filtered_players) / max(1, total_players)
        
        # Count position and team distributions
        position_counts = Counter(p.get("position") for p in filtered_players)
        team_counts = Counter(p.get("team") for p in filtered_players)
        
        # Build filter description
        applied_filters = []
        if normalized_position:
            applied_filters.append(f"Position: {normalized_position}")
        if team:
            applied_filters.append(f"Team: {team}")
        if min_price is not None:
            applied_filters.append(f"Min price: £{min_price}m")
        if max_price is not None:
            applied_filters.append(f"Max price: £{max_price}m")
        if min_points is not None:
            applied_filters.append(f"Min points: {min_points}")
        if min_ownership is not None:
            applied_filters.append(f"Min ownership: {min_ownership}%")
        if max_ownership is not None:
            applied_filters.append(f"Max ownership: {max_ownership}%")
        if form_threshold is not None:
            applied_filters.append(f"Min form: {form_threshold}")
        
        # Build results with summary and detail sections
        result = {
            "summary": {
                "total_matches": total_players,
                "filters_applied": applied_filters,
                "average_points": round(average_points, 1),
                "average_price": round(average_price, 2),
                "position_distribution": dict(position_counts),
                "team_distribution": dict(sorted(
                    team_counts.items(), 
                    key=lambda x: x[1], 
                    reverse=True
                )[:10]),  # Top 10 teams
            },
            "players": filtered_players[:limit]  # Apply limit to detailed results
        }
        
        # Add position normalization note if relevant
        if position_changed:
            result["summary"]["position_note"] = f"'{position}' was interpreted as '{normalized_position}'"
        
        # Include gameweek history if requested
        if include_gameweeks and filtered_players:
            try:
                # Get history for top players (limit)
                player_ids = [p.get("id") for p in filtered_players[:limit]]
                gameweek_data = get_player_gameweek_history(player_ids, num_gameweeks)
                
                # Add gameweek data to the result
                result["gameweek_data"] = gameweek_data
                
                # Calculate and add recent form stats based on gameweek history
                recent_form_stats = {}
                
                if "players" in gameweek_data:
                    for player_id, history in gameweek_data["players"].items():
                        player_id = int(player_id)
                        
                        # Find matching player in our filtered list
                        player_info = next((p for p in filtered_players if p.get("id") == player_id), None)
                        if not player_info:
                            continue
                        
                        # Initialize stats
                        recent_stats = {
                            "player_name": player_info.get("name", "Unknown"),
                            "matches": len(history),
                            "minutes": 0,
                            "points": 0,
                            "goals": 0,
                            "assists": 0,
                            "clean_sheets": 0,
                            "bonus": 0,
                            "expected_goals": 0,
                            "expected_assists": 0,
                            "expected_goal_involvements": 0,
                            "points_per_game": 0,
                            "gameweeks_analyzed": gameweek_data.get("gameweeks", [])
                        }
                        
                        # Sum up stats from gameweek history
                        for gw in history:
                            recent_stats["minutes"] += gw.get("minutes", 0)
                            recent_stats["points"] += gw.get("points", 0)
                            recent_stats["goals"] += gw.get("goals", 0)
                            recent_stats["assists"] += gw.get("assists", 0)
                            recent_stats["clean_sheets"] += gw.get("clean_sheets", 0)
                            recent_stats["bonus"] += gw.get("bonus", 0)
                            recent_stats["expected_goals"] += float(gw.get("expected_goals", 0))
                            recent_stats["expected_assists"] += float(gw.get("expected_assists", 0))
                            recent_stats["expected_goal_involvements"] += float(gw.get("expected_goal_involvements", 0))
                        
                        # Calculate averages
                        if recent_stats["matches"] > 0:
                            recent_stats["points_per_game"] = round(recent_stats["points"] / recent_stats["matches"], 1)
                            
                        # Round floating point values
                        recent_stats["expected_goals"] = round(recent_stats["expected_goals"], 2)
                        recent_stats["expected_assists"] = round(recent_stats["expected_assists"], 2)
                        recent_stats["expected_goal_involvements"] = round(recent_stats["expected_goal_involvements"], 2)
                        
                        recent_form_stats[str(player_id)] = recent_stats
                
                # Add recent form stats to result
                result["recent_form"] = {
                    "description": f"Stats for the last {num_gameweeks} gameweeks only",
                    "player_stats": recent_form_stats
                }
                
                # Add labels to clarify which stats are season-long vs. recent
                for player in result["players"]:
                    player["stats_type"] = "season_totals"
                    
            except Exception as e:
                
                result["gameweek_data_error"] = str(e)
        
        return result
        

    def compare_players(self,
        player_names: list[str],
        metrics: list[str] = ["total_points", "form", "goals_scored", "assists", "bonus"],
        include_gameweeks: bool = False,
        num_gameweeks: int = 5,
        include_fixture_analysis: bool = True
    ) -> dict[str, Any]:
        """Compare multiple players across various metrics
        
        Args:
            player_names: List of player names to compare (2-5 players recommended)
            metrics: List of metrics to compare
            include_gameweeks: Whether to include gameweek-by-gameweek comparison
            num_gameweeks: Number of recent gameweeks to include in comparison
            include_fixture_analysis: Whether to include fixture analysis including blanks and doubles
            
        Returns:
            Detailed comparison of players across the specified metrics

        Raises:
            ValueError: Raised when player_names parameter is empty or invalid.
            TypeError: Raised when metrics parameter is invalid.

        Tags:
            players, compare, important
        """

        if not player_names or len(player_names) < 2:
            return {"error": "Please provide at least two player names to compare"}
        
        # Find all players by name
        players_data = {}
        for name in player_names:
            matches = find_players_by_name(name, limit=3)  # Get more matches to find active players
            if not matches:
                return {"error": f"No player found matching '{name}'"}
                
            # Filter to active players
            active_matches = [p for p in matches]
                
            # Use first active match
            player = active_matches[0]
            players_data[name] = player
        
        # Build comparison structure
        comparison = {
            "players": {
                name: {
                    "id": player["id"],
                    "name": player["name"],
                    "team": player["team"],
                    "position": player["position"],
                    "price": player["price"],
                    "status": "available" if player["status"] == "a" else "unavailable",
                    "news": player.get("news", ""),
                } for name, player in players_data.items()
            },
            "metrics_comparison": {}
        }
        
        # Compare all requested metrics
        for metric in metrics:
            metric_values = {}
            
            for name, player in players_data.items():
                if metric in player:
                    # Try to convert to numeric if possible
                    try:
                        value = float(player[metric])
                    except (ValueError, TypeError):
                        value = player[metric]
                        
                    metric_values[name] = value
            
            if metric_values:
                comparison["metrics_comparison"][metric] = metric_values
        
        # Include gameweek comparison if requested
        if include_gameweeks:
            try:
                gameweek_comparison = {}
                recent_form_comparison = {}
                gameweek_range = []
                
                # Get gameweek data for each player
                for name, player in players_data.items():
                    player_history = get_player_gameweek_history([player["id"]], num_gameweeks)
                    
                    if "players" in player_history and player["id"] in player_history["players"]:
                        history = player_history["players"][player["id"]]
                        gameweek_comparison[name] = history
                        
                        # Store gameweek range
                        if "gameweeks" in player_history and not gameweek_range:
                            gameweek_range = player_history["gameweeks"]
                        
                        # Calculate aggregated recent form stats
                        recent_stats = {
                            "matches": len(history),
                            "minutes": 0,
                            "points": 0,
                            "goals": 0,
                            "assists": 0,
                            "clean_sheets": 0,
                            "bonus": 0,
                            "expected_goals": 0,
                            "expected_assists": 0,
                            "expected_goal_involvements": 0,
                            "points_per_game": 0
                        }
                        
                        # Sum up stats from gameweek history
                        for gw in history:
                            recent_stats["minutes"] += gw.get("minutes", 0)
                            recent_stats["points"] += gw.get("points", 0)
                            recent_stats["goals"] += gw.get("goals", 0)
                            recent_stats["assists"] += gw.get("assists", 0)
                            recent_stats["clean_sheets"] += gw.get("clean_sheets", 0)
                            recent_stats["bonus"] += gw.get("bonus", 0)
                            recent_stats["expected_goals"] += int(float(gw.get("expected_goals", 0)))
                            recent_stats["expected_assists"] += int(float(gw.get("expected_assists", 0)))
                            recent_stats["expected_goal_involvements"] += int(float(gw.get("expected_goal_involvements", 0)))
                        if recent_stats["matches"] > 0:
                            recent_stats["points_per_game"] = int(round(recent_stats["points"] / recent_stats["matches"], 1))
                        
                        # Round floating point values
                        recent_stats["expected_goals"] = round(recent_stats["expected_goals"], 2)
                        recent_stats["expected_assists"] = round(recent_stats["expected_assists"], 2)
                        recent_stats["expected_goal_involvements"] = round(recent_stats["expected_goal_involvements"], 2)
                        
                        recent_form_comparison[name] = recent_stats
                
                # Only add to result if we have data
                if gameweek_comparison:
                    comparison["gameweek_comparison"] = gameweek_comparison
                    comparison["gameweek_range"] = gameweek_range
                    
                    # Add recent form comparison section
                    comparison["recent_form_comparison"] = {
                        "description": f"Aggregated stats for the last {num_gameweeks} gameweeks only",
                        "gameweeks_analyzed": gameweek_range,
                        "player_stats": recent_form_comparison
                    }
                    
                    # Add best performer for recent form metrics
                    comparison["recent_form_best"] = {}
                    
                    # Compare players on key recent form metrics
                    for metric in ["points", "goals", "assists", "expected_goals", "expected_assists"]:
                        values = {name: stats[metric] for name, stats in recent_form_comparison.items()}
                        if values and all(isinstance(v, (int, float)) for v in values.values()):
                            best_player = max(values.items(), key=lambda x: x[1])[0]
                            comparison["recent_form_best"][metric] = best_player
                    
                    # Add label to metrics to indicate they're season-long stats
                    for metric, values in comparison["metrics_comparison"].items():
                        comparison["metrics_comparison"][metric] = {
                            "stats_type": "season_totals",
                            "values": values
                        }
            except Exception as e:
                comparison["gameweek_comparison_error"] = str(e)
        
        # Include fixture analysis if requested
        if include_fixture_analysis:
            fixture_comparison = {}
            fixture_scores = {}
            blank_gameweek_impacts = {}
            double_gameweek_impacts = {}
            
            # Get upcoming fixtures for each player
            for name, player in players_data.items():
                try:
                    # Get fixture analysis
                    player_fixture_analysis = analyze_player_fixtures(player["id"], num_gameweeks)
                    
                    # Format fixture data
                    fixtures_data = []
                    if "fixture_analysis" in player_fixture_analysis and "fixtures_analyzed" in player_fixture_analysis["fixture_analysis"]:
                        fixtures_data = player_fixture_analysis["fixture_analysis"]["fixtures_analyzed"]
                    
                    fixture_comparison[name] = fixtures_data
                    
                    # Store fixture difficulty score
                    if "fixture_analysis" in player_fixture_analysis and "difficulty_score" in player_fixture_analysis["fixture_analysis"]:
                        fixture_scores[name] = player_fixture_analysis["fixture_analysis"]["difficulty_score"]
                    
                    # Check for blank gameweeks
                    team_name = player["team"]
                    blank_gws = get_blank_gameweeks(num_gameweeks)
                    blank_impact = []
                    
                    for blank_gw in blank_gws:
                        for team_info in blank_gw.get("teams_without_fixtures", []):
                            if team_info.get("name") == team_name:
                                blank_impact.append(blank_gw["gameweek"])
                    
                    blank_gameweek_impacts[name] = blank_impact
                    
                    # Check for double gameweeks
                    double_gws = get_double_gameweeks(num_gameweeks)
                    double_impact = []
                    
                    for double_gw in double_gws:
                        for team_info in double_gw.get("teams_with_doubles", []):
                            if team_info.get("name") == team_name:
                                double_impact.append({
                                    "gameweek": double_gw["gameweek"],
                                    "fixture_count": team_info.get("fixture_count", 2)
                                })
                    
                    double_gameweek_impacts[name] = double_impact
                except Exception as e:
                    print(f"Error getting fixture analysis for {name}: {e}")
                
            
            # Add fixture data to comparison
            if fixture_comparison:
                comparison["fixture_comparison"] = {
                    "upcoming_fixtures": fixture_comparison,
                    "fixture_scores": fixture_scores,
                    "blank_gameweeks": blank_gameweek_impacts,
                    "double_gameweeks": double_gameweek_impacts
                }
                
                # Add fixture advantage assessment
                if len(fixture_scores) >= 2:
                    best_fixtures_player = max(fixture_scores.items(), key=lambda x: x[1])[0]
                    worst_fixtures_player = min(fixture_scores.items(), key=lambda x: x[1])[0]
                    
                    comparison["fixture_comparison"]["fixture_advantage"] = {
                        "best_fixtures": best_fixtures_player,
                        "worst_fixtures": worst_fixtures_player,
                        "advantage": f"{best_fixtures_player} has easier upcoming fixtures than {worst_fixtures_player}"
                    }
        
        # Add summary of who's best for each metric
        comparison["best_performers"] = {}
        
        for metric, values in comparison["metrics_comparison"].items():
            # Determine which metrics should be ranked with higher values as better
            higher_is_better = metric not in ["price"]
            
            # Find the best player for this metric
            if all(isinstance(v, (int, float)) for v in values.values()):
                if higher_is_better:
                    best_name = max(values.items(), key=lambda x: x[1])[0]
                else:
                    best_name = min(values.items(), key=lambda x: x[1])[0]
                    
                comparison["best_performers"][metric] = best_name
        
        # Overall comparison summary
        player_wins = {name: 0 for name in players_data.keys()}
        
        for metric, best_name in comparison["best_performers"].items():
            player_wins[best_name] = player_wins.get(best_name, 0) + 1
        
        # Add fixture advantage to wins if available
        if include_fixture_analysis and "fixture_comparison" in comparison and "fixture_advantage" in comparison["fixture_comparison"]:
            best_fixtures_player = comparison["fixture_comparison"]["fixture_advantage"]["best_fixtures"]
            player_wins[best_fixtures_player] = player_wins.get(best_fixtures_player, 0) + 1
        
        comparison["summary"] = {
            "metrics_won": player_wins,
            "overall_best": max(player_wins.items(), key=lambda x: x[1])[0] if player_wins else None
        }
        
        return comparison


    def list_tools(self):
        """
        Lists the available tools (methods) for this application.
        """
        return [self.get_player_information,
                self.search_fpl_players,
                self.get_gameweek_status,
                self.analyze_players,
                self.compare_players
                ]

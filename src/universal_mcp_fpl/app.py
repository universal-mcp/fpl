from universal_mcp.applications import APIApplication
from universal_mcp.integrations import Integration
from typing import Any
from universal_mcp_fpl.helper import get_player_info, search_players

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
        import datetime
        from typing import Any

        # Use the helper's api instance if available, else import here
        try:
            from . import helper
            api = helper.api
        except ImportError:
            raise RuntimeError("Could not import FPL API helper.")

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
    
    def list_tools(self):
        """
        Lists the available tools (methods) for this application.
        """
        return [self.get_player_information,
                self.search_fpl_players,
                self.get_gameweek_status
                ]

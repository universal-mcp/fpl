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
    
    
    def list_tools(self):
        """
        Lists the available tools (methods) for this application.
        """
        return [self.get_player_information,self.search_fpl_players]

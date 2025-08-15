from universal_mcp.applications import APIApplication
from universal_mcp.integrations import Integration
from typing import Any
from universal_mcp_fpl.helper import get_player_info

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
        """
        return get_player_info(
            player_id,
            player_name,
            start_gameweek,
            end_gameweek,
            include_history,
            include_fixtures
        )

    def list_tools(self):
        """
        Lists the available tools (methods) for this application.
        """
        return [self.get_player_information]

from typing import Optional
from universal_mcp.applications import APIApplication
from universal_mcp.integrations import Integration
from universal_mcp_fpl.schemas import *


class FplApp(APIApplication):
    def __init__(self, integration: Integration = None, **kwargs) -> None:
        super().__init__(name="fplapp", integration=integration, **kwargs)
        self.base_url = "https://v3.football.api-sports.io"

    def get_timezone(self) -> GetTimezoneresponse:
        """
        Timezone

        Returns:
            GetTimezoneresponse: OK

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Timezone
        """
        url = f"{self.base_url}/timezone"
        query_params = {}
        response = self._get(url, params=query_params)
        return GetTimezoneresponse.model_validate(self._handle_response(response))

    def get_countries(
        self,
        name: Optional[str] = None,
        code: Optional[str] = None,
        search: Optional[str] = None,
    ) -> GetCountriesresponse:
        """
        Countries

        Args:
            name (string): The name of the country
            code (string): The Alpha code of the country
            search (string): The name of the country

        Returns:
            GetCountriesresponse: OK

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Countries
        """
        url = f"{self.base_url}/countries"
        query_params = {
            k: v
            for k, v in [("name", name), ("code", code), ("search", search)]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return GetCountriesresponse.model_validate(self._handle_response(response))

    def get_leagues(
        self,
        id: Optional[int] = None,
        name: Optional[str] = None,
        country: Optional[str] = None,
        code: Optional[str] = None,
        season: Optional[int] = None,
        team: Optional[int] = None,
        type: Optional[str] = None,
        current: Optional[str] = None,
        search: Optional[str] = None,
        last: Optional[int] = None,
    ) -> GetLeaguesresponse:
        """
        Leagues

        Args:
            id (integer): The id of the league
            name (string): The name of the league
            country (string): The country name of the league
            code (string): The Alpha code of the country
            season (integer): The season of the league
            team (integer): The id of the team
            type (string): The type of the league
            current (string): The state of the league
            search (string): The name or the country of the league
            last (integer): The X last leagues/cups added in the API

        Returns:
            GetLeaguesresponse: OK

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Leagues
        """
        url = f"{self.base_url}/leagues"
        query_params = {
            k: v
            for k, v in [
                ("id", id),
                ("name", name),
                ("country", country),
                ("code", code),
                ("season", season),
                ("team", team),
                ("type", type),
                ("current", current),
                ("search", search),
                ("last", last),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return GetLeaguesresponse.model_validate(self._handle_response(response))

    def get_seasons(self) -> GetTimezoneresponse:
        """
        Seasons

        Returns:
            GetTimezoneresponse: OK

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Leagues
        """
        url = f"{self.base_url}/leagues/seasons"
        query_params = {}
        response = self._get(url, params=query_params)
        return GetTimezoneresponse.model_validate(self._handle_response(response))

    def get_teams(
        self,
        id: Optional[int] = None,
        name: Optional[str] = None,
        league: Optional[int] = None,
        season: Optional[int] = None,
        country: Optional[str] = None,
        code: Optional[str] = None,
        venue: Optional[int] = None,
        search: Optional[str] = None,
    ) -> GetTeamsresponse:
        """
        Teams information

        Args:
            id (integer): The id of the team
            name (string): The name of the team
            league (integer): The id of the league
            season (integer): The season of the league
            country (string): The country name of the team
            code (string): The code of the team
            venue (integer): The id of the venue
            search (string): The name or the country name of the team

        Returns:
            GetTeamsresponse: OK

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Teams
        """
        url = f"{self.base_url}/teams"
        query_params = {
            k: v
            for k, v in [
                ("id", id),
                ("name", name),
                ("league", league),
                ("season", season),
                ("country", country),
                ("code", code),
                ("venue", venue),
                ("search", search),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return GetTeamsresponse.model_validate(self._handle_response(response))

    def get_teams_statistics(
        self, league: int, season: int, team: int, date: Optional[str] = None
    ) -> GetTeamsStatisticsresponse:
        """
        Teams statistics

        Args:
            league (integer): The id of the league
            season (integer): The season of the league
            team (integer): The id of the team
            date (string): The limit date

        Returns:
            GetTeamsStatisticsresponse: OK

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Teams
        """
        url = f"{self.base_url}/teams/statistics"
        query_params = {
            k: v
            for k, v in [
                ("league", league),
                ("season", season),
                ("team", team),
                ("date", date),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return GetTeamsStatisticsresponse.model_validate(
            self._handle_response(response)
        )

    def get_teams_seasons(self, team: int) -> GetTeamsSeasonsresponse:
        """
        Teams seasons

        Args:
            team (integer): The id of the team

        Returns:
            GetTeamsSeasonsresponse: OK

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Teams
        """
        url = f"{self.base_url}/teams/seasons"
        query_params = {k: v for k, v in [("team", team)] if v is not None}
        response = self._get(url, params=query_params)
        return GetTeamsSeasonsresponse.model_validate(self._handle_response(response))

    def get_teams_countries(self) -> GetTeamsSeasonsresponse:
        """
        Teams countries

        Returns:
            GetTeamsSeasonsresponse: OK

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Teams
        """
        url = f"{self.base_url}/teams/countries"
        query_params = {}
        response = self._get(url, params=query_params)
        return GetTeamsSeasonsresponse.model_validate(self._handle_response(response))

    def get_venues(
        self,
        id: Optional[int] = None,
        name: Optional[str] = None,
        city: Optional[str] = None,
        country: Optional[str] = None,
        search: Optional[str] = None,
    ) -> GetVenuesresponse:
        """
        Venues

        Args:
            id (integer): The id of the venue
            name (string): The name of the venue
            city (string): The city of the venue
            country (string): The country name of the venue
            search (string): The name, city or the country of the venue

        Returns:
            GetVenuesresponse: OK

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Venues
        """
        url = f"{self.base_url}/venues"
        query_params = {
            k: v
            for k, v in [
                ("id", id),
                ("name", name),
                ("city", city),
                ("country", country),
                ("search", search),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return GetVenuesresponse.model_validate(self._handle_response(response))

    def get_standings(
        self, season: int, league: Optional[int] = None, team: Optional[int] = None
    ) -> GetStandingsresponse:
        """
        Standings

        Args:
            season (integer): The season of the league
            league (integer): The id of the league
            team (integer): The id of the team

        Returns:
            GetStandingsresponse: OK

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Standings
        """
        url = f"{self.base_url}/standings"
        query_params = {
            k: v
            for k, v in [("league", league), ("season", season), ("team", team)]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return GetStandingsresponse.model_validate(self._handle_response(response))

    def get_fixtures_rounds(
        self,
        league: int,
        season: int,
        current: Optional[bool] = None,
        dates: Optional[bool] = None,
        timezone: Optional[str] = None,
    ) -> GetStandingsresponse:
        """
        Rounds

        Args:
            league (integer): The id of the league
            season (integer): The season of the league
            current (boolean): The current round only
            dates (boolean): Add the dates of each round in the response
            timezone (string): A valid timezone from the endpoint `Timezone`

        Returns:
            GetStandingsresponse: OK

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Fixtures
        """
        url = f"{self.base_url}/fixtures/rounds"
        query_params = {
            k: v
            for k, v in [
                ("league", league),
                ("season", season),
                ("current", current),
                ("dates", dates),
                ("timezone", timezone),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return GetStandingsresponse.model_validate(self._handle_response(response))

    def get_fixtures(
        self,
        id: Optional[int] = None,
        ids: Optional[str] = None,
        live: Optional[str] = None,
        date: Optional[str] = None,
        league: Optional[int] = None,
        season: Optional[int] = None,
        team: Optional[int] = None,
        last: Optional[int] = None,
        next: Optional[int] = None,
        from_: Optional[str] = None,
        to: Optional[str] = None,
        round: Optional[str] = None,
        status: Optional[str] = None,
        venue: Optional[int] = None,
        timezone: Optional[str] = None,
    ) -> GetStandingsresponse:
        """
        Fixtures

        Args:
            id (integer): The id of the fixture
            ids (string): One or more fixture ids
            live (string): All or several leagues ids
            date (string): A valid date
            league (integer): The id of the league
            season (integer): The season of the league
            team (integer): The id of the team
            last (integer): For the X last fixtures
            next (integer): For the X next fixtures
            from_ (string): A valid date
            to (string): A valid date
            round (string): The round of the fixture
            status (string): One or more fixture status short
            venue (integer): The venue id of the fixture
            timezone (string): A valid timezone from the endpoint `Timezone`

        Returns:
            GetStandingsresponse: OK

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Fixtures
        """
        url = f"{self.base_url}/fixtures"
        query_params = {
            k: v
            for k, v in [
                ("id", id),
                ("ids", ids),
                ("live", live),
                ("date", date),
                ("league", league),
                ("season", season),
                ("team", team),
                ("last", last),
                ("next", next),
                ("from", from_),
                ("to", to),
                ("round", round),
                ("status", status),
                ("venue", venue),
                ("timezone", timezone),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return GetStandingsresponse.model_validate(self._handle_response(response))

    def get_fixtures_headtohead(
        self,
        h2h: str,
        date: Optional[str] = None,
        league: Optional[int] = None,
        season: Optional[int] = None,
        last: Optional[int] = None,
        next: Optional[int] = None,
        from_: Optional[str] = None,
        to: Optional[str] = None,
        status: Optional[str] = None,
        venue: Optional[int] = None,
        timezone: Optional[str] = None,
    ) -> GetStandingsresponse:
        """
        Head To Head

        Args:
            h2h (string): The ids of the teams
            date (string): No description provided.
            league (integer): The id of the league
            season (integer): The season of the league
            last (integer): For the X last fixtures
            next (integer): For the X next fixtures
            from_ (string): No description provided.
            to (string): No description provided.
            status (string): One or more fixture status short
            venue (integer): The venue id of the fixture
            timezone (string): A valid timezone from the endpoint `Timezone`

        Returns:
            GetStandingsresponse: OK

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Fixtures
        """
        url = f"{self.base_url}/fixtures/headtohead"
        query_params = {
            k: v
            for k, v in [
                ("h2h", h2h),
                ("date", date),
                ("league", league),
                ("season", season),
                ("last", last),
                ("next", next),
                ("from", from_),
                ("to", to),
                ("status", status),
                ("venue", venue),
                ("timezone", timezone),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return GetStandingsresponse.model_validate(self._handle_response(response))

    def get_fixtures_statistics(
        self,
        fixture: int,
        team: Optional[int] = None,
        type: Optional[str] = None,
        half: Optional[bool] = None,
    ) -> GetStandingsresponse:
        """
        Statistics

        Args:
            fixture (integer): The id of the fixture
            team (integer): The id of the team
            type (string): The type of statistics
            half (boolean): Add the halftime statistics in the response `Data start from 2024 season for half parameter`

        Returns:
            GetStandingsresponse: OK

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Fixtures
        """
        url = f"{self.base_url}/fixtures/statistics"
        query_params = {
            k: v
            for k, v in [
                ("fixture", fixture),
                ("team", team),
                ("type", type),
                ("half", half),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return GetStandingsresponse.model_validate(self._handle_response(response))

    def get_fixtures_events(
        self,
        fixture: int,
        team: Optional[int] = None,
        player: Optional[int] = None,
        type: Optional[str] = None,
    ) -> GetStandingsresponse:
        """
        Events

        Args:
            fixture (integer): The id of the fixture
            team (integer): The id of the team
            player (integer): The id of the player
            type (string): The type

        Returns:
            GetStandingsresponse: OK

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Fixtures
        """
        url = f"{self.base_url}/fixtures/events"
        query_params = {
            k: v
            for k, v in [
                ("fixture", fixture),
                ("team", team),
                ("player", player),
                ("type", type),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return GetStandingsresponse.model_validate(self._handle_response(response))

    def get_fixtures_lineups(
        self,
        fixture: int,
        team: Optional[int] = None,
        player: Optional[int] = None,
        type: Optional[str] = None,
    ) -> GetStandingsresponse:
        """
        Lineups

        Args:
            fixture (integer): The id of the fixture
            team (integer): The id of the team
            player (integer): The id of the player
            type (string): The type

        Returns:
            GetStandingsresponse: OK

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Fixtures
        """
        url = f"{self.base_url}/fixtures/lineups"
        query_params = {
            k: v
            for k, v in [
                ("fixture", fixture),
                ("team", team),
                ("player", player),
                ("type", type),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return GetStandingsresponse.model_validate(self._handle_response(response))

    def get_fixtures_players(
        self, fixture: int, team: Optional[int] = None
    ) -> GetStandingsresponse:
        """
        Players statistics

        Args:
            fixture (integer): The id of the fixture
            team (integer): The id of the team

        Returns:
            GetStandingsresponse: OK

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Fixtures
        """
        url = f"{self.base_url}/fixtures/players"
        query_params = {
            k: v for k, v in [("fixture", fixture), ("team", team)] if v is not None
        }
        response = self._get(url, params=query_params)
        return GetStandingsresponse.model_validate(self._handle_response(response))

    def get_injuries(
        self,
        league: Optional[int] = None,
        season: Optional[int] = None,
        fixture: Optional[int] = None,
        team: Optional[int] = None,
        player: Optional[int] = None,
        date: Optional[str] = None,
        ids: Optional[str] = None,
        timezone: Optional[str] = None,
    ) -> GetStandingsresponse:
        """
        Injuries

        Args:
            league (integer): The id of the league
            season (integer): The season of the league, **required** with `league`, `team` and `player` parameters
            fixture (integer): The id of the fixture
            team (integer): The id of the team
            player (integer): The id of the player
            date (string): A valid date
            ids (string): One or more fixture ids
            timezone (string): A valid timezone from the endpoint `Timezone`

        Returns:
            GetStandingsresponse: OK

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Injuries
        """
        url = f"{self.base_url}/injuries"
        query_params = {
            k: v
            for k, v in [
                ("league", league),
                ("season", season),
                ("fixture", fixture),
                ("team", team),
                ("player", player),
                ("date", date),
                ("ids", ids),
                ("timezone", timezone),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return GetStandingsresponse.model_validate(self._handle_response(response))

    def get_predictions(self, fixture: int) -> GetStandingsresponse:
        """
        Predictions

        Args:
            fixture (integer): The id of the fixture

        Returns:
            GetStandingsresponse: OK

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Predictions
        """
        url = f"{self.base_url}/predictions"
        query_params = {k: v for k, v in [("fixture", fixture)] if v is not None}
        response = self._get(url, params=query_params)
        return GetStandingsresponse.model_validate(self._handle_response(response))

    def get_coachs(
        self,
        id: Optional[int] = None,
        team: Optional[int] = None,
        search: Optional[str] = None,
    ) -> GetStandingsresponse:
        """
        Coachs

        Args:
            id (integer): The id of the coach
            team (integer): The id of the team
            search (string): The name of the coach

        Returns:
            GetStandingsresponse: OK

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Coachs
        """
        url = f"{self.base_url}/coachs"
        query_params = {
            k: v
            for k, v in [("id", id), ("team", team), ("search", search)]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return GetStandingsresponse.model_validate(self._handle_response(response))

    def get_players_seasons(self, player: Optional[int] = None) -> GetStandingsresponse:
        """
        Seasons

        Args:
            player (integer): The id of the player

        Returns:
            GetStandingsresponse: OK

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Players
        """
        url = f"{self.base_url}/players/seasons"
        query_params = {k: v for k, v in [("player", player)] if v is not None}
        response = self._get(url, params=query_params)
        return GetStandingsresponse.model_validate(self._handle_response(response))

    def get_players_profiles(
        self,
        player: Optional[int] = None,
        search: Optional[str] = None,
        page: Optional[int] = None,
    ) -> GetStandingsresponse:
        """
        Profiles

        Args:
            player (integer): The id of the player
            search (string): The lastname of the player
            page (integer): Use for the pagination

        Returns:
            GetStandingsresponse: OK

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Players
        """
        url = f"{self.base_url}/players/profiles"
        query_params = {
            k: v
            for k, v in [("player", player), ("search", search), ("page", page)]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return GetStandingsresponse.model_validate(self._handle_response(response))

    def get_players(
        self,
        id: Optional[int] = None,
        team: Optional[int] = None,
        league: Optional[int] = None,
        season: Optional[int] = None,
        search: Optional[str] = None,
        page: Optional[int] = None,
    ) -> GetStandingsresponse:
        """
        Statistics

        Args:
            id (integer): The id of the player
            team (integer): The id of the team
            league (integer): The id of the league
            season (integer): The season of the league
            search (string): The name of the player
            page (integer): Use for the pagination

        Returns:
            GetStandingsresponse: OK

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Players
        """
        url = f"{self.base_url}/players"
        query_params = {
            k: v
            for k, v in [
                ("id", id),
                ("team", team),
                ("league", league),
                ("season", season),
                ("search", search),
                ("page", page),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return GetStandingsresponse.model_validate(self._handle_response(response))

    def get_players_squads(
        self, team: Optional[int] = None, player: Optional[int] = None
    ) -> GetStandingsresponse:
        """
        Squads

        Args:
            team (integer): The id of the team
            player (integer): The id of the player

        Returns:
            GetStandingsresponse: OK

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Players
        """
        url = f"{self.base_url}/players/squads"
        query_params = {
            k: v for k, v in [("team", team), ("player", player)] if v is not None
        }
        response = self._get(url, params=query_params)
        return GetStandingsresponse.model_validate(self._handle_response(response))

    def get_players_teams(self, player: int) -> GetStandingsresponse:
        """
        Teams

        Args:
            player (integer): The id of the player

        Returns:
            GetStandingsresponse: OK

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Players
        """
        url = f"{self.base_url}/players/teams"
        query_params = {k: v for k, v in [("player", player)] if v is not None}
        response = self._get(url, params=query_params)
        return GetStandingsresponse.model_validate(self._handle_response(response))

    def get_players_topscorers(self, league: int, season: int) -> GetStandingsresponse:
        """
        Top Scorers

        Args:
            league (integer): The id of the league
            season (integer): The season of the league

        Returns:
            GetStandingsresponse: OK

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Players
        """
        url = f"{self.base_url}/players/topscorers"
        query_params = {
            k: v for k, v in [("league", league), ("season", season)] if v is not None
        }
        response = self._get(url, params=query_params)
        return GetStandingsresponse.model_validate(self._handle_response(response))

    def get_players_topassists(self, league: int, season: int) -> GetStandingsresponse:
        """
        Top Assists

        Args:
            league (integer): The id of the league
            season (integer): The season of the league

        Returns:
            GetStandingsresponse: OK

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Players
        """
        url = f"{self.base_url}/players/topassists"
        query_params = {
            k: v for k, v in [("league", league), ("season", season)] if v is not None
        }
        response = self._get(url, params=query_params)
        return GetStandingsresponse.model_validate(self._handle_response(response))

    def get_players_topyellowcards(
        self, league: int, season: int
    ) -> GetStandingsresponse:
        """
        Top Yellow Cards

        Args:
            league (integer): The id of the league
            season (integer): The season of the league

        Returns:
            GetStandingsresponse: OK

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Players
        """
        url = f"{self.base_url}/players/topyellowcards"
        query_params = {
            k: v for k, v in [("league", league), ("season", season)] if v is not None
        }
        response = self._get(url, params=query_params)
        return GetStandingsresponse.model_validate(self._handle_response(response))

    def get_players_topredcards(self, league: int, season: int) -> GetStandingsresponse:
        """
        Top Red Cards

        Args:
            league (integer): The id of the league
            season (integer): The season of the league

        Returns:
            GetStandingsresponse: OK

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Players
        """
        url = f"{self.base_url}/players/topredcards"
        query_params = {
            k: v for k, v in [("league", league), ("season", season)] if v is not None
        }
        response = self._get(url, params=query_params)
        return GetStandingsresponse.model_validate(self._handle_response(response))

    def get_transfers(
        self, player: Optional[int] = None, team: Optional[int] = None
    ) -> GetStandingsresponse:
        """
        Transfers

        Args:
            player (integer): The id of the player
            team (integer): The id of the team

        Returns:
            GetStandingsresponse: OK

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Transfers
        """
        url = f"{self.base_url}/transfers"
        query_params = {
            k: v for k, v in [("player", player), ("team", team)] if v is not None
        }
        response = self._get(url, params=query_params)
        return GetStandingsresponse.model_validate(self._handle_response(response))

    def get_trophies(
        self,
        player: Optional[int] = None,
        players: Optional[str] = None,
        coach: Optional[int] = None,
        coachs: Optional[str] = None,
    ) -> GetStandingsresponse:
        """
        Trophies

        Args:
            player (integer): The id of the player
            players (string): One or more players ids
            coach (integer): The id of the coach
            coachs (string): One or more coachs ids

        Returns:
            GetStandingsresponse: OK

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Trophies
        """
        url = f"{self.base_url}/trophies"
        query_params = {
            k: v
            for k, v in [
                ("player", player),
                ("players", players),
                ("coach", coach),
                ("coachs", coachs),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return GetStandingsresponse.model_validate(self._handle_response(response))

    def get_sidelined(
        self,
        player: Optional[int] = None,
        players: Optional[str] = None,
        coach: Optional[int] = None,
        coachs: Optional[str] = None,
    ) -> GetStandingsresponse:
        """
        Sidelined

        Args:
            player (integer): The id of the player
            players (string): One or more players ids
            coach (integer): The id of the coach
            coachs (string): One or more coachs ids

        Returns:
            GetStandingsresponse: OK

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Sidelined
        """
        url = f"{self.base_url}/sidelined"
        query_params = {
            k: v
            for k, v in [
                ("player", player),
                ("players", players),
                ("coach", coach),
                ("coachs", coachs),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return GetStandingsresponse.model_validate(self._handle_response(response))

    def get_odds_live(
        self,
        fixture: Optional[int] = None,
        league: Optional[int] = None,
        bet: Optional[int] = None,
    ) -> GetStandingsresponse:
        """
        odds/live

        Args:
            fixture (integer): The id of the fixture
            league (integer): The id of the league
            bet (integer): The id of the bet

        Returns:
            GetStandingsresponse: OK

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Odds (In-Play)
        """
        url = f"{self.base_url}/odds/live"
        query_params = {
            k: v
            for k, v in [("fixture", fixture), ("league", league), ("bet", bet)]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return GetStandingsresponse.model_validate(self._handle_response(response))

    def get_bets(
        self, id: Optional[str] = None, search: Optional[str] = None
    ) -> GetStandingsresponse:
        """
        odds/live/bets

        Args:
            id (string): The id of the bet name
            search (string): The name of the bet

        Returns:
            GetStandingsresponse: OK

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Odds (In-Play)
        """
        url = f"{self.base_url}/odds/live/bets"
        query_params = {
            k: v for k, v in [("id", id), ("search", search)] if v is not None
        }
        response = self._get(url, params=query_params)
        return GetStandingsresponse.model_validate(self._handle_response(response))

    def get_odds(
        self,
        fixture: Optional[int] = None,
        league: Optional[int] = None,
        season: Optional[int] = None,
        date: Optional[str] = None,
        timezone: Optional[str] = None,
        page: Optional[int] = None,
        bookmaker: Optional[int] = None,
        bet: Optional[int] = None,
    ) -> GetStandingsresponse:
        """
        Odds

        Args:
            fixture (integer): The id of the fixture
            league (integer): The id of the league
            season (integer): The season of the league
            date (string): A valid date
            timezone (string): A valid timezone from the endpoint `Timezone`
            page (integer): Use for the pagination
            bookmaker (integer): The id of the bookmaker
            bet (integer): The id of the bet

        Returns:
            GetStandingsresponse: OK

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Odds (Pre-Match)
        """
        url = f"{self.base_url}/odds"
        query_params = {
            k: v
            for k, v in [
                ("fixture", fixture),
                ("league", league),
                ("season", season),
                ("date", date),
                ("timezone", timezone),
                ("page", page),
                ("bookmaker", bookmaker),
                ("bet", bet),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return GetStandingsresponse.model_validate(self._handle_response(response))

    def get_odds_mapping(self, page: Optional[int] = None) -> GetStandingsresponse:
        """
        Mapping

        Args:
            page (integer): Use for the pagination

        Returns:
            GetStandingsresponse: OK

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Odds (Pre-Match)
        """
        url = f"{self.base_url}/odds/mapping"
        query_params = {k: v for k, v in [("page", page)] if v is not None}
        response = self._get(url, params=query_params)
        return GetStandingsresponse.model_validate(self._handle_response(response))

    def get_bookmakers(
        self, id: Optional[int] = None, search: Optional[str] = None
    ) -> GetStandingsresponse:
        """
        Bookmakers

        Args:
            id (integer): The id of the bookmaker
            search (string): The name of the bookmaker

        Returns:
            GetStandingsresponse: OK

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Odds (Pre-Match)
        """
        url = f"{self.base_url}/odds/bookmakers"
        query_params = {
            k: v for k, v in [("id", id), ("search", search)] if v is not None
        }
        response = self._get(url, params=query_params)
        return GetStandingsresponse.model_validate(self._handle_response(response))

    def get_bets(
        self, id: Optional[str] = None, search: Optional[str] = None
    ) -> GetStandingsresponse:
        """
        Bets

        Args:
            id (string): The id of the bet name
            search (string): The name of the bet

        Returns:
            GetStandingsresponse: OK

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Odds (Pre-Match)
        """
        url = f"{self.base_url}/odds/bets"
        query_params = {
            k: v for k, v in [("id", id), ("search", search)] if v is not None
        }
        response = self._get(url, params=query_params)
        return GetStandingsresponse.model_validate(self._handle_response(response))




    def list_tools(self):
        return [
            self.get_timezone,
            self.get_countries,
            self.get_leagues,
            self.get_seasons,
            self.get_teams,
            self.get_teams_statistics,
            self.get_teams_seasons,
            self.get_teams_countries,
            self.get_venues,
            self.get_standings,
            self.get_fixtures_rounds,
            self.get_fixtures,
            self.get_fixtures_headtohead,
            self.get_fixtures_statistics,
            self.get_fixtures_events,
            self.get_fixtures_lineups,
            self.get_fixtures_players,
            self.get_injuries,
            self.get_predictions,
            self.get_coachs,
            self.get_players_seasons,
            self.get_players_profiles,
            self.get_players,
            self.get_players_squads,
            self.get_players_teams,
            self.get_players_topscorers,
            self.get_players_topassists,
            self.get_players_topyellowcards,
            self.get_players_topredcards,
            self.get_transfers,
            self.get_trophies,
            self.get_sidelined,
            self.get_odds_live,
            self.get_bets,
            self.get_odds,
            self.get_odds_mapping,
            self.get_bookmakers,
            self.get_bets,
          
        ]

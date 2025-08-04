from typing import Any, Optional, List
from universal_mcp.applications import APIApplication
from universal_mcp.integrations import Integration
from .schemas import *


class FplApp(APIApplication):

    def __init__(self, integration: Integration = None, **kwargs) -> None:
        super().__init__(name="fplapp", integration=integration, **kwargs)
        self.base_url = "https://v3.football.api-sports.io"

    def get_timezone(self) -> GetTimezoneresponse:
        """
        Retrieves the time zone information for a specified location or request context, requiring an API key in the header.

        Returns:
            GetTimezoneresponse: OK

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Timezone, readOnlyHint, openWorldHint"""
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
        Retrieves a list of countries filtered optionally by name, code, or search query, requiring an API key in the header.

        Args:
            name (string): The name of the country to filter results by when retrieving country data.
            code (string): The ISO 3166-1 alpha-2 code representing a country, consisting of two uppercase letters used to uniquely identify countries and territories in queries.
            search (string): Filters the list of countries to include only those whose names contain the specified search term (case-insensitive).

        Returns:
            GetCountriesresponse: OK

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Countries, readOnlyHint, openWorldHint"""
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
        Retrieves a filtered list of leagues based on optional query parameters such as id, name, country, season, team, type, current status, or search terms.

        Args:
            id (integer): The unique identifier of the league to retrieve specific league details; used as a query parameter in the GET /leagues request.
            name (string): The 'name' query parameter specifies the exact or partial name of the league to filter the list of leagues returned by the API.
            country (string): The country parameter specifies the name of the country associated with the league to filter the results accordingly.
            code (string): The Alpha-2 or Alpha-3 country code used to filter leagues by their country in the query.
            season (integer): The season parameter specifies the year or period for which the league data is requested, typically formatted as a four-digit year or a defined season range.
            team (integer): The unique identifier of the team to filter leagues associated with that specific team in the query results.
            type (string): Specifies the category or classification of the league to filter results by league type in the query.
            current (string): Filters the list of leagues to return only those currently active when set to true, or all leagues when false or omitted.
            search (string): Filter leagues by specifying a search term that matches either the league's name or its country.
            last (integer): Specify the number of most recently added leagues or cups to return from the API, ordered by their addition date.

        Returns:
            GetLeaguesresponse: OK

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Leagues, readOnlyHint, openWorldHint"""
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
        Retrieves a list of available league seasons.

        Returns:
            GetTimezoneresponse: OK

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Leagues, readOnlyHint, openWorldHint"""
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
        Retrieves a list of football teams filtered by parameters such as team ID, name, league, season, country, code, venue, or search query.

        Args:
            id (integer): The unique identifier of the team to retrieve specific team details when querying the list of teams.
            name (string): The name of the team to filter results by when retrieving the list of teams via the query parameter.
            league (integer): The league query parameter specifies the unique identifier of the league to filter the teams returned by this endpoint.
            season (integer): The league season to filter teams by, specified in a year or year range format (e.g., 2023 or 2023-2024).
            country (string): The country query parameter filters teams by their associated country, accepting a standardized country name or ISO code to specify the team's location.
            code (string): The unique identifier code used to filter and retrieve a specific team in the query parameters of the GET /teams request.
            venue (integer): The unique identifier of the venue used to filter the list of teams returned by this query parameter.
            search (string): Filter teams by matching their name or the country they represent using this query parameter.

        Returns:
            GetTeamsresponse: OK

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Teams, readOnlyHint, openWorldHint"""
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
        Retrieves detailed statistical data for a specific team in a given league and season, optionally filtered by date, requiring an API key for authorization.

        Args:
            league (integer): The league query parameter specifies the unique identifier of the league for which team statistics are requested.
            season (integer): The season parameter specifies the league season (e.g., 2024-2025) for which team statistics are requested.
            team (integer): The unique identifier of the team for which statistics are being requested, used as a query parameter to specify the target team in the GET /teams/statistics API call.
            date (string): The date to limit the statistics returned, formatted as an ISO 8601 date string (YYYY-MM-DD).

        Returns:
            GetTeamsStatisticsresponse: OK

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Teams, readOnlyHint, openWorldHint"""
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
        Retrieves a list of seasons associated with a specified team using the team ID provided in the query parameter.

        Args:
            team (integer): The unique identifier of the team for which season data is requested, used as a query parameter to filter results by team.

        Returns:
            GetTeamsSeasonsresponse: OK

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Teams, readOnlyHint, openWorldHint"""
        url = f"{self.base_url}/teams/seasons"
        query_params = {k: v for k, v in [("team", team)] if v is not None}
        response = self._get(url, params=query_params)
        return GetTeamsSeasonsresponse.model_validate(self._handle_response(response))

    def get_teams_countries(self) -> GetTeamsSeasonsresponse:
        """
        Retrieves a list of countries and regions registered in the system, including details such as country ID, name, ISO code, and targeting availability.

        Returns:
            GetTeamsSeasonsresponse: OK

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Teams, readOnlyHint, openWorldHint"""
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
        Retrieves a list of venues filtered by optional parameters such as id, name, city, country, or search term, requiring an API key for authorization.

        Args:
            id (integer): The unique identifier of the venue to retrieve specific venue details when making a GET request to the /venues endpoint.
            name (string): The 'name' query parameter filters venues by their exact or partial name to help locate specific venues when retrieving a list.
            city (string): The city name to filter venues by location when making a GET request to the /venues endpoint.
            country (string): The country query parameter filters venues by specifying the full or partial name of the country where the venue is located.
            search (string): A text query to search venues by their name, city, or country, allowing flexible location-based filtering.

        Returns:
            GetVenuesresponse: OK

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Venues, readOnlyHint, openWorldHint"""
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
        Retrieves the current standings for a specified league, season, and optionally a team, requiring an API key in the header.

        Args:
            season (integer): The season parameter specifies the year or range of years for the league season to retrieve standings data for, formatted as a string.
            league (integer): The league query parameter specifies the unique identifier of the league for which the standings are requested.
            team (integer): The unique identifier of the team to filter the standings results by a specific team.

        Returns:
            GetStandingsresponse: OK

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Standings, readOnlyHint, openWorldHint"""
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
        Retrieves fixture round details for a specified league and season, with optional filtering by current rounds, date inclusion, and timezone adjustment.

        Args:
            league (integer): The league query parameter specifies the unique identifier of the league for which you want to retrieve fixture rounds, enabling filtering of results by that league.
            season (integer): Specifies the league season (e.g., year or year range) to filter fixture rounds for that particular competition period.
            current (boolean): Filter the response to include only the current active round of fixtures when set to true; otherwise, return all rounds.
            dates (boolean): Include the specific dates for each round in the response to provide detailed scheduling information for the fixtures.
            timezone (string): Specify a valid IANA timezone identifier to adjust the fixture round times to the desired local time zone.

        Returns:
            GetStandingsresponse: OK

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Fixtures, readOnlyHint, openWorldHint"""
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
        Retrieves a list of football fixtures filtered by various query parameters such as date, league, team, status, and venue, accessible within the user's subscription.

        Args:
            id (integer): The unique identifier of the fixture to retrieve, passed as a query parameter to filter the results by a specific fixture.
            ids (string): Comma-separated list of one or more fixture IDs to filter and retrieve specific fixture details in the response.
            live (string): Filter fixtures by live status: set to true to return only currently live matches, or false to include all fixtures regardless of live status.
            date (string): The date parameter accepts a valid ISO 8601 formatted date (YYYY-MM-DD) to filter fixtures occurring on that specific day.
            league (integer): The league query parameter specifies the unique identifier of the league for which you want to retrieve fixture data.
            season (integer): The season parameter specifies the league season (e.g., 2023-2024) to filter fixtures by that competition year in the query.
            team (integer): The unique identifier of the team to filter fixtures by, returning only matches involving this specific team.
            last (integer): Specifies the number of most recent fixtures to retrieve, returning the last X fixtures in the response.
            next (integer): Specifies the number of upcoming fixtures to return in the response, limiting the results to the next X scheduled events.
            from_ (string): Start date for filtering fixtures in ISO 8601 format (YYYY-MM-DD); only fixtures on or after this date will be included in the response.
            to (string): The 'to' query parameter specifies the end date (in ISO 8601 format) to filter fixtures occurring on or before this date.
            round (string): Specifies the round number or stage of the fixture within the tournament or league schedule to filter the results accordingly.
            status (string): Filter fixtures by one or more short status codes representing their current state (e.g., scheduled, live, finished) passed as query parameters.
            venue (integer): The venue query parameter specifies the unique identifier of the venue where the fixture takes place, used to filter fixtures by their location.
            timezone (string): Specify a valid timezone identifier string to display fixture times adjusted to that timezone.

        Returns:
            GetStandingsresponse: OK

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Fixtures, readOnlyHint, openWorldHint"""
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
        Retrieves head-to-head match data between specified teams with optional filters such as date, league, season, and venue.

        Args:
            h2h (string): Comma-separated list of team IDs to retrieve head-to-head fixture data between the specified teams.
            date (string): Date filter in ISO 8601 string format (e.g., "YYYY-MM-DD") to specify the fixtures' date for the head-to-head query.
            league (integer): The league query parameter specifies the unique identifier of the league for which you want to retrieve head-to-head fixture data.
            season (integer): Specifies the league season (e.g., 2023-2024) to filter fixtures for that particular competition period in the head-to-head query.
            last (integer): Specifies the number of most recent head-to-head fixtures to return.
            next (integer): Specifies the number of upcoming fixtures to retrieve in the head-to-head comparison results.
            from_ (string): Starting point or reference value for filtering or retrieving data in the query parameters.
            to (string): The "to" query parameter specifies the target team or entity for the head-to-head fixtures comparison in the GET /fixtures/headtohead operation.
            status (string): Filter fixtures by one or more short status codes indicating their current state, such as scheduled, live, or finished.
            venue (integer): The venue parameter specifies the unique identifier of the venue where the fixture is scheduled to take place, used to filter head-to-head fixture data by location.
            timezone (string): Specify a valid timezone identifier to adjust the timestamps in the response to the desired local time zone.

        Returns:
            GetStandingsresponse: OK

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Fixtures, readOnlyHint, openWorldHint"""
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
        Retrieves detailed statistical data for a specified fixture, optionally filtered by team, statistic type, and half of the match, requiring an API key in the header.

        Args:
            fixture (integer): The unique identifier of the fixture for which statistical data is requested, provided as a query parameter.
            team (integer): The unique identifier of the team for which statistics are requested in the fixture.
            type (string): Specifies the category of statistics to retrieve for the fixture, such as player, team, or event-based statistics, to tailor the data returned.
            half (boolean): Include halftime statistics in the response when the 'half' query parameter is set. Data for this parameter is available starting from the 2024 season.

        Returns:
            GetStandingsresponse: OK

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Fixtures, readOnlyHint, openWorldHint"""
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
        Retrieves event details for a specified fixture, optionally filtered by team, player, or event type, requiring an API key for authorization.

        Args:
            fixture (integer): The unique identifier of the fixture for which event details are requested, provided as a query parameter to filter results.
            team (integer): The unique identifier of the team for which you want to retrieve fixture events, used to filter results by a specific team in the query.
            player (integer): The unique identifier of the player to filter event data for that specific player in the response.
            type (string): Specifies the event type to filter results by, such as goals, cards, substitutions, or other match events.

        Returns:
            GetStandingsresponse: OK

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Fixtures, readOnlyHint, openWorldHint"""
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
        Retrieves the lineup details for a specified fixture, optionally filtered by team, player, or lineup type.

        Args:
            fixture (integer): The unique identifier of the fixture (match) for which lineup details are requested, provided as a query parameter.
            team (integer): The unique identifier of the team for which you want to retrieve lineup information in the fixture query.
            player (integer): The unique identifier of the player to filter the lineup information for a specific player in the fixture.
            type (string): Specifies the category or classification of lineups to retrieve, such as starting lineup or substitutes, to filter the fixture lineups returned by the API.

        Returns:
            GetStandingsresponse: OK

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Fixtures, readOnlyHint, openWorldHint"""
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
        Retrieves a list of players participating in a specified fixture, optionally filtered by team, requiring an API key for access.

        Args:
            fixture (integer): The unique identifier of the fixture for which player information is requested, passed as a query parameter.
            team (integer): The unique identifier of the team for which player fixture data is requested, used to filter results by team in the query.

        Returns:
            GetStandingsresponse: OK

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Fixtures, readOnlyHint, openWorldHint"""
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
        Retrieves a list of players who are potentially injured and may not participate in a match, filtered by league, season, fixture, team, player, date, and timezone.

        Args:
            league (integer): The unique identifier of the league for which injury data is requested, used to filter results by that specific league.
            season (integer): Specifies the season of the league and is required when using the league, team, or player parameters to filter injury data.
            fixture (integer): The unique identifier of the fixture (match or event) for which injury data is requested in the query.
            team (integer): The unique identifier of the team to filter injury data, provided as a query parameter to retrieve injuries specific to that team.
            player (integer): The unique identifier of the player for whom injury information is requested, passed as a query parameter to filter the results.
            date (string): The date parameter specifies the injury date to filter results; it must be a valid ISO 8601 date string in YYYY-MM-DD format.
            ids (string): One or more fixture IDs to filter injury records, provided as a comma-separated list in the query string.
            timezone (string): Specify a valid IANA timezone identifier (e.g., America/New_York) to indicate the timezone context for the request, ensuring date and time fields are interpreted correctly.

        Returns:
            GetStandingsresponse: OK

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Injuries, readOnlyHint, openWorldHint"""
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
        Retrieves predictions for a specified fixture using a required API key provided in the request header.

        Args:
            fixture (integer): The unique identifier of the fixture for which predictions are requested, used to specify the specific match in the query.

        Returns:
            GetStandingsresponse: OK

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Predictions, readOnlyHint, openWorldHint"""
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
        Retrieves a list of coaches filtered optionally by ID, team, or search query, requiring an API key for authorization.

        Args:
            id (integer): The unique identifier of the coach to retrieve, passed as a query parameter to filter the results by a specific coach.
            team (integer): The unique identifier of the team to filter coaches by team when making the GET request.
            search (string): Filter coaches by their full or partial name to retrieve matching results.

        Returns:
            GetStandingsresponse: OK

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Coachs, readOnlyHint, openWorldHint"""
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
        Retrieves season-specific statistics for a specified player using their player ID.

        Args:
            player (integer): The unique identifier of the player to retrieve season data for, provided as a query parameter.

        Returns:
            GetStandingsresponse: OK

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Players, readOnlyHint, openWorldHint"""
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
        Retrieves player profiles based on optional player ID, search query, and pagination parameters using a required API key in the header.

        Args:
            player (integer): The unique identifier of the player to retrieve detailed profile information in the query parameters of the request.
            search (string): Filter player profiles by last name; provide a partial or full lastname string to search for matching players in the database.
            page (integer): Specifies the page number to retrieve in paginated results, allowing navigation through large sets of player profiles by dividing data into manageable pages.

        Returns:
            GetStandingsresponse: OK

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Players, readOnlyHint, openWorldHint"""
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
        Retrieves a filtered list of players based on optional query parameters such as id, team, league, season, and search term, requiring an API key in the header.

        Args:
            id (integer): The unique identifier of the player to retrieve specific player details in the query parameters of the GET /players request.
            team (integer): The unique identifier of the team used to filter and return only players belonging to that specific team in the query results.
            league (integer): The league query parameter specifies the unique identifier (ID) of the league to filter players by that league in the GET /players request.
            season (integer): The season parameter specifies the league season to filter players by, typically formatted as a year range (e.g., 2023/2024), representing the period when the league games are played.
            search (string): Filter players by their name using this query parameter to search for matching player records in the database.
            page (integer): Specifies the page number to retrieve in paginated results, allowing navigation through large sets of players by dividing data into manageable pages.

        Returns:
            GetStandingsresponse: OK

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Players, readOnlyHint, openWorldHint"""
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
        Retrieves the current squad of a specified team or all teams a specified player has been part of using optional team or player query parameters.

        Args:
            team (integer): The unique identifier of the team to filter the player squads returned by this endpoint.
            player (integer): The unique identifier of the player to retrieve squad information for, provided as a query parameter.

        Returns:
            GetStandingsresponse: OK

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Players, readOnlyHint, openWorldHint"""
        url = f"{self.base_url}/players/squads"
        query_params = {
            k: v for k, v in [("team", team), ("player", player)] if v is not None
        }
        response = self._get(url, params=query_params)
        return GetStandingsresponse.model_validate(self._handle_response(response))

    def get_players_teams(self, player: int) -> GetStandingsresponse:
        """
        Retrieves the list of teams associated with a specified player, requiring the player ID as a query parameter and an API key in the header.

        Args:
            player (integer): The unique identifier of the player used to filter and retrieve teams associated with that specific player in the query.

        Returns:
            GetStandingsresponse: OK

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Players, readOnlyHint, openWorldHint"""
        url = f"{self.base_url}/players/teams"
        query_params = {k: v for k, v in [("player", player)] if v is not None}
        response = self._get(url, params=query_params)
        return GetStandingsresponse.model_validate(self._handle_response(response))

    def get_players_topscorers(self, league: int, season: int) -> GetStandingsresponse:
        """
        Retrieves the top scorers for a specified league and season using the provided API key.

        Args:
            league (integer): The league query parameter specifies the unique identifier of the league for which you want to retrieve the top scorers.
            season (integer): The season parameter specifies the league season (e.g., 2023-2024) for which to retrieve the top scorers, ensuring results are filtered by the selected competition period.

        Returns:
            GetStandingsresponse: OK

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Players, readOnlyHint, openWorldHint"""
        url = f"{self.base_url}/players/topscorers"
        query_params = {
            k: v for k, v in [("league", league), ("season", season)] if v is not None
        }
        response = self._get(url, params=query_params)
        return GetStandingsresponse.model_validate(self._handle_response(response))

    def get_players_topassists(self, league: int, season: int) -> GetStandingsresponse:
        """
        Retrieves the top assist providers for a specified league and season using the provided API key.

        Args:
            league (integer): The league query parameter specifies the unique identifier (ID) of the league for which top assist player data is requested.
            season (integer): Specifies the league season to filter the top assists data, typically formatted as a year or year range (e.g., 2023 or 2023-2024).

        Returns:
            GetStandingsresponse: OK

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Players, readOnlyHint, openWorldHint"""
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
        Retrieves the list of players with the highest number of yellow cards in a specified league and season.

        Args:
            league (integer): The unique identifier of the league for which to retrieve the players with the most yellow cards; provided as a query parameter to filter results accordingly.
            season (integer): The league season to filter the player data for top yellow cards, specified as a year or range (e.g., 2023 or 2023-2024).

        Returns:
            GetStandingsresponse: OK

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Players, readOnlyHint, openWorldHint"""
        url = f"{self.base_url}/players/topyellowcards"
        query_params = {
            k: v for k, v in [("league", league), ("season", season)] if v is not None
        }
        response = self._get(url, params=query_params)
        return GetStandingsresponse.model_validate(self._handle_response(response))

    def get_players_topredcards(self, league: int, season: int) -> GetStandingsresponse:
        """
        Retrieves the top players with the most red cards in a specified league and season.

        Args:
            league (integer): The league query parameter specifies the unique identifier (ID) of the league for which to retrieve the top players with the most red cards.
            season (integer): Specify the league season year or range (e.g., 2023 or 2023-2024) to filter the top red card players for that particular competition period.

        Returns:
            GetStandingsresponse: OK

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Players, readOnlyHint, openWorldHint"""
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
        Retrieves a list of player or team transfers filtered by optional query parameters for player ID or team ID, requiring an API key in the header.

        Args:
            player (integer): The unique identifier of the player to filter transfer records by; provide the player's ID as a query parameter.
            team (integer): The unique identifier of the team to filter transfer records, allowing retrieval of transfers associated with a specific team.

        Returns:
            GetStandingsresponse: OK

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Transfers, readOnlyHint, openWorldHint"""
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
        Retrieves trophies information filtered by player(s) or coach(es) using required API key authentication.

        Args:
            player (integer): The unique identifier of the player whose trophies are being requested, provided as a query parameter.
            players (string): One or more player IDs to filter the trophies returned by the API; specify multiple IDs separated by commas to retrieve data for multiple players in a single request.
            coach (integer): The unique identifier of the coach to filter trophies by, provided as a query parameter.
            coachs (string): One or more coach IDs to filter the trophies by specific coaches; pass as a comma-separated list in the query string.

        Returns:
            GetStandingsresponse: OK

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Trophies, readOnlyHint, openWorldHint"""
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
        Retrieves sidelined player and coach information based on optional query parameters for player(s) and coach(es), requiring an API key in the header.

        Args:
            player (integer): The unique identifier of the player to retrieve sidelined status for, specified as a query parameter.
            players (string): Comma-separated list of one or more player IDs to filter sidelined players in the query.
            coach (integer): The unique identifier of the coach used to filter sidelined players in the query.
            coachs (string): Comma-separated list of one or more coach IDs to filter sidelined data by specific coaches in the query parameters of the request.

        Returns:
            GetStandingsresponse: OK

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Sidelined, readOnlyHint, openWorldHint"""
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
        Retrieves live betting odds for ongoing games filtered by fixture, league, or bet type.

        Args:
            fixture (integer): The unique identifier of the fixture (match) for which live odds data is requested, used to filter and retrieve information about that specific event.
            league (integer): The unique identifier of the league for which to retrieve live odds data, provided as a query parameter to filter results by league.
            bet (integer): The unique identifier of the bet to retrieve live odds and related information for a specific betting market.

        Returns:
            GetStandingsresponse: OK

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Odds (In-Play), readOnlyHint, openWorldHint"""
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
        Retrieves live betting odds and related information for ongoing sports events based on optional filters such as event ID or search terms.

        Args:
            id (string): The unique identifier of the bet for which live odds are requested, specified as a query parameter.
            search (string): Filter live bets by specifying the exact name of the bet to search for in the query parameters.

        Returns:
            GetStandingsresponse: OK

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Odds (In-Play), readOnlyHint, openWorldHint"""
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
        Retrieves betting odds for upcoming, live, or recently completed sports events filtered by fixture, league, season, date, bookmaker, and betting market parameters.

        Args:
            fixture (integer): The unique identifier of the specific sports fixture (match or event) for which odds data is requested, used to filter results in the query.
            league (integer): The unique identifier of the league for which odds data is requested, used as a query parameter to filter results by that specific league.
            season (integer): The season year or identifier for the league to filter odds data, typically formatted as a calendar year or league-specific season code.
            date (string): The date parameter specifies the desired date for filtering odds and must be provided in ISO 8601 format (YYYY-MM-DD) to ensure accuracy and consistency.
            timezone (string): Specifies the valid timezone string to use for date and time values in the query, ensuring timestamps are interpreted and returned in the specified timezone.
            page (integer): Specifies the page number to retrieve in paginated results, enabling navigation through large datasets by dividing responses into manageable pages.
            bookmaker (integer): The unique identifier of the bookmaker to filter odds results by a specific bookmaker in the query.
            bet (integer): The unique identifier of the bet to retrieve odds for, specified as a query parameter.

        Returns:
            GetStandingsresponse: OK

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Odds (Pre-Match), readOnlyHint, openWorldHint"""
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
        Retrieves a paginated mapping of bookmaker event IDs for fixtures, requiring an API key for access.

        Args:
            page (integer): Specifies the page number to retrieve in paginated results, enabling navigation through large data sets by dividing them into manageable pages.

        Returns:
            GetStandingsresponse: OK

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Odds (Pre-Match), readOnlyHint, openWorldHint"""
        url = f"{self.base_url}/odds/mapping"
        query_params = {k: v for k, v in [("page", page)] if v is not None}
        response = self._get(url, params=query_params)
        return GetStandingsresponse.model_validate(self._handle_response(response))

    def get_bookmakers(
        self, id: Optional[int] = None, search: Optional[str] = None
    ) -> GetStandingsresponse:
        """
        Retrieves a list of all available bookmakers with optional filtering by bookmaker ID or search term.

        Args:
            id (integer): The unique identifier of the bookmaker used to filter odds data in the query.
            search (string): The name of the bookmaker to filter the odds results; use this query parameter to retrieve data for a specific bookmaker.

        Returns:
            GetStandingsresponse: OK

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Odds (Pre-Match), readOnlyHint, openWorldHint"""
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
        Retrieves betting odds and related information for specified bets using query parameters and requires an API key in the header.

        Args:
            id (string): The unique identifier of the bet to retrieve odds for, specified as a query parameter.
            search (string): Filter bets by specifying a search term that matches the name or title of the bet you want to retrieve.

        Returns:
            GetStandingsresponse: OK

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Odds (Pre-Match), readOnlyHint, openWorldHint"""
        url = f"{self.base_url}/odds/bets"
        query_params = {
            k: v for k, v in [("id", id), ("search", search)] if v is not None
        }
        response = self._get(url, params=query_params)
        return GetStandingsresponse.model_validate(self._handle_response(response))

    def get_widget_games(
        self,
        data_host: str,
        data_key: str,
        data_refresh: Optional[int] = None,
        data_date: Optional[str] = None,
        data_league: Optional[int] = None,
        data_season: Optional[int] = None,
        data_theme: Optional[str] = None,
        data_show_toolbar: Optional[str] = None,
        data_show_logos: Optional[str] = None,
        data_modal_game: Optional[str] = None,
        data_modal_standings: Optional[str] = None,
        data_modal_show_logos: Optional[str] = None,
        data_show_errors: Optional[str] = None,
    ) -> GetWidgetGamesresponse:
        """
        Retrieves game data with customizable query parameters for host, key, date, league, season, theme, display options, and modal settings.

        Args:
            data_host (string): Specifies the data host to query, required to be either "v3.football.api-sports.io" or "api-football-v1.p.rapidapi.com".
            data_key (string): API key provided as a query parameter named 'data-key'; required to authenticate and authorize access to the GET /widgets/Games endpoint.
            data_refresh (integer): Time interval in seconds for automatic data refresh. Set to 0 or omit to disable automatic updates and keep data static until manually refreshed.
            data_date (string): Specify the desired date for the query in YYYY-MM-DD format; if left empty, the current date will be used automatically.
            data_league (integer): Specify the ID of the league to filter games by that particular league in the query results.
            data_season (integer): Specify the season to filter game data, using the format or identifier recognized by the API (e.g., year or season code).
            data_theme (string): Specify the theme for the widget display; leave empty to use the default theme, or set to "grey" or "dark" for alternate styles.
            data_show_toolbar (string): If set to true, displays a toolbar that lets users switch views among current, finished, or upcoming fixtures and select dates for filtering game widgets.
            data_show_logos (string): If set to true, this query parameter enables the display of team logos in the game widgets response.
            data_modal_game (string): If set to true, loads a modal window displaying detailed information about the selected game.
            data_modal_standings (string): If set to true, this query parameter enables loading a modal window that displays the current standings related to the games.
            data_modal_show_logos (string): If set to true, displays team logos and player images within the game modal window for enhanced visual context.
            data_show_errors (string): Controls whether error details are shown in the response for debugging; defaults to false, set to true to enable error display.

        Returns:
            GetWidgetGamesresponse: Successful response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Widgets, readOnlyHint, openWorldHint"""
        url = f"{self.base_url}/widgets/Games"
        query_params = {
            k: v
            for k, v in [
                ("data-host", data_host),
                ("data-key", data_key),
                ("data-refresh", data_refresh),
                ("data-date", data_date),
                ("data-league", data_league),
                ("data-season", data_season),
                ("data-theme", data_theme),
                ("data-show-toolbar", data_show_toolbar),
                ("data-show-logos", data_show_logos),
                ("data-modal-game", data_modal_game),
                ("data-modal-standings", data_modal_standings),
                ("data-modal-show-logos", data_modal_show_logos),
                ("data-show-errors", data_show_errors),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return GetWidgetGamesresponse.model_validate(self._handle_response(response))

    def get_widget_game(
        self,
        data_host: str,
        data_key: str,
        data_refresh: Optional[int] = None,
        data_id: Optional[int] = None,
        data_theme: Optional[str] = None,
        data_show_errors: Optional[str] = None,
        data_show_logos: Optional[str] = None,
    ) -> GetWidgetGamesresponse:
        """
        Retrieves game widget data based on specified query parameters such as data host, key, refresh rate, ID, theme, and display options.

        Args:
            data_host (string): Specifies the data host to use for the request; must be either "v3.football.api-sports.io" or "api-football-v1.p.rapidapi.com".
            data_key (string): The API key required for authentication, passed as a query parameter named 'data-key', to authorize and access the GET /widgets/game endpoint.
            data_refresh (integer): Interval in seconds defining how often the data should refresh automatically; set to 0 or omit to disable automatic updates.
            data_id (integer): Unique identifier of the fixture to retrieve details for; provide the desired fixture ID as a query parameter in the request.
            data_theme (string): Specifies the theme for the game widget; defaults to "default" if empty, or can be set to "grey" or "dark" to change the appearance accordingly.
            data_show_errors (string): Controls whether errors are shown in the response for debugging; defaults to false, set to true to display error details.
            data_show_logos (string): If set to true, includes team logos and player images in the game widget display.

        Returns:
            GetWidgetGamesresponse: Successful response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Widgets, readOnlyHint, openWorldHint"""
        url = f"{self.base_url}/widgets/game"
        query_params = {
            k: v
            for k, v in [
                ("data-host", data_host),
                ("data-key", data_key),
                ("data-refresh", data_refresh),
                ("data-id", data_id),
                ("data-theme", data_theme),
                ("data-show-errors", data_show_errors),
                ("data-show-logos", data_show_logos),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return GetWidgetGamesresponse.model_validate(self._handle_response(response))

    def get_widget_standings(
        self,
        data_host: str,
        data_key: str,
        data_season: int,
        data_league: Optional[int] = None,
        data_team: Optional[int] = None,
        data_theme: Optional[str] = None,
        data_show_errors: Optional[str] = None,
        data_show_logos: Optional[str] = None,
    ) -> GetWidgetGamesresponse:
        """
        Retrieves the current standings for widgets based on specified league, team, season, and display options provided via query parameters.

        Args:
            data_host (string): Specifies the required data source host for the API request, with allowed values "v3.football.api-sports.io" or "api-football-v1.p.rapidapi.com".
            data_key (string): API key required for authentication to access the standings data; include this key as a query parameter to authorize your GET request.
            data_season (integer): Specify the season for which you want to retrieve standings data, formatted as a year or year range (e.g., 2023 or 2023-2024).
            data_league (integer): Specify the league ID to retrieve standings for that particular league in the query.
            data_team (integer): Specify the unique identifier of the team to retrieve its standings in the response.
            data_theme (string): Optional query parameter to set the widget's color theme. Defaults to `default` if omitted; valid values are `grey` and `dark`.
            data_show_errors (string): If set to true, enables display of error messages in the response for debugging purposes; defaults to false to hide errors.
            data_show_logos (string): If set to true, includes team logos in the standings widget response; if false or omitted, logos are not displayed.

        Returns:
            GetWidgetGamesresponse: Successful response

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Widgets, readOnlyHint, openWorldHint"""
        url = f"{self.base_url}/widgets/standings"
        query_params = {
            k: v
            for k, v in [
                ("data-host", data_host),
                ("data-key", data_key),
                ("data-league", data_league),
                ("data-team", data_team),
                ("data-season", data_season),
                ("data-theme", data_theme),
                ("data-show-errors", data_show_errors),
                ("data-show-logos", data_show_logos),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return GetWidgetGamesresponse.model_validate(self._handle_response(response))

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
            self.get_widget_games,
            self.get_widget_game,
            self.get_widget_standings,
        ]

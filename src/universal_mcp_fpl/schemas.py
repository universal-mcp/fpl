from typing import Any, Optional, List
from pydantic import BaseModel, Field

# Generated Response Models


class GetTimezoneresponseParametersItem(BaseModel):
    field: Optional[str] = None


class GetTimezoneresponseErrorsItem(BaseModel):
    field: Optional[str] = None


class GetTimezoneresponse(BaseModel):
    get: Optional[str] = None
    parameters: Optional[List[GetTimezoneresponseParametersItem]] = None
    errors: Optional[List[GetTimezoneresponseErrorsItem]] = None
    results: Optional[int] = None
    response: Optional[List[str]] = None


class GetCountriesresponseParametersItem(BaseModel):
    field: Optional[str] = None


class GetCountriesresponseErrorsItem(BaseModel):
    field: Optional[str] = None


class GetCountriesresponseResponseItem(BaseModel):
    name: Optional[str] = None
    code: Optional[str] = None
    flag: Optional[str] = None


class GetCountriesresponse(BaseModel):
    get: Optional[str] = None
    parameters: Optional[List[GetCountriesresponseParametersItem]] = None
    errors: Optional[List[GetCountriesresponseErrorsItem]] = None
    results: Optional[int] = None
    response: Optional[List[GetCountriesresponseResponseItem]] = None


class GetLeaguesresponseParametersItem(BaseModel):
    field: Optional[str] = None


class GetLeaguesresponseErrorsItem(BaseModel):
    field: Optional[str] = None


class GetLeaguesresponseResponseItemSeasonsItem(BaseModel):
    year: Optional[int] = None
    start: Optional[str] = None
    end: Optional[str] = None
    current: Optional[bool] = None
    coverage: Optional[dict[str, Any]] = None


class GetLeaguesresponseResponseItem(BaseModel):
    league: Optional[dict[str, Any]] = None
    country: Optional[dict[str, Any]] = None
    seasons: Optional[List[GetLeaguesresponseResponseItemSeasonsItem]] = None


class GetLeaguesresponse(BaseModel):
    get: Optional[str] = None
    parameters: Optional[List[GetLeaguesresponseParametersItem]] = None
    errors: Optional[List[GetLeaguesresponseErrorsItem]] = None
    results: Optional[int] = None
    response: Optional[List[GetLeaguesresponseResponseItem]] = None


class GetTeamsresponseParametersItem(BaseModel):
    field: Optional[str] = None


class GetTeamsresponseErrorsItem(BaseModel):
    field: Optional[str] = None


class GetTeamsresponseResponseItem(BaseModel):
    team: Optional[dict[str, Any]] = None
    venue: Optional[dict[str, Any]] = None


class GetTeamsresponse(BaseModel):
    get: Optional[str] = None
    parameters: Optional[List[GetTeamsresponseParametersItem]] = None
    errors: Optional[List[GetTeamsresponseErrorsItem]] = None
    results: Optional[int] = None
    response: Optional[List[GetTeamsresponseResponseItem]] = None


class GetTeamsStatisticsresponseParametersItem(BaseModel):
    field: Optional[str] = None


class GetTeamsStatisticsresponseErrorsItem(BaseModel):
    field: Optional[str] = None


class GetTeamsStatisticsresponse(BaseModel):
    get: Optional[str] = None
    parameters: Optional[List[GetTeamsStatisticsresponseParametersItem]] = None
    errors: Optional[List[GetTeamsStatisticsresponseErrorsItem]] = None
    results: Optional[int] = None
    response: Optional[dict[str, Any]] = None


class GetTeamsSeasonsresponseParametersItem(BaseModel):
    field: Optional[str] = None


class GetTeamsSeasonsresponseErrorsItem(BaseModel):
    field: Optional[str] = None


class GetTeamsSeasonsresponse(BaseModel):
    get: Optional[str] = None
    parameters: Optional[List[GetTeamsSeasonsresponseParametersItem]] = None
    errors: Optional[List[GetTeamsSeasonsresponseErrorsItem]] = None
    results: Optional[int] = None
    response: Optional[List[Any]] = None


class GetVenuesresponseParametersItem(BaseModel):
    field: Optional[str] = None


class GetVenuesresponseErrorsItem(BaseModel):
    field: Optional[str] = None


class GetVenuesresponseResponseItem(BaseModel):
    id: Optional[int] = None
    name: Optional[str] = None
    address: Optional[str] = None
    city: Optional[str] = None
    country: Optional[str] = None
    capacity: Optional[int] = None
    surface: Optional[str] = None
    image: Optional[str] = None


class GetVenuesresponse(BaseModel):
    get: Optional[str] = None
    parameters: Optional[List[GetVenuesresponseParametersItem]] = None
    errors: Optional[List[GetVenuesresponseErrorsItem]] = None
    results: Optional[int] = None
    response: Optional[List[GetVenuesresponseResponseItem]] = None


class GetStandingsresponseParametersItem(BaseModel):
    field: Optional[str] = None


class GetStandingsresponseErrorsItem(BaseModel):
    field: Optional[str] = None


class GetStandingsresponse(BaseModel):
    get: Optional[str] = None
    parameters: Optional[List[GetStandingsresponseParametersItem]] = None
    errors: Optional[List[GetStandingsresponseErrorsItem]] = None
    results: Optional[int] = None
    response: Optional[List[Any]] = None



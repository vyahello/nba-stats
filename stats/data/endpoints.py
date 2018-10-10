from abc import ABC, abstractmethod
from typing import Dict, Any
from stats.support.tools.date import Date
from stats.support.web_api.requests import Request, BotRequest
from stats.support.web_api.urls import Url


class Endpoint(ABC):
    """Abstract interface for some data set endpoint."""

    @abstractmethod
    def as_dict(self) -> Dict[Any, Any]:
        pass

    @abstractmethod
    def name(self) -> str:
        pass


class _Scoreboard(Endpoint):
    """NBA scoreboard interface endpoint data set."""

    def __init__(self, date: str) -> None:
        self._request: Request = BotRequest(Url('http://data.nba.net/10s/prod/v1', date, '/scoreboard.json'))

    def as_dict(self) -> Dict[Any, Any]:
        return self._request.get().as_dict()

    def name(self) -> str:
        return 'NBA Scoreboard'


class TodayScoreboard(Endpoint):
    """NBA scoreboard interface endpoint data set for today."""

    def __init__(self, date: Date) -> None:
        self._request: Endpoint = _Scoreboard(date.today())

    def as_dict(self) -> Dict[Any, Any]:
        return self._request.as_dict()

    def name(self) -> str:
        return "NBA today's Scoreboard"


class YesterdayScoreboard(Endpoint):
    """NBA scoreboard interface endpoint data set for yesterday."""

    def __init__(self, date: Date) -> None:
        self._request: Endpoint = _Scoreboard(date.yesterday())

    def as_dict(self) -> Dict[Any, Any]:
        return self._request.as_dict()

    def name(self) -> str:
        return "NBA yesterday's Scoreboard"


class TomorrowScoreboard(Endpoint):
    """NBA scoreboard interface endpoint data set for tomorrow."""

    def __init__(self, date: Date) -> None:
        self._request: Endpoint = _Scoreboard(date.tomorrow())

    def as_dict(self) -> Dict[Any, Any]:
        return self._request.as_dict()

    def name(self) -> str:
        return "NBA tomorrow's Scoreboard"

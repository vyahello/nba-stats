from abc import ABC, abstractmethod
from typing import Dict, Any
from stats.support.web_api.requests import Request, BotRequest
from stats.support.web_api.urls import Url


class Endpoint(ABC):
    """Abstract interface for some data set endpoint."""

    @abstractmethod
    def as_dict(self) -> Dict[Any, Any]:
        pass


class Scoreboard(Endpoint):
    """NBA scoreboard interface endpoint data set."""

    def __init__(self, date: str) -> None:
        self._request: Request = BotRequest(Url('http://data.nba.net/10s/prod/v1', date, '/scoreboard.json'))

    def as_dict(self) -> Dict[Any, Any]:
        return self._request.get().as_dict()



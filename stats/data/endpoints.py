from abc import ABC, abstractmethod
from functools import lru_cache
from typing import Dict, Any
from stats.support.web_api.requests import Request, BotRequest
from stats.support.web_api.urls import Url


class Endpoint(ABC):
    """Abstract interface for some data set endpoint."""

    @abstractmethod
    def as_dict(self) -> Dict[Any, Any]:
        pass


class UnifiedEndpoint(Endpoint):
    """Unified statistics interface endpoint data set."""

    def __init__(self, *path: Any) -> None:
        self._request: Request = BotRequest(Url('http://data.nba.net/10s/prod/v1', *path))

    @lru_cache()
    def as_dict(self) -> Dict[Any, Any]:
        """Decorate method to be invoked only once in a life cycle."""
        return self._request.get().as_dict()

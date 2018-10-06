from abc import ABC, abstractmethod
from typing import Dict, Any
from stats.support.web_api.responses import Response
from stats.support.web_api.session import Session, SafeBotSession
from stats.support.web_api.urls import Url


class Request(ABC):
    """The abstraction of a specific API request."""

    @abstractmethod
    def get(self) -> Response:
        pass

    @abstractmethod
    def post(self, data: Dict[Any, Any]) -> Response:
        pass


class BotRequest(Request):
    """Provide bot api requests methods. """

    def __init__(self, url: Url) -> None:
        self._session: Session = SafeBotSession(url)

    def get(self) -> Response:
        return self._session.get()

    def post(self, data: Dict[Any, Any]) -> Response:
        return self._session.post(data)

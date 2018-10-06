from abc import ABC, abstractmethod
from typing import Dict, Any, Callable
import requests
from stats.support.web_api.responses import Response, BotResponse, ResponseError
from stats.support.web_api.urls import Url


class Session(ABC):
    """Abstract interfaces for API Session."""

    @abstractmethod
    def get(self) -> Response:
        pass

    @abstractmethod
    def post(self, data: Dict[Any, Any]) -> Response:
        pass


class _BotSession(Session):
    """Provide interfaces for bot api session."""

    def __init__(self, url: Url) -> None:
        self._api: requests.Session = requests.Session()
        self._url = url

    def get(self) -> Response:
        return BotResponse(self._api.get(str(self._url)))

    def post(self, data: Dict[Any, Any]) -> Response:
        return BotResponse(self._api.post(str(self._url), json=data))


class SafeBotSession(Session):
    """Provide interfaces for safe bot api session.
    Raise an error if specific HTTP status code is not presented.
    """

    def __init__(self, url: Url, codes: int = (200, 204)) -> None:

        def safe(response: Response) -> Response:
            code: int = response.status_code()
            if code not in codes:
                raise ResponseError(f'HTTP response error with {code} status code!!!')
            return response

        self._session: Session = _BotSession(url)
        self._safe: Callable[[Response], Response] = safe

    def get(self) -> Response:
        return self._safe(self._session.get())

    def post(self, data: Dict[Any, Any]) -> Response:
        return self._safe(self._session.post(data))

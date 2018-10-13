from abc import ABC, abstractmethod
from functools import lru_cache
from typing import Dict, Any, Callable
from stats.bot.handler import BotHandler, Handler
from stats.support.server import requests
from stats.support.web_api.requests import Request, BotRequest
from stats.support.web_api.responses import Response
from stats.support.web_api.urls import Url


class Answer(ABC):
    """Abstraction for a answer."""

    @abstractmethod
    def chat_id(self) -> int:
        pass

    @abstractmethod
    def message(self) -> str:
        pass


class Message(ABC):
    """Abstraction for a message."""

    @abstractmethod
    def send(self) -> Dict[Any, Any]:
        pass


class BotAnswer(Answer):
    """An answer from a bot."""

    def __init__(self, request: requests.Request) -> None:

        @lru_cache()
        def _req() -> Dict[Any, Any]:
            return request.as_dict()['message']

        self._req: Callable[..., Dict[Any, Any]] = _req

    def chat_id(self) -> int:
        return self._req()['chat']['id']

    def message(self) -> str:
        return self._req()['text']


class BotMessage(Message):
    """A message of a bot."""

    _api_token: str = '674111678:AAHFLwhuM4_OmJ8CT0vrXmY5cYGOYanQle4'

    def __init__(self, chat_id: int, user_input: str) -> None:
        self._chat_id: int = chat_id
        self._handler: Handler = BotHandler(user_input)
        self._request: Request = BotRequest(Url('https://api.telegram.org', f'bot{self._api_token}', 'sendMessage'))

    def send(self) -> Response:
        return self._request.post({'chat_id': self._chat_id, 'text': self._handler.text()})

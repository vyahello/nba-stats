from abc import ABC, abstractmethod
from typing import Dict, Any
from flask import request
from werkzeug.local import LocalProxy


class Request(ABC):
    """Abstraction of a request."""

    @abstractmethod
    def method(self) -> str:
        pass

    @abstractmethod
    def as_dict(self) -> Dict[Any, Any]:
        pass


class ServerRequest(Request):
    """Concrete server request."""

    def __init__(self) -> None:
        self._request: LocalProxy = request

    def method(self) -> str:
        return self._request.method

    def as_dict(self) -> Dict[Any, Any]:
        return self._request.get_json()

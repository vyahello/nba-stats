from abc import ABC, abstractmethod
from re import sub, match


class Text(ABC):
    """Abstraction of a text."""

    @abstractmethod
    def get(self) -> str:
        pass

    @abstractmethod
    def match(self, pattern: str) -> bool:
        pass

    @abstractmethod
    def substitute(self, pattern: str, replace: str) -> str:
        pass


class InputText(Text):
    """Parse input message."""

    def __init__(self, text: str) -> None:
        self._text: str = text

    def get(self) -> str:
        return self._text

    def match(self, pattern: str) -> bool:
        return match(pattern, self._text)

    def substitute(self, pattern: str, replace: str) -> str:
        return sub(pattern, replace, self._text)

from abc import ABC, abstractmethod
from datetime import date


class Format(ABC):
    """Represent abstraction for formatting."""

    @abstractmethod
    def as_str(self) -> str:
        pass


class FormatTime(Format):
    """Represent date time formatter."""

    def __init__(self, dt: date, fmt: str) -> None:
        self._dt = dt
        self._fmt: str = fmt

    def as_str(self) -> str:
        return self._dt.strftime(self._fmt)

from datetime import date, timedelta
from abc import ABC, abstractmethod


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


class Date:
    """Represent date time object."""

    def __init__(self, fmt: str = '%m%d%y', days: int = 1) -> None:
        self._fmt: str = fmt
        self._today: date = date.today()
        self._diff: timedelta = timedelta(days)

    def today(self) -> str:
        return FormatTime(self._today, self._fmt).as_str()

    def yesterday(self) -> str:
        return FormatTime(self._today-self._diff, self._fmt).as_str()

    def tomorrow(self) -> str:
        return FormatTime(self._today+self._diff, self._fmt).as_str()

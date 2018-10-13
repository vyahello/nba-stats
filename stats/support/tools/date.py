from abc import ABC, abstractmethod
from datetime import date, timedelta
from stats.support.tools.format import FormatTime


class StampTime(ABC):
    """Represent abstraction of time stamp interface."""

    @abstractmethod
    def today(self) -> str:
        pass

    @abstractmethod
    def yesterday(self) -> str:
        pass

    @abstractmethod
    def tomorrow(self) -> str:
        pass

    @abstractmethod
    def custom(self, day: str) -> str:
        pass


class Date(StampTime):
    """Represent date time object."""

    def __init__(self, fmt: str = '%Y-%m-%d') -> None:
        self._fmt: str = fmt
        self._today: date = date.today()
        self._day: timedelta = timedelta(1)

    def today(self) -> str:
        return FormatTime(self._today, self._fmt).as_str()

    def yesterday(self) -> str:
        return FormatTime(self._today - self._day, self._fmt).as_str()

    def tomorrow(self) -> str:
        return FormatTime(self._today + self._day, self._fmt).as_str()

    def custom(self, day: str) -> str:
        return day

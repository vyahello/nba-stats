from datetime import date, timedelta
from abc import ABC, abstractmethod
from stats.support.tools.format import FormatTime


class Date(ABC):
    """Represent abstraction of date interface."""

    @abstractmethod
    def today(self) -> str:
        pass

    @abstractmethod
    def yesterday(self) -> str:
        pass

    @abstractmethod
    def tomorrow(self) -> str:
        pass


class DateStamp(Date):
    """Represent date time object."""

    def __init__(self, fmt: str = '%Y%m%d', days: int = 1) -> None:
        self._fmt: str = fmt
        self._today: date = date.today()
        self._diff: timedelta = timedelta(days)

    def today(self) -> str:
        return FormatTime(self._today, self._fmt).as_str()

    def yesterday(self) -> str:
        return FormatTime(self._today - self._diff, self._fmt).as_str()

    def tomorrow(self) -> str:
        return FormatTime(self._today + self._diff, self._fmt).as_str()

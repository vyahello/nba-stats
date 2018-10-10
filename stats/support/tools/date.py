from datetime import date, timedelta
from stats.support.tools.format import FormatTime
from stats.types import StampTime


class Date(StampTime):
    """Represent date time object."""

    def __init__(self, fmt: str = '%Y%m%d') -> None:
        self._fmt: str = fmt
        self._today: date = date.today()
        self._day: timedelta = timedelta(1)

    def today(self) -> str:
        return FormatTime(self._today, self._fmt).as_str()

    def yesterday(self) -> str:
        return FormatTime(self._today - self._day, self._fmt).as_str()

    def tomorrow(self) -> str:
        return FormatTime(self._today + self._day, self._fmt).as_str()

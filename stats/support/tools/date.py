from datetime import date, timedelta


class Date:
    """Represent data time object."""

    def __init__(self) -> None:
        self._format: str = '%m%d%y'
        self._today: date = date.today()
        self._day: timedelta = timedelta(1)

    def today(self) -> str:
        return self._today.strftime(self._format)

    def yesterday(self) -> str:
        return (self._today-self._day).strftime(self._format)

    def tomorrow(self) -> str:
        return (self._today+self._day).strftime(self._format)

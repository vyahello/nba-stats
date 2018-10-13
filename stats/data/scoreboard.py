from abc import ABC, abstractmethod
from typing import List, Any, Callable
from stats.data.endpoints import UnifiedEndpoint
from stats.support.tools.date import StampTime
from stats.support.tools.text import Text


class Scoreboard(ABC):
    """Represent abstract interface for a scoreboard."""

    @abstractmethod
    def date(self) -> str:
        pass

    @abstractmethod
    def num_games(self) -> int:
        pass

    @abstractmethod
    def games(self) -> List[Any]:
        pass


class _UnifiedScoreboard(Scoreboard):
    """Represent specific scoreboard object."""

    def __init__(self, date: str) -> None:
        self._date = date
        self._scoreboard: Callable = lambda: UnifiedEndpoint(''.join(date.split('-')), '/scoreboard.json')

    def date(self) -> str:
        return self._date

    def num_games(self) -> int:
        return self._scoreboard().as_dict()['numGames']

    def games(self) -> List[Any]:
        return self._scoreboard().as_dict()['games']


class TodayScoreboard(Scoreboard):
    """Today's scoreboard object endpoint data set."""

    def __init__(self, date: StampTime) -> None:
        self._today: Scoreboard = _UnifiedScoreboard(date.today())

    def date(self) -> str:
        return self._today.date()

    def num_games(self) -> int:
        return self._today.num_games()

    def games(self) -> List[Any]:
        return self._today.games()


class YesterdayScoreboard(Scoreboard):
    """Yesterday's scoreboard object endpoint data set."""

    def __init__(self, date: StampTime) -> None:
        self._yesterday: Scoreboard = _UnifiedScoreboard(date.yesterday())

    def date(self) -> str:
        return self._yesterday.date()

    def num_games(self) -> int:
        return self._yesterday.num_games()

    def games(self) -> List[Any]:
        return self._yesterday.games()


class TomorrowScoreboard(Scoreboard):
    """Tomorrow's scoreboard object endpoint data set."""

    def __init__(self, date: StampTime) -> None:
        self._tomorrow: Scoreboard = _UnifiedScoreboard(date.tomorrow())

    def date(self) -> str:
        return self._tomorrow.date()

    def num_games(self) -> int:
        return self._tomorrow.num_games()

    def games(self) -> List[Any]:
        return self._tomorrow.games()


class CustomScoreboard(Scoreboard):
    """Custom scoreboard object endpoint data set."""

    def __init__(self, date: StampTime, day: Text) -> None:
        self._date = date
        self._day = day
        self._custom = lambda: _UnifiedScoreboard(date.custom(day.substitute(pattern='-+', replace='')))

    def date(self) -> str:
        return self._date.custom(self._day.get())

    def num_games(self) -> int:
        return self._custom().num_games()

    def games(self) -> List[Any]:
        return self._custom().games()

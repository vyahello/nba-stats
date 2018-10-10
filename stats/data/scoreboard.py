from abc import ABC, abstractmethod
from typing import List, Any
from stats.data.endpoints import Endpoint, UnifiedEndpoint
from stats.types import StampTime


class Scoreboard(ABC):
    """Represent abstract interface for a scoreboard."""

    @abstractmethod
    def num_games(self) -> int:
        pass

    @abstractmethod
    def games(self) -> List[Any]:
        pass


class _UnifiedScoreboard(Scoreboard):
    """Represent specific scoreboard object."""

    def __init__(self, date: str) -> None:
        self._scoreboard: Endpoint = UnifiedEndpoint(date, '/scoreboard.json')

    def num_games(self) -> int:
        return self._scoreboard.as_dict()['numGames']

    def games(self) -> List[Any]:
        return self._scoreboard.as_dict()['games']


class TodayScoreboard(Scoreboard):
    """Today's scoreboard object endpoint data set."""

    def __init__(self, date: StampTime) -> None:
        self._today: Scoreboard = _UnifiedScoreboard(date.today())

    def num_games(self) -> int:
        return self._today.num_games()

    def games(self) -> List[Any]:
        return self._today.games()


class YesterdayScoreboard(Scoreboard):
    """Yesterday's scoreboard object endpoint data set."""

    def __init__(self, date: StampTime) -> None:
        self._yesterday: Scoreboard = _UnifiedScoreboard(date.yesterday())

    def num_games(self) -> int:
        return self._yesterday.num_games()

    def games(self) -> List[Any]:
        return self._yesterday.games()


class TomorrowScoreboard(Scoreboard):
    """Tomorrow's scoreboard object endpoint data set."""

    def __init__(self, date: StampTime) -> None:
        self._tomorrow: Scoreboard = _UnifiedScoreboard(date.tomorrow())

    def num_games(self) -> int:
        return self._tomorrow.num_games()

    def games(self) -> List[Any]:
        return self._tomorrow.games()

from abc import ABC, abstractmethod
from functools import lru_cache
from typing import Dict, Any, Iterator
from stats.data.scoreboard import Scoreboard
from stats.data.teams import Teams, NbaTeams


class Game(ABC):
    """Abstract interface for a game."""

    @abstractmethod
    def id_(self) -> str:
        pass

    @abstractmethod
    def highlight(self) -> str:
        pass

    @abstractmethod
    def period(self) -> str:
        pass

    @abstractmethod
    def teams(self) -> Teams:
        pass


class Games(ABC):
    """Abstract interface for some games"""

    @abstractmethod
    def __next__(self) -> Game:
        pass

    @abstractmethod
    def __iter__(self) -> Iterator[Game]:
        pass

    @abstractmethod
    def __len__(self) -> int:
        pass

    @abstractmethod
    def date(self) -> str:
        pass


class NbaGame(Game):
    """Represent specific game implementation."""

    def __init__(self, data: Dict[Any, Any]) -> None:
        self._data = data
        self._teams = NbaTeams(data)

    def id_(self) -> str:
        return self._data['gameId']

    def highlight(self) -> str:
        return self._data['nugget']['text']

    def period(self) -> str:
        return self._data['tags'][0]

    def teams(self) -> NbaTeams:
        return self._teams


class NbaGames(Games):
    """Represent set of games implementation."""

    def __init__(self, scoreboard: Scoreboard) -> None:

        @lru_cache()
        def games() -> Iterator[Game]:
            for data in scoreboard.games():
                yield NbaGame(data)

        self._games = games
        self._scoreboard = scoreboard

    def __next__(self) -> Game:
        return next(self._games())

    def __iter__(self) -> Iterator[Game]:
        return self

    def __len__(self) -> int:
        return self._scoreboard.num_games()

    def date(self) -> str:
        return self._scoreboard.date()


from abc import ABC, abstractmethod
from typing import Dict, Any, Iterator
from stats.data.scoreboard import Scoreboard
from stats.data.teams import NbaTeams


class Game(ABC):
    """Abstract interface for a game."""

    @abstractmethod
    def id_(self) -> str:
        pass

    @abstractmethod
    def highlight(self) -> str:
        pass

    @abstractmethod
    def tags(self) -> str:
        pass

    @abstractmethod
    def teams(self) -> NbaTeams:
        pass


class Games(ABC):
    """Abstract interface for some games"""

    @abstractmethod
    def game(self) -> Iterator[Game]:
        pass

    @abstractmethod
    def __len__(self) -> int:
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

    def tags(self) -> str:
        return self._data['tags'][0]

    def teams(self) -> NbaTeams:
        return self._teams


class NbaGames(Games):
    """Represent set of games implementation."""

    def __init__(self, scoreboard: Scoreboard) -> None:
        self._scoreboard = scoreboard

    def game(self) -> Iterator[Game]:
        for data in self._scoreboard.games():
            yield NbaGame(data)

    def __len__(self) -> int:
        return self._scoreboard.num_games()

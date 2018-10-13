from abc import ABC, abstractmethod
from stats.league.scoreboard.boxscore import BoxScores, NbaBoxScores
from stats.league.scoreboard.info import GamesScoresInfo
from stats.support.tools.date import Date


class Handler(ABC):
    """Abstract interface for a handler."""

    @abstractmethod
    def perform(self) -> str:
        pass


class BotHandler(Handler):
    """Represent boxscore handler."""

    def __init__(self, day: str) -> None:
        self._day = day
        self._box_scores: BoxScores = NbaBoxScores(Date(), GamesScoresInfo)

    def perform(self) -> str:
        if self._day == 'yesterday':
            return self._box_scores.yesterday().show()
        elif self._day == 'today':
            return self._box_scores.today().show()
        elif self._day == 'tomorrow':
            return self._box_scores.today().show()
        raise ValueError(f'{self._day} day is not supported!')

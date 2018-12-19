from abc import ABC, abstractmethod
from stats.league.scoreboard.boxscore import BoxScores, NbaBoxScores, BoxScore
from stats.league.scoreboard.info import GamesScoresInfo
from stats.support.tools.date import Date
from stats.support.tools.text import InputText


class Handler(ABC):
    """Abstract interface for a handler."""

    @abstractmethod
    def text(self) -> BoxScore:
        pass


class BotHandler(Handler):
    """Represent box score handler."""

    def __init__(self, day: str) -> None:
        self._box_scores: BoxScores = NbaBoxScores(Date(), GamesScoresInfo)
        self._day = day
        self._date = InputText(day)

    def text(self) -> BoxScore:
        if self._day == '/yesterday':
            return self._box_scores.yesterday()
        if self._day == '/today':
            return self._box_scores.today()
        if self._day == '/tomorrow':
            return self._box_scores.tomorrow()
        if self._date.match(pattern='\d+-\d+-\d+'):
            return self._box_scores.custom(self._day)
        return self._box_scores.empty(self._day)

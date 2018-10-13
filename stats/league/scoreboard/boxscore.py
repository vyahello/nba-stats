from abc import abstractmethod, ABC
from stats.data.games import NbaGames, Games
from stats.data.scoreboard import YesterdayScoreboard
from stats.league.scoreboard.info import GamesScoresInfo
from stats.support.tools.date import StampTime
from stats.types import Information


class BoxScore(ABC):
    """Represent abstraction of a box score."""

    @abstractmethod
    def show(self) -> str:
        pass


class YesterdayBoxScore(BoxScore):
    """Represent yestarday's scores for a set of games."""

    def __init__(self, date: StampTime) -> None:
        self._games: Games = NbaGames(YesterdayScoreboard(date))
        self._info: Information = GamesScoresInfo(self._games)

    def show(self) -> str:
        return f'{len(self._games)} games were played on {self._games.date()}\n {self._info.display()}'

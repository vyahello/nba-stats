from abc import abstractmethod, ABC
from typing import Type, Callable
from stats.data.games import NbaGames, Games
from stats.data.scoreboard import YesterdayScoreboard, TodayScoreboard, TomorrowScoreboard
from stats.league.scoreboard.info import GamesScoresInfo
from stats.support.tools.date import StampTime


class BoxScore(ABC):
    """Represent abstraction of a box score."""

    @abstractmethod
    def show(self) -> str:
        pass


class BoxScores(ABC):
    """Represent abstraction of a box scores."""

    @abstractmethod
    def today(self) -> BoxScore:
        pass

    @abstractmethod
    def yesterday(self) -> BoxScore:
        pass

    @abstractmethod
    def tomorrow(self) -> BoxScore:
        pass


class YesterdayBoxScore(BoxScore):
    """Represent yestarday's scores for a set of games."""

    def __init__(self, date: StampTime, games_info: Type[GamesScoresInfo]) -> None:
        self._games: Games = NbaGames(YesterdayScoreboard(date))
        self._info = games_info(self._games)

    def show(self) -> str:
        return f'{len(self._games)} games were played on {self._games.date()}\n {self._info.display()}'


class TodayBoxScore(BoxScore):
    """Represent today's scores for a set of games."""

    def __init__(self, date: StampTime, games_info: Callable) -> None:
        self._games: Games = NbaGames(TodayScoreboard(date))
        self._info = games_info(self._games)

    def show(self) -> str:
        return f'{len(self._games)} games are played on {self._games.date()}\n {self._info.display()}'


class TomorrowBoxScore(BoxScore):
    """Represent today's scores for a set of games."""

    def __init__(self, date: StampTime, games_info: Callable) -> None:
        self._games: Games = NbaGames(TomorrowScoreboard(date))
        self._info = games_info(self._games)

    def show(self) -> str:
        return f'{len(self._games)} games will be played on {self._games.date()}\n {self._info.display()}'


class NbaBoxScores(BoxScores):
    """Represent certain box scores."""

    def __init__(self, date: StampTime, games_info: Callable) -> None:
        self._yesterday: BoxScore = YesterdayBoxScore(date, games_info)
        self._today: BoxScore = TodayBoxScore(date, games_info)
        self._tomorrow: BoxScore = TomorrowBoxScore(date, games_info)

    def yesterday(self) -> BoxScore:
        return self._yesterday

    def today(self) -> BoxScore:
        return self._today

    def tomorrow(self) -> BoxScore:
        return self._tomorrow

from abc import ABC, abstractmethod
from typing import List, Dict, Any


class Score(ABC):
    """Abstract interface for team score."""

    @abstractmethod
    def first_quarter(self) -> str:
        pass

    @abstractmethod
    def second_quarter(self) -> str:
        pass

    @abstractmethod
    def third_quarter(self) -> str:
        pass

    @abstractmethod
    def fourth_quarter(self) -> str:
        pass


class Team:
    """Abstract interface for team object."""

    @abstractmethod
    def id_(self) -> str:
        pass

    @abstractmethod
    def name(self) -> str:
        pass

    @abstractmethod
    def win(self) -> str:
        pass

    @abstractmethod
    def loss(self) -> str:
        pass

    @abstractmethod
    def score(self) -> str:
        pass

    @abstractmethod
    def line_score(self) -> Score:
        pass


class Teams:
    """Abstract interface for team pair."""

    def home_team(self) -> Team:
        pass

    def visit_team(self) -> Team:
        pass


class _LineScore(Score):
    """Linescore of a team."""

    def __init__(self, line_score: List) -> None:

        def score(quarter: int) -> str:
            return line_score[quarter]['score']

        self._score = score

    def first_quarter(self) -> str:
        return self._score(1)

    def second_quarter(self) -> str:
        return self._score(2)

    def third_quarter(self) -> str:
        return self._score(3)

    def fourth_quarter(self) -> str:
        return self._score(4)


class NbaTeam(Team):
    """Specific team object."""

    def __init__(self, data: Dict[Any, Any]) -> None:
        self._data = data

    def id_(self) -> str:
        return self._data['teamId']

    def name(self) -> str:
        return self._data['triCode']

    def win(self) -> str:
        return self._data['win']

    def loss(self) -> str:
        return self._data['loss']

    def score(self) -> str:
        return self._data['score']

    def line_score(self) -> _LineScore:
        return _LineScore(self._data['linescore'])


class NbaTeams(Teams):
    """Represent team pair for a particular game"""

    def __init__(self, data: Dict[Any, Any]) -> None:
        self._data = data

    def home_team(self) -> NbaTeam:
        return NbaTeam(self._data['hTeam'])

    def visit_team(self) -> NbaTeam:
        return NbaTeam(self._data['vTeam'])

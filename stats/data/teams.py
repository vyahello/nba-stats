from abc import ABC, abstractmethod
from typing import Dict, Any, Iterable
from stats.types import NotAvailable


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

    @abstractmethod
    def all(self) -> str:
        pass


class Team(ABC):
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


class Teams(ABC):
    """Abstract interface for team pair."""

    @abstractmethod
    def home_team(self) -> Team:
        pass

    @abstractmethod
    def visit_team(self) -> Team:
        pass


class _SaveScores:
    """Decorate save scores object."""

    def __init__(self, line_score: Dict) -> None:
        self._line_score = line_score

    def by_quarter(self, quarter: int) -> str:
        try:
            return self._line_score[quarter]['score']
        except IndexError:
            return str(NotAvailable())


class _LineScore(Score):
    """Linescore of a team."""

    def __init__(self, line_score: Dict) -> None:
        self._score = _SaveScores(line_score)

    def first_quarter(self) -> str:
        return self._score.by_quarter(0)

    def second_quarter(self) -> str:
        return self._score.by_quarter(1)

    def third_quarter(self) -> str:
        return self._score.by_quarter(2)

    def fourth_quarter(self) -> str:
        return self._score.by_quarter(3)

    def all(self) -> Iterable[str]:
        return (
            self.first_quarter(),
            self.second_quarter(),
            self.third_quarter(),
            self.fourth_quarter()
        )


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
        return str(NotAvailable(self._data['score']))

    def line_score(self) -> _LineScore:
        return _LineScore(self._data['linescore'])


class NbaTeams(Teams):
    """Represent team pair for a particular game"""

    def __init__(self, data: Dict[Any, Any]) -> None:
        self._data = data

    def home_team(self) -> Team:
        return NbaTeam(self._data['hTeam'])

    def visit_team(self) -> Team:
        return NbaTeam(self._data['vTeam'])

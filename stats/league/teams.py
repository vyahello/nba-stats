from abc import ABC, abstractmethod
from functools import lru_cache
from typing import Iterator


class Team(ABC):
    """Abstract interface for some teams."""

    pass


class Teams(ABC):
    """Abstract interface for some teams."""

    @abstractmethod
    def __next__(self) -> Team:
        pass

    @abstractmethod
    def __iter__(self) -> Iterator[Team]:
        pass


class Atlanta(Team):
    """Represent `Atlanta Hawks` nba team."""

    full_name: str = 'Atlanta Hawks'
    tri_code: str = 'ATL'
    team_id: str = '1610612737'
    nick_name: str = 'Hawks'
    url_name: str = 'hawks'


class Boston(Team):
    """Represent `Boston Celtics` nba team."""

    full_name: str = 'Boston Celtics'
    tri_code: str = 'BOS'
    team_id: str = '1610612738'
    nick_name: str = 'Celtics'
    url_name: str = 'celtics'


class Brooklyn(Team):
    """Represent `Brooklyn Nets` nba team."""

    full_name: str = 'Brooklyn Nets'
    tri_code: str = 'BKN'
    team_id: str = '1610612751'
    nick_name: str = 'Brooklyn'
    url_name: str = 'nets'


class Charlotte(Team):
    """Represent `Charlotte Hornets` nba team."""

    full_name: str = 'Charlotte Hornets'
    tri_code: str = 'CHA'
    team_id: str = '1610612766'
    nick_name: str = 'Hornets'
    url_name: str = 'hornets'


class Chicago(Team):
    """Represent `Chicago Bulls` nba team."""

    full_name: str = 'Chicago Bulls'
    tri_code: str = 'CHI'
    team_id: str = '1610612741'
    nick_name: str = 'Bulls'
    url_name: str = 'bulls'


class Cleveland(Team):
    """Represent `Cleveland Cavaliers` nba team."""

    full_name: str = 'Cleveland Cavaliers'
    tri_code: str = 'CLE'
    team_id: str = '1610612739'
    nick_name: str = 'Cavaliers'
    url_name: str = 'cavaliers'


class Dallas(Team):
    """Represent `Dallas Mavericks` nba team."""

    full_name: str = 'Dallas Mavericks'
    tri_code: str = 'DAL'
    team_id: str = '1610612742'
    nick_name: str = 'Mavericks'
    url_name: str = 'mavericks'


class Denver(Team):
    """Represent `Denver Nuggets` nba team."""

    full_name: str = 'Denver Nuggets'
    tri_code: str = 'DEN'
    team_id: str = '1610612743'
    nick_name: str = 'Nuggets'
    url_name: str = 'nuggets'


class Detroit(Team):
    """Represent `Detroit Pistons` nba team."""

    full_name: str = 'Detroit Pistons'
    tri_code: str = 'DET'
    team_id: str = '1610612765'
    nick_name: str = 'Pistons'
    url_name: str = 'pistons'


class GoldenState(Team):
    """Represent `Golden State` nba team."""

    full_name: str = 'Golden State'
    tri_code: str = 'GSW'
    team_id: str = '1610612744'
    nick_name: str = 'Warriors'
    url_name: str = 'warriors'


class Houston(Team):
    """Represent `Houston Rockets` nba team."""

    full_name: str = 'Houston Rockets'
    tri_code: str = 'HOU'
    team_id: str = '1610612745'
    nick_name: str = 'Rockets'
    url_name: str = 'rockets'


class Indiana(Team):
    """Represent `Indiana Pacers` nba team."""

    full_name: str = 'Indiana Pacers'
    tri_code: str = 'IND'
    team_id: str = '1610612754'
    nick_name: str = 'Pacers'
    url_name: str = 'pacers'


class Clippers(Team):
    """Represent `LA Clippers` nba team."""

    full_name: str = 'LA Clippers'
    tri_code: str = 'LAC'
    team_id: str = '1610612746'
    nick_name: str = 'Clippers'
    url_name: str = 'clippers'


class Lakers(Team):
    """Represent `Los Angeles Lakers` nba team."""

    full_name: str = 'Los Angeles Lakers'
    tri_code: str = 'LAL'
    team_id: str = '1610612747'
    nick_name: str = 'Lakers'
    url_name: str = 'lakers'


class Memphis(Team):
    """Represent `Memphis Grizzlies` nba team."""

    full_name: str = 'Memphis Grizzlies'
    tri_code: str = 'MEM'
    team_id: str = '1610612763'
    nick_name: str = 'Grizzlies'
    url_name: str = 'grizzlies'


class Miami(Team):
    """Represent `Miami Heat` nba team."""

    full_name: str = 'Memphis Grizzlies'
    tri_code: str = 'MIA'
    team_id: str = '1610612748'
    nick_name: str = 'Heat'
    url_name: str = 'heat'


class Milwaukee(Team):
    """Represent `Milwaukee Bucks` nba team."""

    full_name: str = 'Milwaukee Bucks'
    tri_code: str = 'MIL'
    team_id: str = '1610612749'
    nick_name: str = 'Bucks'
    url_name: str = 'bucks'


class Minnesota(Team):
    """Represent `Minnesota Timberwolves` nba team."""

    full_name: str = 'Minnesota Timberwolves'
    tri_code: str = 'MIN'
    team_id: str = '1610612750'
    nick_name: str = 'Timberwolves'
    url_name: str = 'timberwolves'


class NewOrleans(Team):
    """Represent `New Orleans Pelicans` nba team."""

    full_name: str = 'New Orleans Pelicans'
    tri_code: str = 'NOP'
    team_id: str = '1610612740'
    nick_name: str = 'Pelicans'
    url_name: str = 'pelicans'


class NewYork(Team):
    """Represent `New York Knicks` nba team."""

    full_name: str = 'New York Knicks'
    tri_code: str = 'NYK'
    team_id: str = '1610612752'
    nick_name: str = 'Knicks'
    url_name: str = 'knicks'


class OklahomaCity(Team):
    """Represent `Oklahoma City` nba team."""

    full_name: str = 'Oklahoma City Thunder'
    tri_code: str = 'OKC'
    team_id: str = '1610612760'
    nick_name: str = 'Thunder'
    url_name: str = 'thunder'


class Orlando(Team):
    """Represent `Orlando Magic` nba team."""

    full_name: str = 'Orlando Magic'
    tri_code: str = 'ORL'
    team_id: str = '1610612753'
    nick_name: str = 'Magic'
    url_name: str = 'magic'


class Philadelphia(Team):
    """Represent `Philadelphia 76ers` nba team."""

    full_name: str = 'Philadelphia 76ers'
    tri_code: str = 'PHI'
    team_id: str = '1610612755'
    nick_name: str = '76ers'
    url_name: str = 'sixers'


class Phoenix(Team):
    """Represent `Phoenix Suns` nba team."""

    full_name: str = 'Phoenix Suns'
    tri_code: str = 'PHX'
    team_id: str = '1610612756'
    nick_name: str = 'Suns'
    url_name: str = 'suns'


class Portland(Team):
    """Represent `Portland Trail Blazers` nba team."""

    full_name: str = 'Portland Trail Blazers'
    tri_code: str = 'POR'
    team_id: str = '1610612757'
    nick_name: str = 'Trail Blazers'
    url_name: str = 'blazers'


class Sacramento(Team):
    """Represent `Sacramento Kings` nba team."""

    full_name: str = 'Sacramento Kings'
    tri_code: str = 'SAC'
    team_id: str = '1610612758'
    nick_name: str = 'Kings'
    url_name: str = 'kings'


class SanAntonio(Team):
    """Represent `San Antonio Spurs` nba team."""

    full_name: str = 'San Antonio Spurs'
    tri_code: str = 'SAS'
    team_id: str = '1610612759'
    nick_name: str = 'Spurs'
    url_name: str = 'spurs'


class Toronto(Team):
    """Represent `Toronto Raptors` nba team."""

    full_name: str = 'Toronto Raptors'
    tri_code: str = 'TOR'
    team_id: str = '1610612761'
    nick_name: str = 'Raptors'
    url_name: str = 'raptors'


class Utah(Team):
    """Represent `Utah Jazz` nba team."""

    full_name: str = 'Utah Jazz'
    tri_code: str = 'UTA'
    team_id: str = '1610612762'
    nick_name: str = 'Jazz'
    url_name: str = 'jazz'


class Washington(Team):
    """Represent `Washington Wizards` nba team."""

    full_name: str = 'Washington Wizards'
    tri_code: str = 'WAS'
    team_id: str = '1610612764'
    nick_name: str = 'Wizards'
    url_name: str = 'wizards'


class NbaTeams(Teams):
    """Concrete interface for nba teams."""

    def __init__(self) -> None:

        @lru_cache()
        def teams() -> Iterator[Team]:
            yield from (
                Atlanta, Boston, Brooklyn, Charlotte, Chicago, Cleveland, Dallas, Denver, Detroit,
                GoldenState, Houston, Indiana, Clippers, Lakers, Memphis, Milwaukee, Minnesota,
                NewOrleans, NewYork, OklahomaCity, Orlando, Philadelphia, Phoenix, Portland,
                Sacramento, SanAntonio, Toronto, Utah, Washington
            )

        self._teams = teams

    def __next__(self) -> Team:
        return next(self._teams())

    def __iter__(self) -> Iterator[Team]:
        return self

from copy import deepcopy
from database.models import Team, Player
import cache as cache

new_teams: dict[str, Team] = { }
updated_players: dict[str, Player] = { }
new_players: dict[str, Player] = { }

def cache_players(players: dict[str, Player]) -> None:
    cache.players = deepcopy(players)

def cache_teams(teams: dict[str, Team]) -> None:
    cache.teams = deepcopy(teams)

def cache_data(teams: dict[str, Team], players: dict[str, Player]) -> None:
    cache_players(players)
    cache_teams(teams)

def check_diff_players(pls1: dict[str, Player], pls2: dict[str, Player]) -> None:
    for k in pls2:
        pl = pls1.get(k, None)
        if pl == None:
            new_players[pls2[k]["nickname"]] = pls2[k]
            continue
        if pls1[k] != pls2[k]:
            updated_players[pls2[k]["nickname"]] = pls2[k]

def check_deff_teams(tms1: dict[str, Team], tms2: dict[str, Team]) -> None:
    for k in tms2:
        tm = tms1.get(k, None)
        if tm == None:
            new_teams[tms2[k].name] = tms2[k]


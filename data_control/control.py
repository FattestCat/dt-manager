from copy import deepcopy
from database.models import Team, Player
import cache as cache

new_teams: dict[str, Team] = { }
updated_players: dict[str, Player] = { }
new_players: dict[str, Player] = { }
found_player_count: int = 0

def cache_players(players: dict[str, Player]) -> None:
    cache.players = deepcopy(players)

def cache_teams(teams: dict[str, Team]) -> None:
    cache.teams = deepcopy(teams)

def cache_data(teams: dict[str, Team], players: dict[str, Player]) -> None:
    cache_players(players)
    cache_teams(teams)

def get_cached_data():
    return {"players": cache.players, "teams": cache.teams}

def check_diff_players(old_pls: dict[str, Player], new_pls: dict[str, Player]) -> None:
    for k in new_pls:
        pl = old_pls.get(k, None)
        if pl == None:
            new_players[new_pls[k].nickname] = new_pls[k]
            continue
        # if pls1[k] != pls2[k]:
            # updated_players[pls2[k]["nickname"]] = pls2[k]
        if old_pls[k].is_team_changed(new_pls[k]):
            log_team_change(old_pls[k], new_pls[k])
            updated_players[new_pls[k].nickname] = new_pls[k]
        else:
            global found_player_count
            found_player_count += 1


def check_diff_teams(tms1: dict[str, Team], tms2: dict[str, Team]) -> None:
    for k in tms2:
        tm = tms1.get(k, None)
        if tm == None:
            new_teams[tms2[k].name] = tms2[k]

def no_changes() -> bool:
    if (len(new_teams) == 0 and
            len(updated_players) == 0 and
            len(new_players) == 0):
        print("No changes detected.")
        return True
    return False

def log_team_change(old_pl: Player, new_pl: Player) -> None:
    print(f"{old_pl.nickname}({old_pl.name}) has changed team: {old_pl.team} -> {new_pl.team}.")

def get_new_teams():
    return new_teams

def get_new_players():
    return new_players

def get_updated_players():
    return updated_players

def get_fount_players_count():
    return found_player_count

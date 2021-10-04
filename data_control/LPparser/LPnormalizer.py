
from .LPmodels import Team, Player

def normalize_players(pls: dict[str, Player]) -> dict[str, Player]:
    return {pls[k].name: pls[k] for k in pls if _is_valid_player(pls[k]) }

def normalize_teams(tms: dict[str, Team]) -> dict[str, Team]:
    return {tms[k].name: tms[k] for k in tms if _is_valid_team(tms[k]) }

def _is_valid_player(pl: Player) -> bool:
    if pl.name and pl.nickname and _is_valid_pos(pl.position):
        return True
    return False

def _is_valid_pos(n: str) -> bool:
    if n.isnumeric() and 0 < n.isnumeric() < 6:
        return True
    return False

def _is_valid_team(tm: Team) -> bool:
    if tm.name:
        return True
    return False

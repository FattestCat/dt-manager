import data_control.team_struct as ts
from data_control.converters import *

from sqlalchemy.orm import Session
from data_control.database.db_control import DBControl

from data_control.teams_parser.parse_from_liqui import LiquipediaParser
from data_control.team_pipeline import Normalizer
from data_control.cache import Cache
from data_control.database.models import Team, Player

from data_control.converters import *


team_with_players = tuple[Team, list[Player]]

ch = Cache()
staged_teams = [ ]
staged_players = [ ]

def get_parsed_data() -> dict[str, ts.Team]:
    parser = LiquipediaParser()
    parser.run()
    normalized = Normalizer(parser.teams)
    return normalized.teams

def get_data_from_db() -> list[team_with_players]:
    db_control = DBControl("teams.db")
    db_control.create_all()

    with Session(db_control.engine) as session:
        teams = db_control.get_all(session)
    return teams

def cache_data(c: Cache, teams: list[team_with_players]) -> None:
    c.cache({t[0].name: to_parsed_team_full(t) for t in teams})

def check_diff(cache: dict[str, ts.Team], data: dict[str, ts.Team]) -> bool:
    return all([cache[k].deep_eq(data[k]) for k in cache])

def check_team(t1: ts.Team, t2: ts.Team) -> bool:
    if t1.deep_eq(t2):
        return True

    return False


def push_to_db(teams: list[ts.Team]) -> None:
    pass

def pull_from_db() -> list[ts.Team]:
    return []



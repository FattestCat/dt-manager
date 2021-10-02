import data_control.team_struct as ts
from data_control.converters import *

from sqlalchemy.orm import Session
from data_control.database.db_control import DBControl

from data_control.teams_parser.parse_from_liqui import LiquipediaParser
from data_control.team_pipeline import Normalizer
from data_control.cache import Cache
from data_control.database.models import Team, Player

from data_control.converters import *

from pprint import pprint

team_with_players = tuple[Team, list[Player]]

ch = Cache()

def get_parsed_data() -> list[ts.Team]:
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
    c.cache([to_parsed_team_full(t) for t in teams])
    print('-' * 20)
    pprint([t for t in c.data])

def check_diff(cache: Cache, data: list[ts.Team]):
    ...

def push_to_db(teams: list[ts.Team]) -> None:
    pass

def pull_from_db() -> list[ts.Team]:
    return []



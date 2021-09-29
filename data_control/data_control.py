import data_control.team_struct as ts

from .teams_parser.parse_from_liqui import LiquipediaParser
from .team_pipeline import Normalizer
from .cache import Cache

def get_parsed_data() -> list[ts.Team]:
    parser = LiquipediaParser()
    parser.run()
    normalized = Normalizer(parser.teams)

    return normalized.teams

def cheack_diff(cache: Cache, data: list[ts.Team]):
    pass

def push_to_db(teams: list[ts.Team]) -> None:
    pass

def pull_from_db() -> list[ts.Team]:
    return []



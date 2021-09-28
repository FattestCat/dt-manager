from .teams_parser.parse_from_liqui import LiquipediaParser
from .team_pipeline import Normalizer
from .team_struct import Team, Player

def get_parsed_data() -> list[Team]:
    parser = LiquipediaParser()
    parser.run()
    normalized = Normalizer(parser.teams)

    return normalized.teams

def push_to_db(teams: list[Team]) -> None:
    pass



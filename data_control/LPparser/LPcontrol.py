from .LPadapter import *
from .LPmodels import Player, Team
from .LPparser import LiquipediaParser
from .LPnormalizer import normalize_teams, normalize_players

from typing import Union

import data_control.database.models as m

def get_parsed_data() -> dict[str, list[Union[m.Team, m.Player]]]:
    parser = LiquipediaParser()
    parser.run()
    parsed_teams = parser.teams
    parsed_players = parser.players
    n_teams = normalize_teams(parsed_teams)
    n_players = normalize_players(parsed_players)
    return {
            "teams": [to_db_team(n_teams[k]) for k in n_teams], 
            "players": [to_db_player(n_players[k]) for k in n_players]
           }

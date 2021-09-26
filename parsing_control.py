from time import sleep
import os
from typing import Callable

from teams_parser.parse_from_liqui import parse_teams_from_liqui, parse_players_from_liqui
from team import Team
from player import Player

DATABASE_FILE = "teams.db"
CONFIRMATION_WORDS = ["Y", "y", "yes", "Yes"]


def main():
    teams = get_teams_to_dict(parse_teams_from_liqui)
    for k in teams:
        players = get_player_to_dict(parse_players_from_liqui, teams[k])
        print(k, teams[k])
        print(players)
        sleep(0.5)

# next two functions created in case changing of parser functions
def get_teams_to_dict(parser: Callable[[], dict]) -> dict:
    return parser()

def get_player_to_dict(parser: Callable[[str], dict], team_url: str) -> dict:
    return parser(team_url)

def is_teams_db_file_exist(file: str = DATABASE_FILE):
    return os.path.isfile(file)

def create_teams_db_file(file: str = DATABASE_FILE):
    with open(file, 'w'):
        print(f"Created blank teams database file: {file}.")

def delete_teams_db_file(file: str = DATABASE_FILE):
    if not is_teams_db_file_exist(file):
        print(f"File {file} do not exist.")
        return
    if get_confirmation_from_terminal(file, "Delete file"):
        os.remove(file)
        print(f"File {file} deleted.")
    else:
        print("Aborted.")

def update_teams_db_file(file: str = DATABASE_FILE):
    if not is_teams_db_file_exist(file):
        print(f"File {file} do not exist.")
        return
    if get_confirmation_from_terminal(file, "Update file"):
        print(f"File {file} updated.")
    else:
        print("Aborted.")

# TODO:
def read_teams_db_file():
    pass

def get_confirmation_from_terminal(file: str, message: str = "WTF?!") -> bool:
    conf = input(message + f" {file}. y/N? ")
    if conf in CONFIRMATION_WORDS:
        return True
    return False

if __name__ == '__main__':
    main()

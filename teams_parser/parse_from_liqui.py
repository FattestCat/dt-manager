import requests
# from time import sleep
from bs4 import BeautifulSoup

# from ..team import Team
# from ..player import Player

BASE_URL = "https://liquipedia.net"
TEAMS_URL = "https://liquipedia.net/dota2/Portal:Teams"

def parse_teams_from_liqui() -> dict:
    r = requests.get(TEAMS_URL)
    soup = BeautifulSoup(r.text, "html.parser")
    teams = soup.find_all("span", {"class": "team-template-text"})
    teams_as_dict = {  }

    for team in teams[:5]:
        att = team.contents[0].attrs # type: ignore
        teams_as_dict[att["title"]] = BASE_URL + att["href"]

    return teams_as_dict

def parse_players_from_liqui(team_url: str):
    r = requests.get(team_url)
    soup = BeautifulSoup(r.text, "html.parser")
    players_table = soup.find("div", {"class": "roster table-responsive"})
    players = players_table.find_all("td", {"class": "Name"}) # type: ignore
    positions = players_table.find_all("td", {"class": "PositionWoTeam2"}) # type: ignore
    # print(team_url)
    players_as_dict = {  }
    for player, pos in zip(players, positions):
        players_as_dict[player.get_text().strip('()')] = pos.get_text() # type: ignore
        # print(f"Player: {player.get_text().strip('()')}, pos: {pos.get_text()}") # type: ignore
    # print()
    # TODO: must ruturn dict of players
    return players_as_dict


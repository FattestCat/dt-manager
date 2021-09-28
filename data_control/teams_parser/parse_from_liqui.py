import requests
from bs4 import BeautifulSoup
from typing import Optional
from pprint import pprint

from ..team_struct import Team, Player

class LiquipediaParser:

    BASE_URL: str = "https://liquipedia.net"
    TEAMS_URL: str = "https://liquipedia.net/dota2/Portal:Teams"
    teams: list[Team] = [ ]

    def run(self):
        self._parse_teams()
        self._update_teams()

    def collect(self):
        self.run()
        

    def _parse_teams(self) -> list[Team]:
        r = requests.get(self. TEAMS_URL)
        soup = BeautifulSoup(r.text, "html.parser")
        teams = soup.find_all("span", {"class": "team-template-text"})

        for team in teams[:5]:
            att = team.contents[0].attrs # type: ignore
            tm = Team(att["title"], self.BASE_URL + att["href"])
            self.teams.append(tm)
            pprint(f"Got team data from {tm.url}")

        return self.teams

    @staticmethod
    def _parse_players(team_url: str) -> list[Player]:
        r = requests.get(team_url)
        soup = BeautifulSoup(r.text, "html.parser")
        # table with players
        pt_soup = soup.find("div", {"class": "roster table-responsive"})
        p_name = pt_soup.find_all("td", class_ = "Name") # type: ignore
        p_pos = pt_soup.find_all("td", class_ = "PositionWoTeam2") # type: ignore
        p_nn_soup = pt_soup.find_all("span", id = "player") # type: ignore
        p_nn = [span.find("a") for span in p_nn_soup] # type: ignore
        players = [ ]

        for p, nn, pos in zip(p_name, p_nn, p_pos):
            players.append(Player(
                            p.text.strip("() []"), # type: ignore
                            nn.text.strip("() "), # type: ignore
                            pos.text.strip("() []")) # type: ignore
                           )
        print(f"Got players data {players}")
        return players

    def _update_teams(self) -> None:
        for tm in self.teams:
            tm.players = LiquipediaParser._parse_players(tm.url)

    def __repr__(self):
        return f"{self.TEAMS_URL}\n\n" + \
                "\n".join(str(t) for t in self.teams) + "\n"
                
    def __srt__(self):
        return self.__repr__()
            


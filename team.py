from dataclasses import dataclass
from random import randint
from player import Player

@dataclass
class Team:
    players: list[Player]
    team_id: int = 1
    name: str = "new team"
    coach: int = 0
    manager: int = 0
    bootcamp: int = 0
    jetlag: int = 0


    @staticmethod
    def gerenate_blank_team():
        return Team(players=[Player.generate_blank_player() for _ in range(5)],
                team_id=randint(1, 400))

    def __repr__(self):
        res = f"Team name: {self.name}.\n" + \
                f"Team id: {self.team_id}\n" + \
            "\n".join([str(p.name) for p in self.players]) + "\n"
        return res


from dataclasses import dataclass

@dataclass
class Player:
    name: str
    nickname: str
    position: str
    team_name: str = ""

    def __eq__(self, other):
        if (self.name == other.name
                and self.nickname == other.nickname):
            return True
        print(f'{self.name}, {self.nickname} != {other.name}, {other.nickname}')
        return False

@dataclass
class Team:
    name: str
    url: str

    def __eq__(self, other):
        if self.name == other.name:
            return True
        return False

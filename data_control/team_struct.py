from dataclasses import dataclass, field

@dataclass
class Player:
    name: str
    nickname: str
    position: str
    team_name: str = ""

    def __repr__(self):
        return f"{self.name} - {self.nickname}, {self.team_name} p:{self.position}"

    def __srt__(self):
        return self.__repr__()

    def __eq__(self, other):
        if (self.name == other.name
                and self.nickname == other.nickname):
            return True
        return False

@dataclass
class Team:
    name: str
    url: str
    players: list[Player] = field(default_factory=list)

    def __repr__(self):
        return f"{self.url}: {self.name}\nPlayers list:\n" + \
                "\n".join(str(p) for p in self.players if p)

    def __srt__(self):
        return self.__repr__()

    def __eq__(self, other):
        if self.name == other.name:
            return True
        return False

    def deep_eq(self, other):
        return self.__eq__(other) \
            and all([(pp == po) for pp in self.players for po in other.players])

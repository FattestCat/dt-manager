from dataclasses import dataclass, field

@dataclass
class Player:
    name: str
    nickname: str
    position: str

    def __repr__(self):
        return f"{self.name} - {self.nickname}: {self.position}"

    def __srt__(self):
        return self.__repr__()

@dataclass
class Team:
    name: str
    url: str
    players: list[Player] = field(default_factory=list)

    def __repr__(self):
        return f"{self.url}:\n{self.name} \nPlayers list:\n" + \
                "\n".join(str(p) for p in self.players if p) + "\n"

    def __srt__(self):
        return self.__repr__()

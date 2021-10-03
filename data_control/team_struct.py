from dataclasses import dataclass, field

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
    players: list[Player] = field(default_factory=list)

    def __eq__(self, other):
        if self.name == other.name:
            return True
        return False

    def deep_eq(self, other):
        return self.__eq__(other) \
            and all([(pp == po) for pp, po in zip(self.players, other.players)])

    # def diff(self, other) -> list[Player]:
        # if self.deep_eq(other):
            # return [ ]
        # diff_pl = [ ]
        # for s_player in self.players:
            # for o_player in other.players:
                # if s_player.name == o_player.name:
                    # continue
                # else:
                    # diff_pl.append(s_player)
        # return diff_pl

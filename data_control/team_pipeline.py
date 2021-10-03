from .team_struct import Team, Player

class Normalizer:

    def __init__(self, teams):
        self.teams: dict[str, Team] = teams
        self._normalize()

    def get_teams(self) -> dict[str, Team]:
        return self.teams

    def _normalize(self):
        for k in self.teams:
            self.teams[k].players = [p for p in self.teams[k].players if Normalizer._is_valid_player(p)]
                

    @staticmethod
    def _is_valid_player(pl: Player) -> bool:
        if pl.name and pl.nickname and Normalizer._is_valid_pos(pl.position):
            return True
        return False

    @staticmethod
    def _is_valid_pos(n: str) -> bool:
        if n.isnumeric() and 0 < n.isnumeric() < 6:
            return True
        return False

    def __repr__(self):
        return  "\n".join(str(self.teams[t]) for t in self.teams) + "\n"
                
    def __srt__(self):
        return self.__repr__()

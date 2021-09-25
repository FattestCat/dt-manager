from __future__ import annotations

from team import Team
from bracket import Bracket, OlimpicBracket

class Tournament:

    def __init__(self, teams: list[Team], bracket: Bracket):
        self.teams: list[Team] = teams
        self.bracket: Bracket = bracket

    @classmethod
    def generate_blank_tournament(cls):
        trn_teams = [Team.gerenate_blank_team() for _ in range(4)]
        brk = OlimpicBracket([t.team_id for t in trn_teams])
        return cls(trn_teams, brk)

    def __repr__(self):
        res = ""
        res += "\n".join(str(team) for team in self.teams)
        res += self.bracket.get_history()
        return res


def main():
    trn = Tournament.generate_blank_tournament()
    trn.bracket.generate_initial_team_pairs()
    while trn.bracket.get_winner() < 0:
        trn.bracket.play_round()
    # print(trn)




if __name__ == "__main__":
    main()

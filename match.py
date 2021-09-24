from random import randint

class Match:

    def __init__(self, team1: int, team2: int, winner: int = -1, looser: int = -1):
        self.team1 = team1
        self.team2 = team2
        self.winner = winner
        self.looser = looser

    # TODO: implement formula to det winner
    def play_match(self) -> int:
        if randint(1, 100000) % 2 == 0:
            self.winner, self.looser = self.team1, self.team2
        else:
            self.winner, self.looser = self.team2, self.team1

        return self.winner

    def is_played(self) -> bool:
        return not self.winner == -1

    def __repr__(self) -> str:
        return  "\n".join([
                 f"First team: {self.team1}",
                 f"Second team: {self.team2}",
                 f"Winner: {self.winner}",
                 f"Looser: {self.looser}\n"
                ])

    def __str__(self) -> str:
        return self.__repr__()

# to delete
def main():
    m = Match(1, 2)
    wn = m.play_match()
    print(wn)
    print(m)


if __name__ == "__main__":
    main()

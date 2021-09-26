from random import shuffle
from typing import Protocol

from match import Match

# Pair = tuple[int, int]

class Bracket(Protocol):
    def generate_initial_team_pairs(self) -> list[Match]: ...
    def play_round(self) -> None: ...
    def get_history(self) -> str: ...
    def get_next_round_matches(self) -> str: ...
    def get_winner(self) -> int: ...

class OlimpicBracket: # should we enh from Protocol

    def __init__(self, team_numbers: list[int]):
        if len(team_numbers) & (len(team_numbers) - 1) != 0 or len(team_numbers) < 1:
            # TODO: implement exceptions
            raise NotImplemented
        self.team_numbers: list[int] = team_numbers
        self.next_round_matches: list[Match] = [  ]
        self.history: list[list[Match]] = [  ]
        self.winner: int = -1
        self.rounds_player: int = 0

    def generate_initial_team_pairs(self) -> list[Match]:
        for team1, team2 in self._create_baskets():
            self.next_round_matches.append(Match(team1, team2))

        self._update_history()
        return self.next_round_matches

    def play_round(self) -> None:
        # TODO: dont forget to check if all played before u can call this method
        self.rounds_player += 1
        if len(self.next_round_matches) == 1:
            self.winner = self.next_round_matches[0].play_match()
            return

        pairs_of_winners: list[Match] = [  ]

        for i, _ in enumerate(self.next_round_matches):
            if i % 2 == 0:
                winner1 = self.next_round_matches[i].play_match()
                winner2 = self.next_round_matches[i + 1].play_match()
                pairs_of_winners.append(Match(winner1, winner2))

        self.next_round_matches = pairs_of_winners
        self._update_history()

    # TODO: to upgrade
    def get_history(self) -> str:
        res = ""
        for i, rnd in enumerate(self.history):
            res += f"Round: {i + 1} \n" + \
                " ".join(f"[L:{match.looser}, W:{match.winner}] " for match in rnd) + "\n"
        return res

    def get_winner(self):
        return self.winner


    def get_next_round_matches(self) -> str:
        return  f" --- Round number: {self.rounds_player + 1} \n" + \
                            "\n".join(str(x) for x in self.next_round_matches)

    def _update_history(self) -> None:
        self.history.append(self.next_round_matches[:])

    def _create_baskets(self) -> list[tuple[int, int]]:
        basket_1 = self.team_numbers[ :len(self.team_numbers)//2]
        basket_2 = self.team_numbers[len(self.team_numbers)//2: ]
        shuffle(basket_1)
        shuffle(basket_2)
        return list(zip(basket_1, basket_2))

# to delete
def main():
    ob = OlimpicBracket(list(range(8)))
    ob.generate_initial_team_pairs()
    # ob.play_round()
    # print(ob.get_history())
    while ob.winner < 0:
        ob.play_round()

    print(ob.get_history())


if __name__ == '__main__':
    main()


from player import Player
from team import Team

def main():
    pl1 = Player("xiao", 1, 1000, 1000, 1, 1, 1, 1, 1, 1)
    pl2 = Player.generate_blank_player()
    # print(pl1)
    # print(pl2)
    tm = Team.gerenate_blank_team()
    # print(tm)
    for k, v in vars(Player).items():
        if callable(v):
            print(f"{k=} :::: {v=}")
    # start()

def start():
    while True:
        command = input("Enter command: ")
        if command == "One":
            print("First command")
        elif command == "Two":
            print("Second command")
        elif command == "Three":
            print("Third command")
        elif command == "Exit":
            break
        else:
            print("Commands are: One, Two, Three, Exit")

if __name__ == '__main__':
    main()

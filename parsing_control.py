from time import sleep
from teams_parser.parser import parse_teams_from_liqui, parse_players_from_liqui


def main():
    teams = parse_teams_from_liqui()
    for k in teams:
        print(teams[k])
    for k in teams:
        parse_players_from_liqui(teams[k])
        sleep(0.5)

if __name__ == '__main__':
    main()

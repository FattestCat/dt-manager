import data_control.team_struct as ts
import data_control.database.models as m

def to_db_player(player: ts.Player) -> m.Player:
    return m.Player(name=player.name,
                    nickname=player.nickname,
                    position=player.position,
                    team=player.team_name)

def to_db_team(team: ts.Team) -> m.Team:
    return m.Team(name=team.name)

def to_parsed_player(player: m.Player) -> ts.Player:
    return ts.Player(name=player.name,
                     nickname=player.nickname,
                     position=player.position,
                     team_name=player.team)

def to_parsed_team(team: m.Team) -> ts.Team:
    return ts.Team(name=team.name, url="url not defined")

def to_parsed_team_full(team: tuple[m.Team, list[m.Player]]) -> ts.Team:
    p_team = to_parsed_team(team[0])
    p_team.players = [to_parsed_player(p) for p in team[1]]
    return p_team

import data_control.LPparser.LPmodels as lp
import data_control.database.models as m

def to_db_player(player: lp.Player) -> m.Player:
    return m.Player(name=player.name,
                    nickname=player.nickname,
                    position=player.position,
                    team=player.team_name)

def to_db_team(team: lp.Team) -> m.Team:
    return m.Team(name=team.name)

def to_lp_player(player: m.Player) -> lp.Player:
    return lp.Player(name=player.name,
                     nickname=player.nickname,
                     position=player.position,
                     team_name=player.team)

def to_lp_team(team: m.Team) -> lp.Team:
    return lp.Team(name=team.name, url="url not defined")

import data_control.team_struct as ts
import data_control.database.models as m

def to_db_player(pl: ts.Player) -> m.Player:
    return m.Player(name=pl.name,
                    nickname=pl.nickname,
                    position=pl.position)

def to_db_team(tm: ts.Team) -> m.Team:
    return m.Team(name=tm.name)

def to_parsed_player(pl: m.Player) -> ts.Player:
    return ts.Player(name=pl.name,
                     nickname=pl.nickname,
                     position=pl.position)

def to_parsed_team(tm: m.Team) -> ts.Team:
    return ts.Team(name=tm.name, url="")

def to_parsed_team_full(tm: m.Team) -> tuple[ts.Team, list[ts.Player]]:
    return (to_parsed_team(tm),
            [to_parsed_player(p) for p in tm.players])

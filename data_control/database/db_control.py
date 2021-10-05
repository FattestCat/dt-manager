import pathlib
import shutil
from typing import Union
from sqlalchemy import select, create_engine
from sqlalchemy.orm import Session

# import data_control.database.models as m
from .models import Player, Team, Base

class DBControl:
    cnt: list[int] = [0, ]
    
    def __init__(self, db: str):
        if DBControl.is_db(db):
            self.db = db
        else:
            self.db = DBControl.autogenerate_name(self.cnt[0])
            # create no more than 10 files
            self.cnt[0] = 0 if self.cnt[0] > 10 else self.cnt[0] + 1

        self._path = pathlib.Path(self.db)
        self._backup_path = pathlib.Path(self.db + ".bak")
        self.engine = create_engine(f"sqlite:///{self.db}", echo=True, future=True)

    def create_db(self) -> None:
        if not self._path.is_file():
            self._path.touch()

    def _backup(self) -> None:
        if self._path.is_file():
            shutil.copy(self._path, self._backup_path)

    def create_all(self) -> None:
        Base.metadata.create_all(self.engine)

    def add_team(self, session: Session, team: Team) -> None:
        if not self.get_team(session, team.name):
            session.add(team)

    def add_teams(self, session: Session, teams: dict[str, Team]) -> None:
        for v in teams.values():
            if not self.get_team(session, v.name):
                session.add(v)

    def add_player(self, session, player: Player) -> None:
        if not self.get_player(session, player.nickname):
            session.add(player)

    def add_players(self, session, players: dict[str, Player]) -> None:
        for v in players.values():
            self.add_player(session, v)

    def get_team(self, session: Session, name: str) -> Team:
        return session.query(Team).filter_by(name=name).first()

    def get_player(self, session: Session, nickname: str) -> Player:
        return session.query(Player).filter_by(nickname = nickname).first()

    def get_players_of_one_team(self, session: Session, team: str) -> dict[str, Player]:
        return {p.nickname: p for p in session.query(Player).filter_by(team=team).all()}

    def get_all(self, session: Session) -> dict[str, dict[str, Union[Team, Player]]]:
        return {
            "teams": {t.name: t for t in session.query(Team).all()},
            "players": {p.nickname: p for p in session.query(Player).all()}
        }

    def update_player(self, session: Session, player: Player) -> None:
        pl = self.get_player(session, player.nickname)
        pl.name = player.name
        pl.nickname = player.nickname
        pl.team = player.team
        session.add(pl)

    def update_players(self, session: Session, players: dict[str, Player]) -> None:
        for v in players.values():
            self.update_player(session, v)

    @staticmethod
    def log_player(old_pl: Player, new_pl: Player) -> None:
        print(f'{old_pl.nickname}({old_pl.name}) has changed team: {old_pl.team} -> {new_pl.team}.')

    @staticmethod
    def autogenerate_name(n) -> str:
        return f"autogenerated_{n}.db"

    @staticmethod
    def is_db(db: str) -> bool:
        if db[-3:] == ".db":
            return True
        return False

    def is_created(self) -> bool:
        if self._path.is_file():
            return True
        return False


from sqlalchemy import create_engine, Column, String, Integer, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Player(Base):
    __tablename__ = "players"

    id = Column(Integer, primary_key=True)
    name = Column(String(40))
    nickname = Column(String(40))
    team = Column(Integer, ForeignKey("teams.name"))
    position = Column(Integer, default=0)
    price = Column(Integer, default=0)
    salary = Column(Integer, default=0)
    laning = Column(Integer, default=0)
    agression = Column(Integer, default=0)
    map_awareness = Column(Integer, default=0)
    reaction_time = Column(Integer, default=0)
    farm_speed = Column(Integer, default=0)
    hero_pool = Column(Integer, default=0)

    player_team = relationship("Team", back_populates="players")
    

    def __repr__(self):
        return f"Player({self.id=}, {self.name=}, {self.nickname=}, {self.team=})"

class Team(Base):
    __tablename__ = "teams"

    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    coach = Column(Integer, default=0)
    manager = Column(Integer, default=0)
    bootcamp = Column(Integer, default=0)
    jetlag = Column(Integer, default=0)

    players = relationship("Player", back_populates="player_team")

    def __repr__(self):
        return f"Team({self.id=}, {self.name=})"

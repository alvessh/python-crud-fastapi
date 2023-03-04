from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

Base  = declarative_base()

class Game(Base):
    __tablename__ = 'game'
    id  = Column(Integer, primary_key=True, index=True)
    competition = Column(String)
    date = Column(DateTime(timezone=True))
    home_team_id = Column(Integer, ForeignKey('team.id'))
    away_team_id = Column(Integer, ForeignKey('team.id'))
    winner_team_id = Column(Integer, ForeignKey('team.id'))
    time_created = Column(DateTime(timezone=True), server_default=func.now())
    time_updated = Column(DateTime(timezone=True), onupdate=func.now())

    home_team = relationship('Team', foreign_keys=[home_team_id])
    away_team = relationship('Team', foreign_keys=[away_team_id])
    winner_team = relationship('Team', foreign_keys=[winner_team_id])


class Team(Base):
    __tablename__ = 'team'
    id  = Column(Integer, primary_key=True)
    description = Column(String)
    level = Column(String)
    sport = Column(String)
    country = Column(String)
    time_created = Column(DateTime(timezone=True), server_default=func.now())
    time_updated = Column(DateTime(timezone=True), onupdate=func.now())
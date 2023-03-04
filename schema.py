from pydantic import BaseModel
from datetime import datetime

class Game(BaseModel):
    competition: str
    date: datetime
    home_team_id: int
    away_team_id: int
    winner_team_id: int

    class Config:
        orm_mode = True

class Team(BaseModel):
    description:str
    level:str
    sport:str
    country:str

    class Config:
        orm_mode = True
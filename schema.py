from pydantic import BaseModel

class Game(BaseModel):
    competition: str
    gameDate: str
    home_team_id: int
    away_team_id: int
    winner_team_id: int = None
    addres: str

    class Config:
        orm_mode = True

class Team(BaseModel):
    description:str
    level:str
    sport:str
    country:str

    class Config:
        orm_mode = True
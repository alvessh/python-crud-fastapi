import uvicorn
from fastapi import FastAPI
from fastapi_sqlalchemy import DBSessionMiddleware, db

from schema import Game as SchemaGame
from schema import Team as SchemaTeam

from schema import Game
from schema import Team

from models import Game as ModelGame
from models import Team as ModelTeam

import os
from dotenv import load_dotenv

load_dotenv('.env')


app = FastAPI()

app.add_middleware(DBSessionMiddleware, db_url=os.environ['DATABASE_URL'])

@app.get("/")
async def root():
    return {"message": "hello world"}


@app.post('/game/', response_model=SchemaGame)
async def game(game: SchemaGame):
    db_game = ModelGame(competition=game.competition, date=game.date, home_team_id=game.home_team_id, away_team_id=game.away_team_id, winner_team_id=game.winner_team_id)
    db.session.add(db_game)
    db.session.commit()
    return db_game

@app.get('/game/')
async def game():
    db_game = db.session.query(ModelGame).all()
    return db_game

@app.get('/game/{id}')
async def game(id: int):
    db_game = db.session.query(ModelGame).filter_by(id=id).all()
    return db_game

@app.post('/team/', response_model=SchemaTeam)
async def team(team:SchemaTeam):
    db_team = ModelTeam(description=team.description, level=team.level, sport=team.sport, country=team.country)
    db.session.add(db_team)
    db.session.commit()
    return db_team

@app.get('/team/')
async def team():
    db_team = db.session.query(ModelTeam).all()
    return db_team

@app.get('/team/{id}')
async def team(id: int):
    db_team = db.session.query(ModelTeam).filter_by(id=id).all()
    return db_team


# To run locally
if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
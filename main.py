import uvicorn
from fastapi import FastAPI, HTTPException
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

# INICIO DOS ENDPOINT PARA TRABALHAR COM O GAME
@app.post('/game/', response_model=SchemaGame)
async def game(game: SchemaGame):
    db_game = ModelGame(competition=game.competition, gameDate=game.gameDate, home_team_id=game.home_team_id, away_team_id=game.away_team_id, winner_team_id=game.winner_team_id, addres=game.addres)
    db.session.add(db_game)
    db.session.commit()
    return db_game

@app.put('/game/{id}', response_model=SchemaGame)
async def game(id: int, game: SchemaGame):
    db_game = db.session.query(ModelGame).filter_by(id=id).first()

    if db_game is None:
        raise HTTPException(status_code=404, detail="Game not found")

    db_game.competition = game.competition
    db_game.gameDate = game.gameDate
    db_game.home_team_id = game.home_team_id
    db_game.away_team_id = game.away_team_id
    db_game.winner_team_id = game.winner_team_id
    db_game.addres = game.addres

    db.session.commit()
    db.session.refresh(db_game)

    return db_game

@app.get('/game/')
async def game():
    db_game = db.session.query(ModelGame).all()
    return db_game

@app.get('/game/{id}')
async def game(id: int):
    db_game = db.session.query(ModelGame).filter_by(id=id).first()
    return db_game

@app.delete('/game/{id}')
async def game(id: int):
    db_game = db.session.query(ModelGame).filter_by(id=id).first()

    if db_game is None:
        raise HTTPException(status_code=404, detail="Game not found")

    db.session.delete(db_game)
    db.session.commit()

    return {"message": "Game canceled successfully."}

# END DOS ENDPOINT PARA TRABALHAR COM O GAME

# INICIO DOS ENDPOINT PARA TRABALHAR COM O TEAM
@app.post('/team/', response_model=SchemaTeam)
async def team(team:SchemaTeam):
    db_team = ModelTeam(description=team.description, level=team.level, sport=team.sport, country=team.country)
    db.session.add(db_team)
    db.session.commit()
    return db_team

@app.put('/team/{id}', response_model=SchemaTeam)
async def team(id: int, team:SchemaTeam):
    db_team = db.session.query(ModelTeam).filter_by(id=id).first()

    if db_team is None:
        raise HTTPException(status_code=404, detail="Team not found")

    db_team.description = team.description
    db_team.level = team.level
    db_team.sport = team.sport
    db_team.country = team.country

    db.session.commit()
    db.session.refresh(db_team)
    
    return db_team

@app.get('/team/')
async def team():
    db_team = db.session.query(ModelTeam).all()
    return db_team

@app.get('/team/{id}')
async def team(id: int):
    db_team = db.session.query(ModelTeam).filter_by(id=id).first()
    return db_team

@app.delete('/team/{id}')
async def team(id: int):
    db_team = db.session.query(ModelTeam).filter_by(id=id).first()

    if db_team is None:
        raise HTTPException(status_code=404, detail="Team not found")

    db.session.delete(db_team)
    db.session.commit()

    return {"message": "Game canceled successfully."}

# END DOS ENDPOINT PARA TRABALHAR COM O TEAM

# To run locally
if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
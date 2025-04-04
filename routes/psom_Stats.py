from fastapi import APIRouter, Depends
from psom_db import get_db

router = APIRouter()


@router.get("/")
def get_player_stats(db=Depends(get_db)):
    cursor = db.cursor()
    cursor.execute("SELECT * FROM player_stats")
    players = cursor.fetchall()
    return [dict(player) for player in players]
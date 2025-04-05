from fastapi import APIRouter, Depends
from psom_db import get_db, sv_2_db

router = APIRouter()


@router.get("/")
def get_player_stats(db=Depends(get_db)):
    cursor = db.cursor()
    cursor.execute("SELECT * FROM player_stats")
    players = cursor.fetchall()

    if not players:
        return {"message": "No player stats found"}
    
    return [dict(player) for player in players]





@router.post("/scraper")
def scraper(url: str, player_name: str):
    
    psom_db = scraper(url, player_name)

    if not psom_db:
        return {"error": "Failed to scrape data"}
    
    return sv_2_db(psom_db)
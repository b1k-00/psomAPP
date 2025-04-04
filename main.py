# Import functions from other modules
from fastapi import FastAPI
from routes.psom_Stats import router as psom_router

app = FastAPI()

app.include_router(psom_router)


@app.get("/")
def home():
    return {"message": "Welcome to the PSOM Stats API!"}
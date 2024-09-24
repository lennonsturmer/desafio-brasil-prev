import uvicorn
from fastapi import FastAPI

from app.controller import game

app = FastAPI()

app.include_router(game.router)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)

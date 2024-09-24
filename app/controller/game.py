import random

from fastapi import APIRouter, Depends

from app.model.board import Board
from app.model.player import Player
from app.service.game_service import GameService


router = APIRouter(prefix="/jogo", tags=["jogo"])


def get_service():
    board = Board()
    players = [
        Player('impulsivo'),
        Player('exigente'),
        Player('cauteloso'),
        Player('aleatorio')
    ]
    random.shuffle(players)
    return GameService(board, players)


@router.get("/simular")
def simulate_game(service: GameService = Depends(get_service)):
    result = service.play_game()
    return result

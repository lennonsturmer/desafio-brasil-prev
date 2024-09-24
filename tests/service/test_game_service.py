import random
from unittest.mock import MagicMock

import pytest

from app.model.board import Board
from app.model.player import Player
from app.service.game_service import GameService


class TestGameService:
    @pytest.fixture
    def game_service(self):
        board = MagicMock(spec=Board)
        players = [
            MagicMock(spec=Player, player_type='impulsivo', balance=300, position=0, estates=[], active=True),
            MagicMock(spec=Player, player_type='exigente', balance=300, position=0, estates=[], active=True),
            MagicMock(spec=Player, player_type='cauteloso', balance=300, position=0, estates=[], active=True),
            MagicMock(spec=Player, player_type='aleatorio', balance=300, position=0, estates=[], active=True)
        ]
        random.shuffle(players)
        game_service = GameService(board, players)
        return game_service

    def test_play_game(self, game_service):
        result = game_service.play_game()
        assert result

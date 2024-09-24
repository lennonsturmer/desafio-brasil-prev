from typing import List

from app.model.board import Board
from app.model.player import Player


class GameService:
    def __init__(self, board: Board, players: List[Player]):
        self.board = board
        self.players = players
        self.round = 0

    def play_game(self):
        while len([player for player in self.players if player.active]) > 1 and self.round < 1000:
            for player in self.players:
                if not player.active:
                    continue

                position = player.move(self.board)
                estate = self.board.estates[position]

                if estate.owner and estate.owner != player:
                    player.pay_rent(estate.rent_value)
                    estate.owner.receive_rent(estate.rent_value)
                elif not estate.owner and player.can_buy(estate):
                    if player.balance >= estate.sales_cost:
                        player.buy_estate(estate)
                        estate.owner = player
                        player.estates.append(estate)

                if player.balance < 0:
                    player.game_over()

            self.round += 1

        winner = max(self.players, key=lambda player: player.balance if player.active else -float('inf'))
        sorted_players = sorted(self.players, key=lambda player: player.balance, reverse=True)

        return {
            "vencedor": winner.player_type,
            "jogadores": [player.player_type for player in sorted_players]
        }

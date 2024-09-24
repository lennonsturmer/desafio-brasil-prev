from typing import List

from app.model.board import Board
from app.model.player import Player


class GameService:
    def __init__(self, board: Board, players: List[Player]):
        self.board = board
        self.players = players
        self.round = 0

    def play_game(self):
        while self.__is_game_running():
            self.__play_round()

        return self.__get_game_results()

    def __is_game_running(self):
        active_players = len([player for player in self.players if player.active])
        return active_players > 1 and self.round < 1000

    def __play_round(self):
        for player in self.players:
            if player.active:
                self.__handle_player_turn(player)

        self.round += 1

    def __handle_player_turn(self, player):
        position = player.move(self.board)
        estate = self.board.estates[position]
        self.__handle_estate_interaction(player, estate)
        if player.balance < 0:
            player.game_over()

    def __handle_estate_interaction(self, player, estate):
        if estate.owner and estate.owner != player:
            self.__handle_rent_payment(player, estate)
        elif not estate.owner and player.can_buy(estate):
            self.__handle_estate_purchase(player, estate)

    def __get_game_results(self):
        winner = max(self.players, key=lambda player: player.balance if player.active else -float('inf'))
        sorted_players = sorted(self.players, key=lambda player: (player.balance, -self.players.index(player)), reverse=True)
        return {
            "vencedor": winner.player_type,
            "jogadores": [player.player_type for player in sorted_players]
        }

    @staticmethod
    def __handle_rent_payment(player, estate):
        player.pay_rent(estate.rent_value)
        estate.owner.receive_rent(estate.rent_value)

    @staticmethod
    def __handle_estate_purchase(player, estate):
        if player.balance >= estate.sales_cost:
            player.buy_estate(estate)
            estate.owner = player
            player.estates.append(estate)

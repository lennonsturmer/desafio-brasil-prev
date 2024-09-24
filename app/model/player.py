import random


class Player:
    def __init__(self, player_type):
        self.player_type = player_type
        self.balance = 300
        self.position = 0
        self.estates = []
        self.active = True

    def complete_round(self):
        self.balance += 100

    def pay_rent(self, rent_value):
        self.balance -= rent_value

    def receive_rent(self, rent_value):
        self.balance += rent_value

    def game_over(self):
        self.active = False
        for estate in self.estates:
            estate.owner = None

        self.estates.clear()

    def can_buy(self, estate):
        if self.player_type == 'impulsivo':
            return True
        elif self.player_type == 'exigente':
            return estate.rent_value > 50
        elif self.player_type == 'cauteloso':
            return self.balance - estate.sales_cost >= 80
        elif self.player_type == 'aleatorio':
            return random.choice([True, False])

    def move(self, board):
        dice = random.randint(1, 6)
        new_position = (self.position + dice) % len(board.estates)
        if self.position > new_position:
            self.complete_round()

        self.position = new_position
        return self.position

    def buy_estate(self, estate):
        self.balance -= estate.sales_cost

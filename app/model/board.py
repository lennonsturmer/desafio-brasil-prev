import random

from app.model.estate import Estate


class Board:
    def __init__(self):
        self.estates = [Estate(random.randint(100, 400), random.randint(10, 100)) for _ in range(20)]

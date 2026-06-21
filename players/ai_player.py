import random
from players.player import Player

class AIPlayer(Player):

    def get_move(self, hands=None):
        return random.choice(
            ["rock", "paper", "scissors"]
        )
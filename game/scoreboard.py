class ScoreBoard:

    def __init__(self):
        self._ai_score = 0
        self._player_score = 0

    def update(self, ai_move, player_move):

        if (player_move == "rock" and ai_move == "scissors") or \
           (player_move == "paper" and ai_move == "rock") or \
           (player_move == "scissors" and ai_move == "paper"):
            self._player_score += 1

        elif (ai_move == "rock" and player_move == "scissors") or \
             (ai_move == "paper" and player_move == "rock") or \
             (ai_move == "scissors" and player_move == "paper"):
            self._ai_score += 1

    @property
    def ai_score(self):
        return self._ai_score

    @property
    def player_score(self):
        return self._player_score
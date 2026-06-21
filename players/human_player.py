from players.player import Player

class HumanPlayer(Player):

    def __init__(self, detector):
        self._detector = detector

    def get_move(self, hands=None):

        if not hands:
            return None

        hand = hands[0]
        fingers = self._detector.fingersUp(hand)

        if fingers == [0, 0, 0, 0, 0]:
            return "rock"

        elif fingers == [1, 1, 1, 1, 1]:
            return "paper"

        elif fingers == [0, 1, 1, 0, 0]:
            return "scissors"

        return None
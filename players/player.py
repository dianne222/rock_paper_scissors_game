from abc import ABC, abstractmethod


class Player(ABC):

    @abstractmethod
    def get_move(self, hands=None):
        pass
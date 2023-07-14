from abc import ABC, abstractmethod

class GameInterface(ABC):
    @abstractmethod
    def add_winner(self, position, name):
        pass

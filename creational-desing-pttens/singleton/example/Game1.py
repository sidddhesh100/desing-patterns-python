from GameInterface import GameInterface
from LeaderBoard import LeaderBoard

class Game1(GameInterface):
    def __init__(self):
        self.leader_board = LeaderBoard()


    def add_winner(self, position, name):
        self.leader_board.add_winner(position, name)


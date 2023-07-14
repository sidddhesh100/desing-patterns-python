from Game1 import Game1
from Game2 import Game2
from Game3 import Game3

game_1 = Game1()
game_1.add_winner(2, "Cosmo")
game_1.leader_board.print()

game_2 = Game2()
game_2.add_winner(3, "Sean")
game_2.leader_board.print()

game_3 = Game3()
game_3.add_winner(1, "Emmy")
game_3.leader_board.print()




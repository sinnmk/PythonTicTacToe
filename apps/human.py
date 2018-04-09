from user_interface import UserInterface
from player import Player

class Human(Player): 

    def __init__(self): 
        self.user_interface = UserInterface()
        self.stored_moves = [] 
        self.num_board = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    def make_move(self, board): 
        move = self.user_interface.input_move(board)
        return move

    def set_name(self): 
        name = self.user_interface.input_name()
        return name

    def set_turn(self): 
        turn = self.user_interface.input_turn_choice()
        return turn 


from computer_logic import ComputerLogic
from user_interface import UserInterface
from game_engine import GameEngine
from game_board import GameBoard
import numpy as np

class WinLogic(object): 

    def __init__(self): 
        self.computer_logic = ComputerLogic()
        self.user_interface = UserInterface()
        self.game_engine = GameEngine()
        self.game_board = GameBoard()
        self.board = self.game_engine.interpret_and_translate_move()

    def check_col_for_win(self): 
        game_board = self.game_board.create_new_board()
        gameboard.any(axis = 1)

    def check_row_for_win(self):
        game_board = self.game_board.create_new_board()
        game_board.any(axis = 2)

    def check_diag_for_win(self): 
        game_board = self.game_board.create_new_board()
        
    def is_win(self): 
        return False
        



        


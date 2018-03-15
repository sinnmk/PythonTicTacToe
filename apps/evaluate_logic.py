from computer_logic import ComputerLogic
from user_interface import UserInterface
from game_engine import GameEngine
from game_board import GameBoard
from move_translator import MoveTranslator
import numpy as np

class EvaluateLogic(object): 

    def __init__(self): 
        self.computer_logic = ComputerLogic()
        self.user_interface = UserInterface()
        self.game_engine = GameEngine()
        self.move_translator = MoveTranslator()
        self.game_board = GameBoard()
        self.board = self.move_translator.translate_comp_move()
        self.win_msg = ("You have won!")

    def is_win(self): 
        return True


    def check_col_for_win(self): 
        game_board = self.game_board.create_new_board()
        column = gameboard.all(axis = 1)
        if column == True: 
            print(self.win_msg)
            return self.is_win()

    def check_row_for_win(self):
        game_board = self.game_board.create_new_board()
        row = game_board.all(axis = 2)
        if row == True: 
            print(self.win_msg)
            return self.is_win()

        



        


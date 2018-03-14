from computer_logic import ComputerLogic
from user_interface import UserInterface
from game_engine import GameEngine
from game_board import GameBoard

class WinLogic(object): 

    def __init__(self): 
        self.computer_logic = ComputerLogic()
        self.user_interface = UserInterface()
        self.game_engine = GameEngine()
        self.game_board = GameBoard()
        self.board = self.game_engine.interpret_and_translate_move()
        self.win = False

    def winning_scenarios(self): 
        pass 

    def check_if_win(self): 
        return False
        



        


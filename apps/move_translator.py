from user_interface import UserInterface
from game_board import GameBoard
from computer_logic import ComputerLogic

class MoveTranslator(object):
    
    def __init__(self): 
        self.user_interface = UserInterface()
        self.computer_logic = ComputerLogic()

        self.game_board = GameBoard()
        self.board = self.game_board.create_new_board()

    def interpret_user_move(self): 
        move = self.user_interface.get_game_move()
        if move == 1 and self.board[0][0] == 0: 
            self.board[0][0] = 1 
        if move == 2 and self.board[0][1] == 0: 
            self.board[0][1] = 1
        if move == 3 and self.board[0][2] == 0: 
            self.board[0][2] = 1

        if move == 4 and self.board[1][0] == 0: 
            self.board[1][0] = 1 
        if move == 5 and self.board[1][1] == 0: 
            self.board[1][1] = 1
        if move == 6 and self.board[1][2] == 0: 
            self.board[2][2] = 1

        if move == 7 and self.board[2][0] == 0: 
            self.board[2][0] = 1 
        if move == 8 and self.board[2][1] == 0: 
            self.board[2][1] = 1
        if move == 9 and self.board[2][2] == 0: 
            self.board[2][2] = 1

        print(self.board)

    def interpret_comp_move(self): 
        move = self.computer_logic.get_comp_move()
        if move == 1 and self.board[0][0] == 0: 
            self.board[0][0] = 2 
        if move == 2 and self.board[0][1] == 0: 
            self.board[0][1] = 2
        if move == 3 and self.board[0][2] == 0: 
            self.board[0][2] = 2

        if move == 4 and self.board[1][0] == 0: 
            self.board[1][0] = 2 
        if move == 5 and self.board[1][1] == 0: 
            self.board[1][1] = 2
        if move == 6 and self.board[1][2] == 0: 
            self.board[2][2] = 2

        if move == 7 and self.board[2][0] == 0: 
            self.board[2][0] = 2 
        if move == 8 and self.board[2][1] == 0: 
            self.board[2][1] = 2
        if move == 9 and self.board[2][2] == 0: 
            self.board[2][2] = 2

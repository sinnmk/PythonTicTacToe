from user_interface import UserInterface 
import random

#_____BASE CLASS: PLAYER_____
class Player(object): 
    move = '' 
    index = '' 
    name = ''
    turn = '' 

    def __init__(self, move, index, name, turn): 
        self.move = move 
        self.index = index
        self.name = name 
        self.turn = turn
        self.num_board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.game_engine = GameEngine()

    def get_name(self): 
        return self.name

    def make_move(self, board):
        return self.move

    def set_turn(self): 
        return self.turn

    def find_index_of_move(self, board):
        move = self.make_move(board)
        move_index = 0
        for num in self.num_board: 
            if num == move:
                move_index = move - 1
        return move_index

    def display_players_name(self): 
        print (self.set_name() + "'s" + " turn...")

#_____DERIVED CLASS: HUMAN_____
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

#_____DERIVED CLASS: COMPUTER_____
class Computer(Player): 

    def __init__(self): 
        self.num_board = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    def make_move(self, board):
        i = 0
        open_positions = [] 
        while i < len(board): 
            for digit in board: 
                if board[i] == 0: 
                    open_positions.append(i + 1)
                if board[i] != 0: 
                    open_positions.append("")
                i += 1
        move = random.choice(self.num_board)
        if move in open_positions: 
            return move
        else: 
            return self.make_move(board)

    def set_name(self): 
        name = "Computer"
        return name

def move(Player): 
    Player.make_move(board)

def name(Player): 
    Player.set_name()

def display_name(Player): 
    Player.display_players_name()

def set_turn(Player): 
    Player.set_turn()

def find_index_of_move(Player):
    Player.find_index_of_move(board)




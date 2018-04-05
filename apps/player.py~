from user_interface import UserInterface
import random

#_____BASE CLASS: PLAYER_____
class Player(object): 
    move = '' 
    index = '' 
    name = ''
    turn = '' 

    def __init__(self, move, index, name, turn): 
        self.PLAYER_X = PLAYER_X
        self.PLAYER_O = PLAYER_O
        self.move = move 
        self.index = index
        self.name = name 
        self.turn = turn
        self.place_board = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.num_board = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    def get_name(self): 
        return self.name

    def make_move(self):
        return self.move

    def set_turn(self): 
        return self.turn

    def find_index_of_move(self):
        move = self.make_move()
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

    def make_move(self): 
        move = self.user_interface.input_move()
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

    def make_move(self):
        move = random.choice(self.num_board)
        return move

    def set_name(self): 
        name = "Computer"
        return name

def move(Player): 
    Player.make_move()

def name(Player): 
    Player.set_name()

def display_name(Player): 
    Player.display_players_name()

def set_turn(Player): 
    Player.set_turn()

def find_move_index(Player):
    Player.find_move_index()


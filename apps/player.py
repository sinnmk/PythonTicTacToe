from user_interface import UserInterface
import random

#_____BASE CLASS: PLAYER_____
class Player(object): 
    move = 0
    name = ''
    turn = 0
    index = 0

    def __init__(self, move, name, turn, index): 
        self.move = move 
        self.name = name 
        self.turn = turn
        self.index = index

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

    def display_players_name(self): 
        print("It is " + self.set_name() + "'s" + " turn.")

#_____DERIVED CLASS: COMPUTER_____
class Computer(Player): 

    def __init__(self): 
        self.num_board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.choices = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    def make_move(self): 
        move = random.choice(self.choices)
        return move 

    def display_players_name(self): 
        print("It is the computer's turn.")

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

def get_place_board(Player): 
    Player.get_place_board()















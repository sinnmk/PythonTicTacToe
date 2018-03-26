from user_interface import UserInterface
import functools 
from functools import reduce
import random

#Parent class
class Player(object): 
    move = 0
    name = ''
    
    def __init__(self, move, name): 
        self.move = move 
        self.name = name 

    def get_name(self): 
        return self.name

    def make_move(self):
        return self.move

#Child class
class Human(Player): 
    
    def __init__(self): 
        self.user_interface = UserInterface()
        self.stored_moves = [] 

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

#Child class
class Computer(Player): 

    def __init__(self): 
        self.stored_moves = []

    def make_move(self): 
        open_positions = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        move = random.choice(open_positions)
        return move 

    def display_players_name(self): 
        print("It is the computer's turn.")

def move(Player): 
    Player.make_move()

def name(Player): 
    Player.set_name()

def display_name(Player): 
    Player.display_players_name()
















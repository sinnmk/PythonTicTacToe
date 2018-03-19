from computer_logic import ComputerLogic
from user_interface import UserInterface
from game_board import GameBoard
import numpy as np

class GameEngine(object): 

    def __init__(self): 
        self.user_interface = UserInterface()
        self.computer_logic = ComputerLogic()
        self.game_board = GameBoard()
        self.turns = 0
        self.invalid_input_msg = ("You have given an invalid choice, please try again: ")
        self.player_one_turn_msg = ("It's player one's turn: ")
        self.player_two_turn_msg = ("The computer has finished it's turn.")
        self.name = self.user_interface.get_players_name()
        self.welcome_msg = ("Welcome to Tic Tac Toe, ")

    def welcome_prompt(self): 
        print(self.welcome_msg + self.name + "." )

    def turn_prompt(self): 
        print("It is " + self.name + " turn.")

    def play_game(self): 
        game_running = True
        while game_running == True: 
            self.game_board.place_x()
            self.game_board.check_for_win()
            self.game_board.place_o()
            self.game_board.check_for_win()

    def choose_menu_choice(self): 
        self.user_interface.display_menu()
        user_choice = self.user_interface.get_menu_choice()

        if (user_choice == 1): 
            return self.play_game()
        elif (user_choice == 2): 
            print(self.user_interface.display_rules())
            return self.choose_menu_choice()
        elif (user_choice == 3): 
            exit()
        else: 
            print(self.invalid_input_msg)
            return self.choose_menu_choice()

if __name__ == "__main__": 
    a = GameEngine()
    a.choose_menu_choice()

            
        

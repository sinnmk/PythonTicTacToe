from user_interface import UserInterface 
from game_board import GameBoard 
from game_play_options import GamePlayOptions 
import numpy as np

class GameEngine(object): 

    def __init__(self): 
        self.user_interface = UserInterface()
        self.game_play_options = GamePlayOptions()
        self.invalid_input_msg = ("You have given an invalid choice, please try again: ")
        self.menu_choice_msg = ("\nTIC TAC TOE MENU \n1. Player vs Computer \n2. Player vs Player \n3. Computer vs Computer \n4. Display Rules \n5. Quit")

    def menu_choice_one(self): 
        return self.game_play_options.player_vs_computer()

    def menu_choice_two(self): 
        return self.game_play_options.player_vs_player()

    def menu_choice_three(self): 
        return self.game_play_options.computer_vs_computer()

    def menu_choice_four(self): 
        return self.user_interface.display_rules()

    def menu_choice_five(self): 
        exit()

    def choose_menu_choice(self): 
        print(self.menu_choice_msg)
        menu_choices = [self.menu_choice_one, self.menu_choice_two, self.menu_choice_three, self.menu_choice_four, self.menu_choice_five]
        user_choice = int(input("Please choose a number choice (1-5)")) - 1 
        menu_choices[user_choice]()

if __name__ == "__main__": 
    a = GameEngine()
    a.choose_menu_choice()

            
        

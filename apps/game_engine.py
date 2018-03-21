from user_interface import UserInterface 
from game_board import GameBoard 
from game_play_options import GamePlayOptions 
import numpy as np

class GameEngine(object): 

    def __init__(self): 
        self.user_interface = UserInterface()
        self.game_play_options = GamePlayOptions()
        self.game_board = GameBoard()
        #move msgs all in one place
        self.invalid_input_msg = ("You have given an invalid choice, please try again: ")

    def return_choice(self): 
        choice = getattr(self, self.user_interface)
        return choice

    def choose_menu_choice(self): 
        self.user_interface.display_menu()
        user_choice = self.user_interface.get_menu_choice()

        if (user_choice == 1): 
            self.game_play_options.player_vs_computer()
        elif (user_choice == 2): 
            self.game_play_options.player_vs_player()
        elif (user_choice == 3): 
            self.game_play_options.computer_vs_computer()
        elif (user_choice == 4): 
            print(self.user_interface.display_rules())
            return self.choose_menu_choice()
        elif (user_choice == 5): 
            exit()
        else: 
            print(self.invalid_input_msg)
            return self.choose_menu_choice()

if __name__ == "__main__": 
    a = GameEngine()
    a.choose_menu_choice()

            
        

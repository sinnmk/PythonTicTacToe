from game_board import GameBoard
from user_interface import UserInterface
import time

class GamePlayOptions(object): 

    def __init__(self): 
        self.game_board = GameBoard()
        self.user_interface = UserInterface()
        self.turns = 0
        self.name = self.user_interface.input_name()

    def computer_vs_computer(self): 
        i = 0
        while i < 9: 
            self.player.place_x()
            self.game_board.check_for_win()
            i += 1

    def computer_vs_computer(self): 
        i = 0  
        while i < 9: 
            self.game_board.place_x()
            self.game_board.check_for_win()
            i += 1
            time.sleep(1)
            self.game_board.comp_place_o()
            self.game_board.check_for_win()
            time.sleep(1)
            i += 1

    def player_one_goes_first(self): 
        self.turn_prompt()
        self.turns += 1
        self.game_board.player_place_o()
        self.game_board.check_for_win()
        self.turns += 1
        self.game_board.place_x()
        self.game_board.check_for_win()

    def player_two_goes_first(self): 
        self.turns += 1
        self.game_board.comp_place_x()
        self.game_board.check_for_win()
        self.turn_prompt()
        self.turns += 1
        self.game_board.player_place_o()
        self.game_board.check_for_win()

    def turn_prompt(self): 
        print("It is " + self.name + "'s turn!")

    def turn_choice(self): 
        turn_choice = int(self.user_interface.input_turn_choice())
        print(turn_choice)
        return turn_choice

    def player_vs_computer(self): 
        turn_choice = self.turn_choice()
        while self.turns < 9: 
            if turn_choice == 1: 
                self.player_one_goes_first()
            elif turn_choice == 2: 
                self.player_two_goes_first()

    def player_vs_player(self): 
        while self.turns < 9: 
            self.turns += 1
            self.game_board.player_place_x()
            self.game_board.check_for_win()
            self.turns += 1
            self.game_board.player_place_o()
            self.game_board.check_for_win()
            

    


            

    


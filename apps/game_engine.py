from computer_logic import ComputerLogic
from user_interface import UserInterface

class GameEngine(object): 

    def __init__(self): 
        self.turns = 0
        self.max_turns = 9
        self.user_interface = UserInterface()
        self.computer_logic = ComputerLogic()
        self.player_one_moves = []
        self.player_two_moves = []
        self.invalid_input_msg = ("You have given an invalid choice, please try again: ")
        self.play = 1
        self.display_rules = 2
        self.quit = 3

    def get_player_turn_choice(self): 
        return self.user_interface.get_player_turn_choice()

    def store_player_one_moves(self): 
        game_move = self.user_interface.get_game_move()
        self.player_one_moves.append(game_move)
        return self.player_one_moves

    def store_player_two_moves(self): 
        game_move = self.computer_logic.get_comp_move()
        self.player_two_moves.append(game_move)
        return self.player_two_moves

    def play_game(self): 
        if self.get_player_turn_choice == 1: 
            while self.turns < self.max_turns: 
                self.user_interface.get_game_move()
                self.store_player_one_moves()
                self.turns += 1
                self.computer_logic.get_comp_move()
                self.store_player_two_moves()
                self.turns += 1
            return self.turns 
                
    def choose_menu_choice(self): 
        choice = self.user_interface.get_menu_choice()

        if (choice == self.play): 
            self.play_game()
        elif (choice == self.display_rules): 
            print(self.user_interface.display_rules())
        elif (choice == self.quit): 
            exit()
        else: 
            print(self.invalid_input_msg)
            self.choose_menu_choice()
            
        

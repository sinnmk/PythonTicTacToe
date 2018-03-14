from computer_logic import ComputerLogic
from user_interface import UserInterface
from game_board import GameBoard
from move_translator import MoveTranslator

class GameEngine(object): 

    def __init__(self): 
        self.turns = 0
        self.max_turns = 9
        self.user_interface = UserInterface()
        self.computer_logic = ComputerLogic()
        self.move_translator = MoveTranslator()
        self.player_one_moves = []
        self.player_two_moves = []
        self.invalid_input_msg = ("You have given an invalid choice, please try again: ")
        self.play = 1
        self.display_rules = 2
        self.quit = 3

    def get_player_turn_choice(self): 
        return self.user_interface.get_player_turn_choice()

    def store_player_one_moves(self): 
        p1_move = self.user_interface.get_game_move()
        self.player_one_moves.append(p1_move)
        return self.player_one_moves

    def store_player_two_moves(self): 
        p2_move = self.computer_logic.get_comp_move()
        self.player_two_moves.append(p2_move)
        return self.player_two_moves

    def there_are_turns_left(self): 
        return self.turns < self.max_turns

    def play_game(self): 
        self.game_board.create_new_board()
        while self.there_are_turns_left(): 
             self.move_translator.interpret_user_move()
             self.turns += 1
             self.check_if_win()
             self.move_translator.interpret_comp_move()
             self.turns += 1
             self.check_if_win()
                
    def choose_menu_choice(self): 
        self.user_interface.display_menu()
        user_choice = self.user_interface.get_menu_choice()
        if (user_choice == self.play): 
            return self.play_game()
        elif (user_choice == self.display_rules): 
            print(self.user_interface.display_rules())
            return self.choose_menu_choice()
        elif (user_choice == self.quit): 
            exit()
        else: 
            print(self.invalid_input_msg)
            return self.choose_menu_choice()

if __name__ == "__main__": 
    a = GameEngine()
    a.choose_menu_choice()

            
        

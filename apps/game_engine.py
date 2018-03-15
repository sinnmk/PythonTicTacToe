from computer_logic import ComputerLogic
from user_interface import UserInterface
from game_board import GameBoard
from move_translator import MoveTranslator

class GameEngine(object): 

    def __init__(self): 
        self.user_interface = UserInterface()
        self.computer_logic = ComputerLogic()
        self.move_translator = MoveTranslator()
        self.game_board = GameBoard()

        self.player_one_moves = []
        self.player_two_moves = []

        self.turns = 0
        self.invalid_input_msg = ("You have given an invalid choice, please try again: ")
        self.player_one_turn_msg = ("It's player one's turn: ")
        self.player_two_turn_msg = ("The computer has finished it's turn.")

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

    def player_one_turn(self): 
        print(self.player_one_turn_msg)
        self.turns += 1
        return self.move_translator.interpret_user_move()

    def player_two_turn(self): 
        print(self.player_two_turn_msg)
        self.turns += 1
        return self.move_translator.interpret_comp_move()

    def check_for_repeat_moves(self): 
        player_one_moves = self.store_player_one_moves()
        player_two_moves = self.store_player_two_moves()
        comp_move = self.computer_logic.get_comp_move()
        player_move = self.user_interface.get_game_move() 
        
        if comp_move in player_two_moves or comp_move in player_one_moves: 
            return True
        if player_move in player_one_moves or player_move in player_two_moves: 
            return True
        else: 
            return False

    def create_board(self): 
        return self.game_board.create_new_board()

    def get_player_turn_choice(self): 
        return self.user_interface.get_player_turn_choice()

    def play_game(self): 
        while self.turns < 9: 
            self.player_one_turn()
            self.player_two_turn()

    def choose_menu_choice(self): 
        self.user_interface.display_menu()
        user_choice = self.user_interface.get_menu_choice()

        if (user_choice == 1): 
            self.create_board()
            self.get_player_turn_choice()
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

            
        

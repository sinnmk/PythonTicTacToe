from computer_logic import ComputerLogic
from user_interface import UserInterface
from game_board import GameBoard

class GameEngine(object): 

    def __init__(self): 
        self.turns = 0
        self.max_turns = 9
        self.user_interface = UserInterface()
        self.computer_logic = ComputerLogic()
        self.game_board = GameBoard()
        self.board = self.game_board.create_new_board()
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

    def interpret_user_move(self): 
        move = self.user_interface.get_game_move()
        if move == 1 and self.board[0][0] == 0: 
            self.board[0][0] = 1 
        if move == 2 and self.board[0][1] == 0: 
            self.board[0][1] = 1
        if move == 3 and self.board[0][2] == 0: 
            self.board[0][2] = 1

        if move == 4 and self.board[1][0] == 0: 
            self.board[1][0] = 1 
        if move == 5 and self.board[1][1] == 0: 
            self.board[1][1] = 1
        if move == 6 and self.board[1][2] == 0: 
            self.board[2][2] = 1

        if move == 7 and self.board[2][0] == 0: 
            self.board[2][0] = 1 
        if move == 8 and self.board[2][1] == 0: 
            self.board[2][1] = 1
        if move == 9 and self.board[2][2] == 0: 
            self.board[2][2] = 1

        print(self.board)

    def interpret_comp_move(self): 
        move = self.computer_logic.get_comp_move()
        if move == 1 and self.board[0][0] == 0: 
            self.board[0][0] = 2 
        if move == 2 and self.board[0][1] == 0: 
            self.board[0][1] = 2
        if move == 3 and self.board[0][2] == 0: 
            self.board[0][2] = 2

        if move == 4 and self.board[1][0] == 0: 
            self.board[1][0] = 2 
        if move == 5 and self.board[1][1] == 0: 
            self.board[1][1] = 2
        if move == 6 and self.board[1][2] == 0: 
            self.board[2][2] = 2

        if move == 7 and self.board[2][0] == 0: 
            self.board[2][0] = 2 
        if move == 8 and self.board[2][1] == 0: 
            self.board[2][1] = 2
        if move == 9 and self.board[2][2] == 0: 
            self.board[2][2] = 2
    
    def there_are_turns_left(self): 
        return self.turns < self.max_turns

    def play_game(self): 
        self.game_board.create_new_board()
        while self.there_are_turns_left(): 
             self.interpret_user_move()
             self.interpret_comp_move()
             self.turns += 1
                
    def choose_menu_choice(self): 
        self.user_interface.display_menu()
        choice = self.user_interface.get_menu_choice()
        if (choice == self.play): 
            return self.play_game()
        elif (choice == self.display_rules): 
            print(self.user_interface.display_rules())
            self.choose_menu_choice()
        elif (choice == self.quit): 
            exit()
        else: 
            print(self.invalid_input_msg)
            self.choose_menu_choice()

if __name__ == "__main__": 
    a = GameEngine()
    a.choose_menu_choice()

            
        

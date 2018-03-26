from user_interface import UserInterface 
from player import Player
from player import Computer
from player import Human
import time

class GameEngine(object): 

    PLAYER_X = '' 
    PLAYER_O = ''

    def __init__(self): 
        self.user_interface = UserInterface()
        self.invalid_input_msg = ("You have given an invalid choice, please try again: ")
        self.menu_choice_msg = ("\nTIC TAC TOE MENU \n1. Player vs Computer \n2. Player vs Player \n3. Computer vs Computer \n4. Display Rules \n5. Quit")
        self.welcome_pvc_msg = ("Welcome to Player vs Computer Tic Tac Toe!")
        self.computer_player = Computer()
        self.human_player = Human()
        self.user_interface = UserInterface()

        self.invalid_entry_msg = ("This is not a valid entry")
        self.not_open_msg = ("This position is already taken, please choose another.")
        self.new_board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.place_board = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.turns = 0

    def display_players_name(self): 
        print("It is " + self.human_player.set_name() + " turn")

    def find_index_of_move(self, move): 
        move_index = 0 
        for num in self.new_board: 
            if num == move: 
                move_index = move - 1
        return move_index

    def display_board(self): 
        self.game_board_list = []

        for i in range(0, 9): 
            if self.place_board[i] == 1: 
                self.game_board_list.append('X')
            elif self.place_board[i] == 2: 
                self.game_board_list.append('O')
            elif self.place_board[i] == 0: 
                self.game_board_list.append(' ')

        print("""
         {} | {} | {}
        ---+---+---
         {} | {} | {}
        ---+---+---
         {} | {} | {}
        """.format(*self.game_board_list))
        return self.place_board

    #EVALUATE WIN
    def check_for_win(self): 
        win_combos = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))

        for i in win_combos:
            if self.place_board[i][0] == self.board[i][1] == self.board[i][2] == "O": 
                print("wins!\n")
            if self.board[i][0] == self.board[i][1] == self.board[i][2] == "X": 
                print("wins!\n")

    def is_position_open(self, index): 
        for digit in self.place_board: 
            if self.place_board[index] == 0: 
                return True
            elif self.place_board[index] != 0: 
                return False

    #PLACE MOVE
    def place_x(self, index): 
        if self.is_position_open(index) == True: 
            self.place_board[index] = 1
        else: 
            print("This is not an open position. Please re-enter a move that is in an open position")
            return False 
    def place_o(self, index): 
        if self.is_position_open(index) == True: 
            self.place_board[index] = 2
        else: 
            print("This is not an open position. Please re-enter a move that is in an open position")
            return False 

    #GAME CHOICES
    def player_vs_computer(self): 
        self.user_interface.print_example_board()
        while self.turns < 9 : 
            move = self.human_player.make_move()
            index = self.find_index_of_move(move)
            self.place_x(index)
            self.turns += 1
            self.display_board()
            move = self.computer_player.make_move()
            index = self.find_index_of_move(move)
            self.place_o(index)
            self.turns += 1
            self.display_board()

    def player_vs_player(self): 
        self.user_interface.print_example_board()
        while self.turns < 9: 
            move = self.human_player.make_move()
            index = self.find_index_of_move(move)
            self.place_x(index)
            self.display_board()
            self.turns += 1
            move = self.human_player.make_move()
            index = self.find_index_of_move(move)
            self.place_o(index)
            self.display_board()
            self.turns += 1

    def computer_vs_computer(self): 
        self.user_interface.print_example_board()
        while self.turns < 9: 
            move = self.computer_player.make_move()
            index = self.find_index_of_move(move)
            self.place_x(index)
            self.display_board()
            self.turns += 1
            time.sleep(1)
            move = self.computer_player.make_move()
            index = self.find_index_of_move(move)
            self.place_o(index)
            self.display_board()
            self.turns += 1
            time.sleep(1)

    def display_rules(self): 
        self.user_interface.display_rules()
        return self.choose_menu_choice()

    def exit_game(self): 
        exit()

    def choose_menu_choice(self): 
        print(self.menu_choice_msg)
        menu_choices = [self.player_vs_computer, self.player_vs_player, self.computer_vs_computer, self.display_rules, self.exit_game]

        user_choice = int(input("Please choose a number choice (1-5): ")) - 1 

        menu_choices[user_choice]()

if __name__ == "__main__": 
    a = GameEngine()
    a.choose_menu_choice()
    

            
        

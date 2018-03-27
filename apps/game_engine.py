from user_interface import UserInterface 
from player import Player
from player import Computer
from player import Human
import numpy as np
import time

class GameEngine(object): 

    def __init__(self): 
        self.user_interface = UserInterface()
        self.computer_player = Computer()
        self.human_player = Human()
        self.invalid_input_msg = ("You have given an invalid choice, please try again: ")
        self.menu_choice_msg = ("\nTIC TAC TOE MENU \n1. Player vs Computer \n2. Player vs Player \n3. Computer vs Computer \n4. Display Rules \n5. Quit")
        self.welcome_pvc_msg = ("Welcome to Player vs Computer Tic Tac Toe!")
        self.invalid_entry_msg = ("This is not a valid entry")
        self.not_open_msg = ("POSITION TAKEN")
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

    #DISPLAY AND MODIFY BOARD
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
        board = self.place_board

        for i in win_combos:
            if board[i[0]] == 1 and board[i[1]] == 1 and  board[i[2]] == 1: 
                print("X WINS")
            if board[i[0]] == 2 and  board[i[1]] == 2 and  board[i[2]] == 2: 
                print("O WINS")

    #CHECK OPEN POSITIONS 
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
            self.turns += 1
        else: 
            print(self.not_open_msg)

    def place_o(self, index): 
        if self.is_position_open(index) == True: 
            self.place_board[index] = 2
            self.turns += 1
        else: 
            print(self.not_open_msg)

    #GAME CHOICES
    def player_vs_computer(self): 
            pass

    def player_vs_player(self): 
        while self.turns < 9:  
            move = self.human_player.make_move()
            index = self.find_index_of_move(move)
            self.place_x(index)
            self.check_for_win()
            self.display_board()

    def computer_vs_computer(self): 
        pass

    def display_rules(self): 
        self.user_interface.display_rules()
        return self.choose_menu_choice()

    def exit_game(self): 
        exit()

    def choose_menu_choice(self): 
        print(self.menu_choice_msg)
        menu_choices = [self.player_vs_computer, self.player_vs_player, self.computer_vs_computer, self.display_rules, self.exit_game]
        user_choice = int(input("Please choose (1-5): ")) - 1 
        menu_choices[user_choice]()

if __name__ == "__main__": 
    a = GameEngine()
    a.choose_menu_choice()
    

            
        

from user_interface import UserInterface
from player import Player
from human import Human
from computer import Computer
import os
import time


class GameEngine(object):

    def __init__(self):
        self.user_interface = UserInterface()
        self.computer_player = Computer()
        self.human_player = Human()
        self.menu_choice_msg = ("\nTIC TAC TOE MENU \n1. Player vs Computer \n2. Player vs Player \n3. Computer vs Computer \n4. Display Rules \n5. Quit")
        self.invalid_entry_msg = ("This is not a valid entry, please try again: ")
        self.input_choice_msg = ("""Please pick menu choice(1-5): """)
        self.catgame_msg = ("CAT GAME! Better luck next time!")
        self.pvp_prompt_msg = ("X goes first, O goes second.")
        self.x_win_msg = ("Player X wins")
        self.o_win_msg = ("Player O wins")
        self.placeholder_board = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.win_combos = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
        self.game_running = True
        self.turns = 0
        self.x_moves = 0
        self.o_moves = 0
        self.scores = []

    def exit_game(self):
        return exit()

    def modify_game_board_list(self, board):
        game_board_list = []
        for i in range(0, 9):
            if board[i] == 1:
                game_board_list.append('X')
            elif board[i] == 2:
                game_board_list.append('O')
            elif board[i] == 0:
                game_board_list.append(' ')
        return game_board_list

    def display_board(self, board):
        game_board_list = self.modify_game_board_list(board)
        print("""
         {} | {} | {}
        ---+---+---
         {} | {} | {}
        ---+---+---
         {} | {} | {}
        """.format(*game_board_list))

    def x_win(self, board):
        for i in self.win_combos:
            if board[i[0]] == 1 and board[i[1]] == 1 and board[i[2]] == 1:
                return True

    def o_win(self, board):
        for i in self.win_combos:
            if board[i[0]] == 2 and board[i[1]] == 2 and board[i[2]] == 2:
                return True

    def check_for_win(self, board):
        if self.x_win(board) == True:
            print(self.x_win_msg)
            self.game_running = False
            self.play_again()
        if self.o_win(board) == True:
            print(self.o_win_msg)
            self.game_running = False
            self.play_again()
        else:
            self.game_running = True

    def out_of_turns(self):
        if self.turns == 9: 
            self.game_running == False 
        return self.turns == 9

    def take_turn(self, player): 
        board = self.placeholder_board
        index = player.find_index_of_move(board)
        x_moves, o_moves = player.all_moves(board)
        player_marker = player.set_player_marker(x_moves, o_moves) 
        player.make_move(index, board, player_marker)

    def pause(self): 
        return time.sleep(1)

    def clear_screen(self): 
        return os.system('clear')

    def run_game(self, player):
        if self.out_of_turns():
           print(self.catgame_msg)
           self.play_again()
        else: 
            board = self.placeholder_board
            self.take_turn(player)
            self.turns += 1
            self.display_board(board)
            self.check_for_win(board)
            self.pause()

    def player_vs_computer(self):
        board = self.placeholder_board
        turn_choice = self.human_player.set_turn()
        while self.game_running:
            if turn_choice == 2:
                self.run_game(self.computer_player)
                self.run_game(self.human_player)
            if turn_choice == 1:
                self.run_game(self.human_player)
                self.run_game(self.computer_player)

    def player_vs_player(self):
        board = self.placeholder_board
        while self.game_running:
            self.run_game(self.human_player)

    def computer_vs_computer(self):
        board = self.placeholder_board
        while self.game_running:
            self.run_game(self.computer_player)
            self.clear_screen()

    def display_rules(self):
        self.user_interface.display_rules()
        return self.choose_menu_choice()

    def choose_menu_choice(self):
        self.user_interface.display_game_prompt()
        self.user_interface.display_menu()
        menu_choices = [self.player_vs_computer, self.player_vs_player, self.computer_vs_computer, self.display_rules, self.exit_game]
        while True:
           try:
              menu_choice = int(input(self.input_choice_msg)) - 1
           except ValueError:
              print(self.invalid_entry_msg)
           else:
              return menu_choices[menu_choice]()

    def play_again(self): 
        answer = input("Y or N: ").upper()
        if answer == "Y": 
            self.choose_menu_choice()
        else: 
            exit()

if __name__ == "__main__":
    a = GameEngine()
    a.choose_menu_choice()

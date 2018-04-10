from user_interface import UserInterface 
from player import Player
from human import Human
from computer import Computer
import time

class GameEngine(object): 

    def __init__(self): 
        self.user_interface = UserInterface()
        self.computer_player = Computer()
        self.human_player = Human()
        self.menu_choice_msg = ("\nTIC TAC TOE MENU \n1. Player vs Computer \n2. Player vs Player \n3. Computer vs Computer \n4. Display Rules \n5. Quit")
        self.invalid_entry_msg = ("This is not a valid entry, please try again: ")
        self.input_choice_msg = ("""Please pick menu choice(1-5): """)
        self.placeholder_board = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.win_combos = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
        self.game_running = True
        self.turns = 0

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
            print("Player X WINS")
            self.game_running = False
            exit()
        if self.o_win(board) == True: 
            print("Player O WINS")
            self.game_running = False
            exit()
        else: 
            self.game_running = True

    def finish_turn(self, board): 
        self.turns += 1
        self.display_board(board)
        self.check_for_win(board)
        time.sleep(1)

    def out_of_turns(self): 
        return self.turns == 9

    def player_vs_computer(self): 
        board = self.placeholder_board
        turn_choice = self.human_player.set_turn() 
        if turn_choice == 2: 
            while self.game_running:
               index = self.computer_player.find_index_of_move(board)
               self.computer_player.make_move(index, board, player_num = 1)
               self.finish_turn(board)
               if self.out_of_turns(): 
                  print("It is a CAT GAME")
                  break 
               else: 
                  index = self.human_player.find_index_of_move(board)
                  self.human_player.make_move(index, board, player_num = 2)
                  self.finish_turn(board)
        if turn_choice == 1: 
            while self.game_running:
               index = self.human_player.find_index_of_move(board)
               self.human_player.make_move(index, board, player_num = 1)
               self.finish_turn(board)
               if self.out_of_turns(): 
                  print("It is a CAT GAME")
                  break 
               else: 
                  index = self.computer_player.find_index_of_move(board)
                  self.computer_player.make_move(index, board, player_num = 2)
                  self.finish_turn(board)

    def player_vs_player(self): 
        board = self.placeholder_board
        print("Player One is 'X', Player Two is 'O'")
        while self.game_running: 
            index = self.human_player.find_index_of_move(board)
            self.human_player.make_move(index, board, player_num = 1)
            self.finish_turn(board)
            if self.out_of_turns(): 
               print("It is a CAT GAME")
               break 
            else: 
               index = self.human_player.find_index_of_move(board)
               self.human_player.make_move(index, board, player_num = 2)
               self.finish_turn(board)

    def computer_vs_computer(self): 
        board = self.placeholder_board
        while self.game_running: 
            index = self.computer_player.find_index_of_move(board)
            self.computer_player.make_move(index, board, player_num = 1)
            self.finish_turn(board)
            if self.out_of_turns(): 
               print("It is a CAT GAME")
               break 
            else: 
               index = self.computer_player.find_index_of_move(board)
               self.computer_player.make_move(index, board, player_num = 2)
               self.finish_turn(board)
            
    def display_rules(self): 
        self.user_interface.display_rules()
        return self.choose_menu_choice()

    def exit_game(self): 
        exit()

    #__________MENU___________
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
              menu_choices[menu_choice]()

if __name__ == "__main__": 
    a = GameEngine()
    a.choose_menu_choice()


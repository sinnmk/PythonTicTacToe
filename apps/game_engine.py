from user_interface import UserInterface
from player import Player
from human import Human
from computer import Computer
from minimax import Minimax
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
        self.x_moves = 0
        self.o_moves = 0

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

    def count_x(self, board): 
        x_moves = []
        i = 0
        while i < len(board): 
            for marker in board: 
                if marker == 1: 
                    x_moves.append(marker)
                i += 1
            return x_moves

    def count_o(self, board): 
        o_moves = []
        i = 0
        while i < len(board): 
            for marker in board: 
                if marker == 2: 
                    o_moves.append(marker)
                i += 1
            return o_moves
    
    def turn_counter(self, x_moves, o_moves): 

        #NOT COMPLETED

        #figure out how to use a turn counter to set the marker of each player instead of hardcoding it 

        #figure out how to properly assign the player num in computer vs computer 

        if len(x_moves) == 0 and len(o_moves) == 0: 
            player_num = 1
            print(player_num)
            return player_num
        elif len(x_moves) > len(o_moves):
            player_num = 2
            print(player_num)
            return player_num
        elif len(o_moves) > len(x_moves): 
            player_num = 1
            print(player_num)
            return player_num

   # def turn_counter(self, board): 
   #     x_moves = []
   #     o_moves = []
   #     for num in board: 
   #         if num == 1: 
   #             x_moves.append(num)
   #         if num == 2: 
   #             o_moves.append(num)
   #     if len(x_moves) == 0: 
   #         player_num = 1
   #         return player_num
   #     if len(x_moves) > len(o_moves): 
   #         print("o_turn")
   #         player_num = 2
   #         return player_num
   #     if len(o_moves) > len(x_moves): 
   #         print("x_turn")
   #         player_num = 1
   #         return player_num
   #     if len(x_moves) == len(o_moves): 
   #         player_num = 1
   #         return player_num

    def player_vs_computer(self):
        pass
  #      board = self.placeholder_board
  #      turn_choice = self.human_player.set_turn()
  #      if turn_choice == 2:
  #          while self.game_running:
  #             index = self.computer_player.find_index_of_move(board)
  #             self.computer_player.make_move(index, board, player_num = 1)
  #             self.finish_turn(board)
  #             if self.out_of_turns():
  #                print("It is a CAT GAME")
  #                break
  #             else:
  #                index = self.human_player.find_index_of_move(board)
  #                self.human_player.make_move(index, board, player_num = 2)
  #                self.finish_turn(board)
  #      if turn_choice == 1:
  #          while self.game_running:
  #             index = self.human_player.find_index_of_move(board)
  #             self.human_player.make_move(index, board, player_num = 1)
  #             self.finish_turn(board)
  #             if self.out_of_turns():
  #                print("It is a CAT GAME")
  #                break
  #             else:
  #                index = self.computer_player.find_index_of_move(board)
  #                self.computer_player.make_move(index, board, player_num = 2)
  #                self.finish_turn(board)

    def player_vs_player(self):
        pass
  #      board = self.placeholder_board
  #      print("Player One is 'X', Player Two is 'O'")
  #      while self.game_running:
  #          index = self.human_player.find_index_of_move(board)
  #          self.human_player.make_move(index, board, player_num = 1)
  #          self.finish_turn(board)
  #          if self.out_of_turns():
  #             print("It is a CAT GAME")
  #             break
  #          else:
  #             index = self.human_player.find_index_of_move(board)
  #             self.human_player.make_move(index, board, player_num = 2)
  #             self.finish_turn(board)

    def computer_vs_computer(self):

        #figure out how to use player num as parameter instead of hard coding the number

        board = self.placeholder_board
        x_moves = self.count_x(board)
        o_moves = self.count_o(board)
        while self.game_running:
            player_num = self.turn_counter(x_moves, o_moves)
            index = self.computer_player.find_index_of_move(board)
            self.computer_player.make_move(index, board, player_num)
            self.finish_turn(board)
            if self.out_of_turns():
               print("It is a CAT GAME")
               break
            else:
               player_num = self.turn_counter(x_moves, o_moves)
               index = self.computer_player.find_index_of_move(board)
               self.computer_player.make_move(index, board, player_num)
               self.finish_turn(board)

    def display_rules(self):
        self.user_interface.display_rules()
        return self.choose_menu_choice()

    def exit_game(self):
        return exit()

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

if __name__ == "__main__":
    a = GameEngine()
    board = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    x_moves = a.count_x(board)
    o_moves = a. count_o(board) 
    a.turn_counter(x_moves, o_moves)
    a.computer_vs_computer()


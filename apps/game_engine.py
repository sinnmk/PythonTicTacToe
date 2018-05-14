from user_interface import UserInterface
from human import Human
from computer import Computer
import math
import time

class GameEngine(object):

    def __init__(self):
        self.user_interface = UserInterface()

    def create_board(self, size): 
        board = ([0] * size **2) 
        return board

    def display_board(self, size, board):
        game_board_list = self.user_interface.modify_game_board_list(size, board)
        display_board = self.user_interface.display_game_board(size, game_board_list)
        return display_board

    def get_available_moves(self, board): 
        available_moves = []
        for i in range(0, len(board)): 
            if board[i] == 0: 
                available_moves.append(i + 1)
        return available_moves

    def switch_player(self, turn_player, player_one, player_two): 
        if turn_player == player_one:  
            turn_player = player_two 
            return turn_player
        else:
            turn_player = player_one 
            return turn_player

    def get_size(self): 
        size = self.user_interface.input_size_of_board()
        return size

    def run_game(self, player_one, player_two):
        size = self.get_size()
        board = self.create_board(size)
        win_combos = self.win_combo_list(size)
        game_running = True
        difficulty = self.user_interface.input_difficulty_choice()
        self.user_interface.clear_screen()
        turn_player = player_one
        self.user_interface.display_example_board()
        while game_running == True: 
            turn_player.make_move(board, difficulty)
            self.display_board(size, board)
            if self.is_game_over(board, size, win_combos, turn_player) == True: 
                game_running = False
            turn_player = self.switch_player(turn_player, player_one, player_two) 
            time.sleep(1)
        self.user_interface.clear_screen()
        self.user_interface.display_play_again_msg()
        self.play_again()

    def game_setup(self): 
        self.user_interface.display_game_prompt()
        self.user_interface.display_menu()
        game_mode = self.user_interface.input_menu_choice()
        if game_mode == 1: 
            turn_choice = self.user_interface.input_turn_choice()
            if turn_choice == 1: 
                player_one = Human(marker = 1) 
                player_two = Computer(marker = 2)
                self.run_game(player_one, player_two)
            else: 
                player_one = Computer(marker = 1)
                player_two = Human(marker = 2)
                self.run_game(player_one, player_two)
                
        elif game_mode == 2: 
            player_one = Human(marker = 1)
            player_two = Human(marker = 2)
            self.run_game(player_one, player_two)

        elif game_mode == 3: 
            player_one = Computer(marker = 1)
            player_two = Computer(marker = 2)
            self.run_game(player_one, player_two)

        elif game_mode == 4: 
            self.user_interface.display_game_rules()
            time.sleep(1)
            self.game_setup()

        elif game_mode == 5: 
            self.user_interface.display_goodbye_msg()
            exit()

    def play_again(self): 
        self.user_interface.display_play_again_msg()
        choice = self.user_interface.input_play_again_choice() 
        choice = choice.upper()
        if choice == "Y": 
            self.game_setup()
        else: 
            self.user_interface.display_goodbye_msg()
            exit()

    def create_index_board(self, size): 
        num_of_cells = size**2 
        i = -1 
        index_board = []
        while i < (num_of_cells-1): 
            index_board.append(i+1)
            i += 1
        return index_board

    def generate_horizontal_win_combos(self, size): 
        index_board = self.create_index_board(size)
        horizontal_wins = []
        for i in index_board: 
            horizontal_wins.append(i)
        horizontal_wins = self.split_list(horizontal_wins, size)
        return horizontal_wins

    def generate_vertical_win_combos(self, size): 
        index_board = self.create_index_board(size)
        vertical_wins = []
        i = 0
        num_of_cells = size**2
        while i < len(index_board):
            vert_win = index_board[0+i:num_of_cells:size]
            if len(vert_win) == size:
                vertical_wins.append(vert_win)
            i += 1
        return vertical_wins

    def generate_right_diagonal_win_combo(self, size): 
        index_board = self.create_index_board(size)
        num_of_cells = size**2
        right_diagonal_win_combos = []
        right_diagonal_win_combos.append(index_board[0:num_of_cells:(size+1)])
        return right_diagonal_win_combos

    def generate_left_diagonal_win_combo(self, size): 
        index_board = self.create_index_board(size)
        num_of_cells = size**2
        left_diagonal_win_combos = []
        left_diagonal_win_combos.append(index_board[(size -1):(num_of_cells) - (size-1):(size -1)])
        return left_diagonal_win_combos

    def win_combo_list(self, size): 
        vertical_wins = self.generate_vertical_win_combos(size)
        horizontal_wins = self.generate_horizontal_win_combos(size)
        rt_diag_wins = self.generate_right_diagonal_win_combo(size)
        lt_diag_wins = self.generate_left_diagonal_win_combo(size)
        win_combo_list = (vertical_wins+ horizontal_wins+ rt_diag_wins + lt_diag_wins)
        return win_combo_list

    def is_game_over(self, board, size, win_combos, turn_player): 
        available_moves = self.get_available_moves(board)
        combo_points = 0
        for combo in win_combos: 
           for number in combo: 
              if board[number] == turn_player.marker: 
                 combo_points += 1
                 if combo_points == size:
                    print(turn_player.name, "wins")
                    return True
           combo_points = 0
        if len(available_moves) == 0:
           self.user_interface.display_cat_game_msg()
           return True
                  
    def split_list(self, board, size):
        new_board = [board[i:i+size] for i in range(0, (len(board)), size)]
        return new_board

if __name__ == "__main__":
    a = GameEngine()
    a.game_setup()



from user_interface import UserInterface
from human import Human
from computer import Computer
import math
import time

class GameEngine(object):

    def __init__(self):
        self.user_interface = UserInterface()

    def display_board(self, board):
        game_board_list = self.user_interface.modify_game_board_list(board)
        display_board = self.user_interface.display_game_board(game_board_list)
        return display_board

    def get_available_moves(self, board): 
        available_moves = []
        for i in range(0, len(board)): 
            if board[i] == 0: 
                available_moves.append(i + 1)
        return available_moves

    def is_game_over(self, board, turn_player):
        available_moves = self.get_available_moves(board)
        win_combos = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
        for i in win_combos:
            if board[i[0]] == turn_player.marker and board[i[1]] == turn_player.marker and board[i[2]] == turn_player.marker:
                print(turn_player.name, " wins!")
                return True
        if len(available_moves) == 0: 
            self.user_interface.display_cat_game_msg()
            return True

    def switch_player(self, turn_player, player_one, player_two): 
        if turn_player == player_one:  
            turn_player = player_two 
            return turn_player
        else:
            turn_player = player_one 
            return turn_player

    def run_game(self, player_one, player_two):
        game_running = True
        board = self.create_board()
        difficulty = self.user_interface.input_difficulty_choice()
        self.user_interface.clear_screen()
        turn_player = player_one
        self.user_interface.display_example_board()
        while game_running == True: 
            print("It is ", turn_player.name,"'s turn...")
            turn_player.make_move(board, difficulty)
            self.display_board(board)
            if self.is_game_over(board, turn_player) == True: 
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

    def create_board(self): 
        size = self.user_interface.input_size_of_board()
        board = ([0] * size **2) 
        return board

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
        print(win_combo_list)
        return win_combo_list

   # def is_game_over(self, board, turn_player):
   #     available_moves = self.get_available_moves(board)
   #     win_combos = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
   #     for i in win_combos:
   #         if board[i[0]] == turn_player.marker and board[i[1]] == turn_player.marker and board[i[2]] == turn_player.marker:
   #             print(turn_player.name, " wins!")
   #             return True
   #     if len(available_moves) == 0: 
   #         self.user_interface.display_cat_game_msg()
   #         return True

    def is_game_over(self, board, size, turn_player): 
        pass

    def split_list(self, board, size):
        new_board = [board[i:i+size] for i in range(0, (len(board)), size)]
        return new_board

if __name__ == "__main__":
    a = GameEngine()
    size = 4
    a.win_combo_list(size)
    board = [1, 1, 1, 0, 0, 0, 0, 0, 0]
    turn_player = 1
    a.is_game_over(board, size, turn_player)




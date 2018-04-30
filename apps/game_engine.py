from user_interface import UserInterface
from human import Human
from computer import Computer
import os
import time

class GameEngine(object):

    def __init__(self):
        self.user_interface = UserInterface()

    def create_board(self): 
        board = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        return board

    def modify_game_board_list(self, board):
        game_board_list = []
        for i in range(0, 9):
            if board[i] == 1:
                game_board_list.append('X')
            elif board[i] == 2:
                game_board_list.append('O')
            elif board[i] == 0: game_board_list.append(' ')
        return game_board_list

    def display_board(self, board):
        game_board_list = self.modify_game_board_list(board)
        #put in ui and figure out how to input using string interpolation
        print("""
         {} | {} | {}
        ---+---+---
         {} | {} | {}
        ---+---+---
         {} | {} | {}
        """.format(*game_board_list))

    def get_available_moves(self, board): 
        available_moves = []
        for i in range(0, len(board)): 
            if board[i] == 0: 
                available_moves.append(i + 1)
        return available_moves

    def is_game_over(self, board):
        available_moves = self.get_available_moves(board)
        win_combos = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
        if len(available_moves) == 0: 
            return True
        else: 
            for i in win_combos:
                if board[i[0]] == 1 and board[i[1]] == 1 and board[i[2]] == 1:
                    return True

    def switch_player(self, turn_player): 
        if turn_player == Human(marker = 1): 
            turn_player = Computer(marker = 2)
            return turn_player
        else: 
            turn_player = Human(marker = 1)
            return turn_player

    def take_turn(self, board, turn_player): 
        player = turn_player
        move = player.make_move(board)
        return move
        
    def run_game(self, player_one, player_two):
        game_running = True
        board = self.create_board()
        turn_player = player_one
        while game_running == True: 
            if self.is_game_over(board) == True: 
                self.user_interface.display_game_over_msg()
                self.user_interface.display_play_again_msg()
                self.play_again()
                break
            else: 
                self.take_turn(board, turn_player)
                self.display_board(board)
                self.switch_player(turn_player)

    def game_set_up(self): 
        game_mode = self.get_game_type()

        if game_mode == 1: 
            turn_choice = self.set_turn()
            if turn_choice == 1: 
                player_one = Human(marker = 1) 
                player_two = Computer(marker = 2)
                self.run_game(player_one, player_two)
            else: 
                player_one = Computer(marker = 1)
                player_two = Human(marker = 2)
                self.run_game(player_one, player_two)
                
        if game_mode == 2: 
            player_one = Human(marker = 1)
            player_two = Human(marker = 2)
            self.run_game(player_one, player_two)

        if game_mode == 3: 
            player_one = Computer(marker = 1)
            player_two = Computer(marker = 2)
            self.run_game(player_one, player_two)

    def get_game_type(self): 
        game_mode = self.user_interface.input_menu_choice()
        return game_mode

    def set_turn(self): 
        turn_choice = self.user_interface.input_turn_choice()
        return turn_choice  

    def play_again(self): 
        print(self.play_again_msg)
        answer = input("Y or N: ").upper()
        if answer == "Y": 
            self.menu_choice()
        else: 
            exit()


if __name__ == "__main__":
    a = GameEngine()
    player_one = Computer(marker = 1)
    player_two = Computer(marker = 2)
    a.run_game(player_one, player_two)


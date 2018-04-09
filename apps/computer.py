from player import Player 
import random

class Computer(Player): 

    def __init__(self): 
        self.num_board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.win_combos = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))

    def get_possible_win_combos(self, board): 
        winning_moves = []
        for combo in self.win_combos: 
            if board[combo[0]] == 1 and board[combo[1]] == 1 and board[combo[2]] == 0: 
                moves = self.num_board[combo[2]]
                winning_moves.append(moves)
            if board[combo[0]] == 0 and board[combo[1]] == 1 and board[combo[2]] == 1: 
                moves = self.num_board[combo[0]]
                winning_moves.append(moves)
            if board[combo[0]] == 1 and board[combo[1]] == 0 and board[combo[2]] == 1: 
                moves = self.num_board[combo[1]]
                winning_moves.append(moves)
        return winning_moves

    def get_possible_lose_combos(self, board):
        blocking_moves = []
        for combo in self.win_combos: 
            if board[combo[0]] == 2 and board[combo[1]] == 2 and board[combo[2]] == 0: 
                moves = self.num_board[combo[2]]
                blocking_moves.append(moves)
            if board[combo[0]] == 0 and board[combo[1]] == 2 and board[combo[2]] == 2: 
                moves = self.num_board[combo[0]]
                blocking_moves.append(moves)
            if board[combo[0]] == 2 and board[combo[1]] == 0 and board[combo[2]] == 2: 
                moves = self.num_board[combo[1]]
                blocking_moves.append(moves)
        return blocking_moves

    def get_open_positions(self, board): 
        open_positions = []
        i = 0
        while i < len(board): 
            for digit in board: 
                if board[i] == 0: 
                    open_positions.append(i + 1)
                if board[i] != 0: 
                    open_positions.append("")
                i += 1
        return open_positions

    def make_move(self, board):
        i = 0
        open_positions = [] 
        winning_moves = self.get_possible_win_combos(board)
        blocking_moves = self.get_possible_lose_combos(board)
        open_positions = self.get_open_positions(board)
        if len(winning_moves) > 0: 
            move = random.choice(winning_moves)
            return move
        if len(blocking_moves) > 0:
            move = random.choice(blocking_moves)
            return move
        move = random.choice(self.num_board)
        if move in open_positions: 
            return move
        else: 
            return self.make_move(board)

    def set_name(self): 
        name = "Computer"
        return name

    def set_turn(self): 
        turn_choices = [1, 2]
        choice = random.choice(turn_choices)
        return choice

    

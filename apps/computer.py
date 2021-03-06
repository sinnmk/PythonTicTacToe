from player import Player
import random

class Computer(Player):

    def __init__(self):
        self.num_board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.win_combos = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))


    def get_possible_win_combos(self, board):
        winning_moves = []
        for i in self.win_combos:
            if board[i[0]] == 1 and board[i[1]] == 1 and board[i[2]] == 0:
                moves = self.num_board[i[2]]
                winning_moves.append(moves)
            if board[i[0]] == 0 and board[i[1]] == 1 and board[i[2]] == 1:
                moves = self.num_board[i[0]]
                winning_moves.append(moves)
            if board[i[0]] == 1 and board[i[1]] == 0 and board[i[2]] == 1:
                moves = self.num_board[i[1]]
                winning_moves.append(moves)
        return winning_moves


    def get_possible_lose_combos(self, board):
        blocking_moves = []
        for i in self.win_combos:
            if board[i[0]] == 2 and board[i[1]] == 2 and board[i[2]] == 0:
                moves = self.num_board[i[2]]
                blocking_moves.append(moves)
            if board[i[0]] == 0 and board[i[1]] == 2 and board[i[2]] == 2:
                moves = self.num_board[i[0]]
                blocking_moves.append(moves)
            if board[i[0]] == 2 and board[i[1]] == 0 and board[i[2]] == 2:
                moves = self.num_board[i[1]]
                blocking_moves.append(moves)
        return blocking_moves


    def get_open_positions(self, board):
        copy_board = board[:]
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


    def get_move(self, board):
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
            return self.get_move(board)


    def set_name(self):
        name = "Computer"
        return name



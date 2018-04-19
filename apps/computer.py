from player import Player
import copy
import random

class Computer(Player):

    def __init__(self):
        self.num_board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.win_combos = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
        self.scores = []
        self.depth = 0
        self.max_depth = 9 

    def get_possible_win_combos(self, board):
        winning_moves = []
        for i in self.win_combos:
            if board[i[0]] == 1 and board[i[1]] == 1 and board[i[2]] == 0:
                move = self.num_board[i[2]]
                winning_moves.append(move)
            if board[i[0]] == 0 and board[i[1]] == 1 and board[i[2]] == 1:
                move = self.num_board[i[0]]
                winning_moves.append(move)
            if board[i[0]] == 1 and board[i[1]] == 0 and board[i[2]] == 1:
                move = self.num_board[i[1]]
                winning_moves.append(move)
        return winning_moves

    def get_possible_lose_combos(self, board):
        blocking_moves = []
        for i in self.win_combos:
            if board[i[0]] == 2 and board[i[1]] == 2 and board[i[2]] == 0:
                move = self.num_board[i[2]]
                blocking_moves.append(move)
            if board[i[0]] == 0 and board[i[1]] == 2 and board[i[2]] == 2:
                move = self.num_board[i[0]]
                blocking_moves.append(move)
            if board[i[0]] == 2 and board[i[1]] == 0 and board[i[2]] == 2:
                move = self.num_board[i[1]]
                blocking_moves.append(move)
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


    def x_win(self, board):
        for i in self.win_combos:
            if board[i[0]] == 1 and board[i[1]] == 1 and board[i[2]] == 1:
                return True
            else: 
                return False

    def o_win(self, board):
        for i in self.win_combos:
            if board[i[0]] == 2 and board[i[1]] == 2 and board[i[2]] == 2:
                return True
            else: 
                return False

    def board_is_terminal(self, board):
        i = 0
        if self.x_win(board) == True: 
            return True
        elif self.o_win(board) == True: 
            return True
        elif all(board) != 0: 
            return True
        while i < len(board): 
            for num in board: 
                if board[i] == 0: 
                    return False
                i += 1

    def score_board(self, board): 
        if self.x_win(board) == True: 
            self.scores.append(10)
            print('x')
        elif self.o_win(board) == True: 
            self.scores.append(-10)
            print('o')
        elif self.board_is_terminal(board) == True and self.x_win(board) == False and self.o_win(board) == False: 
            self.scores.append(0)
        print(self.scores, "score")
        return self.scores

    def get_available_moves(self, board): 
        moves = self.get_open_positions(board) 
        available_moves = [x for x in moves if isinstance(x, int)]
        return available_moves

    def get_index_of_available_moves(self, board): 
        available_moves = self.get_available_moves(board)
        index_of_moves = []
        for i in available_moves: 
            index_of_moves.append(i -1)
        return index_of_moves

    def minimax(self, board, depth, is_max_player):
        new_board = board[:]

        if self.board_is_terminal(new_board) == True: 
            print(self.score_board(new_board))
            return self.score_board(new_board) 

        else: 
            if is_max_player == True: 
                state_score = [-10] 
            else: 
                state_score = [10]
            index = super(Computer, self).find_index_of_move(new_board)
            x_moves, o_moves = super(Computer, self).all_moves(new_board)
            player_marker = super(Computer, self).set_player_marker(x_moves, o_moves) 
            available_moves = self.get_available_moves(board)
            super(Computer, self).make_move(index, new_board, player_marker)
            next_score = self.scores
            print(self.scores, "self scores")
            print(new_board, "new_board")
            next_score = self.minimax(new_board, depth, is_max_player) 
            if next_score < state_score: 
                next_score = state_score
                print(next_score, "next score")
            elif next_score > state_score: 
                next_score = state_score
                print(next_score, "next score")
            print(next_score, "last")
            return next_score

    def take_master_move(self): 
        master_move_list = [index for index in enumerate(self.scores)]            
        print(master_move_list)

if __name__ == "__main__": 
    a = Computer()
    board = [1, 1, 0, 0, 2, 0, 2, 1, 2]
    depth = 0
    is_max_player = True
    a.minimax(board, depth, is_max_player)


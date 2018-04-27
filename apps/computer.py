from player import Player
import random

class Computer(Player):

    def __init__(self):
        self.num_board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.win_combos = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
        self.x_scores = []
        self.o_scores = []
        self.max_depth = -9 

    def set_name(self):
        name = "Computer"
        return name

    def get_open_positions(self, board): 
        open_positions = []
        for i in range(0, len(board)): 
            if board[i] == 0: 
                open_positions.append(i + 1)
        return open_positions

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

    def move(self, board): 
        index = super(Computer, self).find_index_of_move(board)
        x_moves, o_moves = super(Computer, self).all_moves(board)
        player_marker = super(Computer, self).set_player_marker(x_moves, o_moves)
        move = super(Computer, self).make_move(index, board, player_marker)
        return move

    def find_depth(self, board): 
        open_positions = self.get_open_positions(board)
        depth_lost = 9 - len(open_positions)
        depth = 0 - depth_lost 
        return depth

    def minimax(self, board): 
        new_board = board[:]
        available_moves = self.get_open_positions(new_board)
        if self.board_is_terminal == True:
            if self.x_win() == True: 
                return 100
            if self.o_win() == True: 
                return -100
            else: 
                return 0

        for move in available_moves: 
            pass

    def min_play(self): 
        if self.board_is_terminal() == True: 
            return self.minimax(new_board)

    def max_play(self): 
        if self.board_is_terminal() == True: 
            return self.minimax(new_board)
        
if __name__ == "__main__":
    a = Computer()
    board = [0, 0, 0, 0, 0, 0, 0, 0, 0]


    


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
   
   # def get_move(self, board): 
   #     open_positions = self.get_open_positions(board)
   #     tried_positions = []
   #     for i in open_positions: 
   #       tried_positions.append(i)
   #       return i

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

    def minimax(self, board, depth, player_marker): 
        new_board = board[:]
        choices = []
        x_moves, o_moves = super(Computer, self).all_moves(new_board)
        player_marker = super(Computer, self).set_player_marker(x_moves, o_moves)
        open_positions = self.get_open_positions(new_board)

        if self.board_is_terminal(new_board) == True or depth == self.max_depth: 
            if self.x_win(new_board) == True: 
                return 100
            if self.o_win(new_board) == True: 
                return -100
            else: 
                return 0

        if player_marker == 1: 
           best_score = -100
           for move in open_positions: 
               self.move(new_board)
               move_score = self.minimax(new_board, depth - 1, player_marker)
               best_score = max(best_score, move_score) 
           return best_score

        if player_marker == 2: 
           best_score = 100
           for move in open_positions: 
               self.move(new_board)
               move_score = self.minimax(new_board, depth - 1, player_marker)
               best_score = min(best_score, move_score) 
           return best_score

    def best_move(self, board, depth, player_marker): 
        choices = []
        open_positions = self.get_open_positions(new_board)
        
        for move in open_positions: 
            self.move(board)
            move_score = self.minimax(board, depth - 1, player_marker)
            if move_score > 0: 
               choices = [move]
            elif move_score == 0: 
               choices.append(move)

        if len(choices) > 0: 
           move = random.choice(choices)
           print("MOVE CHOICE: ", move)
           return move 
        else: 
           position = random.choice(open_positions)
           return move 
        
if __name__ == "__main__":
    a = Computer()
    board = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    new_board = board[:]
    depth = a.find_depth(board)
    player_marker = 1
    a.best_move(board, depth, player_marker)


    


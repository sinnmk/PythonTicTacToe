from player import Player
import random

class Computer(Player):

    def __init__(self):
        self.num_board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.win_combos = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
        self.scores = []
        self.moves = []
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
        open_positions = []
        for i in range(0, len(board)): 
            if board[i] == 0: 
                open_positions.append(i + 1)
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
    
   # def get_move(self, board): 
   #     available_moves = self.get_open_positions(board)
   #     for i in available_moves: 
   #         return i

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

    def minimax(self, board, depth, player_marker):
        if self.board_is_terminal == True: 
            if self.x_win(board) == True: 
                return -50
            elif self.o_win(board) == True: 
                return 50 
            else: 
                return 0

        if player_marker == 2: 
            best_val = -50
            available_moves = self.get_open_positions(board)

            for move in available_moves: 
                index = super(Computer, self).find_index_of_move(board)
                x_moves, o_moves = super(Computer, self).all_moves(board)
                player_marker = super(Computer, self).set_player_marker(x_moves, o_moves)
                super(Computer, self).make_move(index, board, player_marker)
                #move_val = self.minimax(board, depth - 1, player_marker)
                move_val = 1
                best_val = max(best_val, move_val)
            print(best_val, "best val for o")
            return best_val

        if player_marker == 1: 
            best_val = 50 
            available_moves = self.get_open_positions(board)

            for move in available_moves: 
                index = super(Computer, self).find_index_of_move(board)
                x_moves, o_moves = super(Computer, self).all_moves(board)
                player_marker = super(Computer, self).set_player_marker(x_moves, o_moves)
                super(Computer, self).make_move(index, board, player_marker)
                move_val = 1
                #move_val = self.minimax(board, depth - 1, player_marker)
                best_val = min(best_val, move_val)
            print(best_val, "best val for x")
            return best_val

    def take_best_move(self, board, depth, player_marker): 
        available_moves = self.get_open_positions(board)
        draw_val = 0 
        choices = []
        print(board, "board")

        for move in available_moves: 
            index = super(Computer, self).find_index_of_move(board)
            x_moves, o_moves = super(Computer, self).all_moves(board)
            player_marker = super(Computer, self).set_player_marker(x_moves, o_moves)
            super(Computer, self).make_move(index, board, player_marker)
            move_val = 1
            #move_val = self.minimax(board, depth - 1, player_marker)

            if move_val > draw_val: 
                choices = [move]
                print(choices, "choices")

            elif move_val == draw_val: 
                choices.append(move)
                print(choices, "choices")

        if len(choices) > 0: 
            best_move = random.choice(choices)
            print(best_move, "best_move")
            return best_move

        else: 
            rand_move = random.choice(available_moves)
            print(rand_move, "random move")
            return rand_move


if __name__ == "__main__": 
    a = Computer()
    board = [0, 2, 0, 0, 1, 0, 0, 2, 1]
    depth = 9
    player_marker = 1
    a.minimax(board, depth, player_marker)
    a.take_best_move(board, depth, player_marker)


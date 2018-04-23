from player import Player
import copy
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


    def get_available_moves(self, board): 
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
        moves = open_positions
        available_moves = [x for x in moves if isinstance(x, int)]
        print(available_moves)
        return available_moves

    def get_move(self, board): 
        available_moves = self.get_available_moves(board)
        move = random.choice(available_moves)
        return move 

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

    def change_player(self, player_marker): 
        if player_marker == 1: 
            return player_marker == 2
        if player_marker == 2: 
            return player_marker == 1

    def minimax(self, node, depth, player_marker):
        if self.board_is_terminal == True: 
            if self.x_win(board) == True: 
                print("-50")
                return -50
            elif self.o_win(board) == True: 
                print("50")
                return 50 
            else: 
                print("0")
                return 0

        if player_marker == 2: 
            best_val = -50
            available_moves = self.get_available_moves(board)

            for move in available_moves: 
                index = super(Computer, self).find_index_of_move(board)
                print("index", index)
                x_moves, o_moves = super(Computer, self).all_moves(board)
                player_marker = super(Computer, self).set_player_marker(x_moves, o_moves)
                move_val = self.minimax(board, depth - 1, player_marker)
                move_val = 50
                print("move value", move_val)
                self.make_move(index, board, player_marker)
                best_val = max(best_val, move_val)
            print("best_value", best_val)
            print(board, "board")
            return best_val

        if player_marker == 1: 
            best_val = 50 
            available_moves = self.get_available_moves(board)

            for move in available_moves: 
                index = super(Computer, self).find_index_of_move(board)
                print("index", index)
                x_moves, o_moves = super(Computer, self).all_moves(board)
                player_marker = super(Computer, self).set_player_marker(x_moves, o_moves)
                print(player_marker, "player marker")
                move_val = self.minimax(board, depth - 1, player_marker)
                move_val = -50
                print("move value", move_val)
                self.make_move(index, board, player_marker)
                best_val = min(best_val, move_val)
            print("best value", best_val)
            print(board, "board")
            return best_val

    def take_best_move(self, board, depth, player_marker): 
        available_moves = self.get_available_moves(board)
        neutral_val = 0 
        choices = []

        for move in available_moves: 
            print("hey begin")
            index = super(Computer, self).find_index_of_move(board)
            x_moves, o_moves = super(Computer, self).all_moves(board)
            player_marker = super(Computer, self).set_player_marker(x_moves, o_moves)
            self.make_move(index, board, player_marker)
            move_val = self.minimax(board, depth - 1, player_marker)
            print("hey")

            if move_val > neutral_val: 
                choices = [move]
            elif move_val == neutral_val: 
                choices.append(move)
        print("choices: ", choices)

        if len(choices) > 0: 
            print("hi")
            move = random.choice(choices)
            print("best move", move)
            return move

        else: 
            print("hello")
            move = random.choice(available_moves)
            print("random move", move)
            return move


if __name__ == "__main__": 
    a = Computer()
    board = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    depth = 9
    player_marker = 1
    index = 1
    a.minimax(board, depth, player_marker)
    a.take_best_move(board, depth, player_marker)


import random

class Computer(object):

    def __init__(self, marker):
        self.name = "Computer"
        self.marker = marker
        self.num_board = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    def make_move(self, board, difficulty): 
       if difficulty == 1: 
           move = self.get_novice_move(board)
       elif difficulty == 2: 
           move = self.get_intermediate_move(board)
       elif difficulty == 3: 
           move = self.get_master_move(board)
       board[move - 1] = self.marker 

    def get_open_positions(self, board): 
       open_positions = []
       for i in range(0, len(board)): 
           if board[i] == 0: 
               open_positions.append(i + 1)
       return open_positions

    def is_game_over(self, board, depth):
       available_moves = self.get_open_positions(board)
       if self.x_win(board) == True: 
           return True
       if self.o_win(board) == True:
           return True
       if len(available_moves) == 0: 
           return True

    def make_next_move(self, move, board, marker):
        index = move - 1
        board[index] = marker

    def x_win(self, board): 
       pass

    def o_win(self, board): 
        pass

    def score_game(self, board):
       if self.x_win(board) == True: 
           return 10 
       if self.o_win(board) == True: 
           return -10 
       else: 
           return 0

    def change_marker(self, player_marker): 
        if player_marker == 1: 
            return 2
        else:
            return 1

    def minimax(self, board, depth, player_marker): 
        moves = self.get_open_positions(board)

        if self.is_game_over(board, depth) == True: 
            score = self.score_game(board)
            return score

        if player_marker == 1: 
            moves = self.get_open_positions(board)
            best_score = -10
            for move in moves: 
                self.make_next_move(move, board, player_marker)
                move_score = self.minimax(board, depth + 1, self.change_marker(player_marker))
                self.make_next_move(move, board, 0)
                best_score = max(best_score, move_score)
            return best_score

        if player_marker == 2: 
            moves = self.get_open_positions(board)
            best_score = 10 
            for move in moves: 
                self.make_next_move(move, board, player_marker)
                move_score = self.minimax(board, depth + 1, self.change_marker(player_marker))
                self.make_next_move(move, board, 0)
                best_score = min(best_score, move_score)
            return best_score

    def best_move(self, board, depth, player_marker): 
        moves = self.get_open_positions(board)
        choices = []
        for move in moves: 
            self.make_next_move(move, board, player_marker)
            move_score = self.minimax(board, depth + 1, self.change_marker(player_marker))
            self.make_next_move(move, board, 0)
            if player_marker == 1: 
                if move_score == 10: 
                    choices = move
                    return choices
                if move_score > 0: 
                    choices = [move]
                elif move_score == 0: 
                    choices.append(move)
            else: 
                if move_score == -10: 
                    choices = move
                    return choices
                if move_score < 0: 
                    choices = [move]
                elif move_score == 0: 
                    choices.append(move)
        if len(choices) > 0: 
            return random.choice(choices)
        else: 
            return random.choice(moves)

    def get_novice_move(self, board): 
        open_positions = self.get_open_positions(board)
        move = random.choice(open_positions)
        return move

    def get_intermediate_move(self, board): 
        num_board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        winning_moves = self.get_possible_win_combos(board)
        blocking_moves = self.get_possible_lose_combos(board)
        open_positions = self.get_open_positions(board)
        if len(winning_moves) > 0: 
            move = random.choice(winning_moves)
            if move in open_positions: 
                return move
            else: 
                return self.get_intermediate_move(board)
        elif len(blocking_moves) > 0: 
            move = random.choice(blocking_moves)
            if move in open_positions: 
                return move
            else: 
                return self.get_intermediate_move()
        else: 
            move = random.choice(open_positions)
            return move

    def get_master_move(self, board): 
        player_marker = self.marker 
        depth = 0
        move = self.best_move(board, depth, player_marker)
        return move

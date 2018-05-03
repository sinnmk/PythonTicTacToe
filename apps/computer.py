import random

class Computer(object):

    def __init__(self, marker):
        self.num_board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.win_combos = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
        self.name = "Computer"
        #set difficulty
        self.marker = marker

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

    def make_intermediate_move(self, board): 
        winning_moves = self.get_possible_win_combos(board)
        blocking_moves = self.get_possible_lose_combos(board)
        open_positions = self.get_open_positions(board)
        if len(winning_moves) > 0: 
            move = random.choice(winning_moves)
            board[move - 1] = self.marker
        if len(blocking_moves) > 0: 
            move = random.choice(blocking_moves)
            board[move - 1] = self.marker
        move = random.choice(self.num_board)
        if move in open_positions: 
            board[move - 1] = self.marker
        else: 
            return self.get_move(board)

    def make_move(self, board): 
       available_moves = self.get_open_positions(board)
       move = random.choice(available_moves)
       board[move - 1] = self.marker 
#---------------------------------------------------------------------------------------------------------------------------
    def get_open_positions(self, board): 
       open_positions = []
       for i in range(0, len(board)): 
           if board[i] == 0: 
               open_positions.append(i + 1)
       return open_positions

    def is_game_over(self, new_board):
       available_moves = self.get_open_positions(new_board)
       if len(available_moves) == 0: 
          return True

    def is_win(self, new_board, marker): 
       win_combos = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
       for i in win_combos:
          if new_board[i[0]] == marker and new_board[i[1]] == marker and new_board[i[2]] == marker:
              return True

    def score_game(self, new_board):
       if self.is_win(new_board, marker = 1) == True: 
           score = 10
       elif self.is_win(new_board, marker = 2) == True: 
           score = -10
       else: 
           score = 0
       return score

    def make_next_move(self, move, new_board, marker):
        index = move - 1
        new_board[index] = marker
        best_move = []

    def minimax(self, board, depth, marker):
        print("beginning of minimax")
        new_board = board[:]
        best_score = []
        best_move = []

        if self.is_game_over(new_board) == True: 
           best_score = self.score_game(new_board)
           print("GAME IS OVER:")
           print("SCORE:", best_score, "PLAYER:", marker)
           print(board)
           print(best_move)
            
        if depth % 2 == 0: 
            marker = 1
        elif depth % 2 == 1:  
            marker = 2

        #maximizing player: X
        if marker == 1: 
            best_value = -10
            moves = self.get_open_positions(new_board)
            for move in moves:
                self.make_next_move(move, new_board, marker)
                move_value = self.minimax(new_board, depth + 1, marker)  
                best_value = max(move_value, best_value)
                self.make_next_move(move, new_board, marker = 0)
                print("x move:", move, "marker:", marker)
            return best_value

        #minimizing player: O
        if marker == 2:  
            best_value = 10
            moves = self.get_open_positions(new_board)
            for move in moves: 
                self.make_next_move(move, new_board, marker)
                move_value = self.minimax(new_board, depth + 1, marker) 
                best_value = min(move_value, best_value)
                self.make_next_move(move, new_board, marker = 0)
                print("o move:", move, "marker:", marker)
            return best_value

if __name__ == "__main__":
    a = Computer(marker = 1)
    marker = 1
    board = [1, 0, 1, 2, 1, 2, 2, 0 , 0]
    depth = 6 
    a.minimax(board, depth, marker)












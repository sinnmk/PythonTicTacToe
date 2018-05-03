import random

class Computer(object):

    def __init__(self, marker):
        self.num_board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.win_combos = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
        self.name = "Computer"
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
       if self.x_win(new_board) == True: 
           return True
       if self.o_win(new_board) == True:
           return True

    def x_win(self, new_board): 
       win_combos = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
       for i in win_combos:
           if new_board[i[0]] == 1 and new_board[i[1]] == 1 and new_board[i[2]] == 1:
              return True

    def o_win(self, new_board): 
       win_combos = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
       for i in win_combos:
           if new_board[i[0]] == 2 and new_board[i[1]] == 2 and new_board[i[2]] == 2:
              return True

  #  def score_game(self, new_board):
  #     if self.x_win(new_board) == True: 
  #         score = 10  
  #         return score
  #     if self.o_win(new_board) == True: 
  #         score = -10 
  #         return score
  #     if self.x_win(new_board) == False and self.o_win(new_board) == False: 
  #         score = 0
  #         return score

    def make_next_move(self, move, new_board, marker):
        index = move - 1
        new_board[index] = marker

    def minimax(self, board, depth, marker):
        new_board = board[:]

        if depth % 2 == 0: 
            marker = 1
        elif depth % 2 == 1:  
            marker = 2

        if depth == 9 or self.is_game_over(new_board): 
           if self.x_win(new_board) == True: 
               return 10
           if self.o_win(new_board) == True: 
               return -10
           if self.x_win(new_board) == False and self.o_win(new_board) == False: 
               return 0

        if marker == 1: 
            best_value = -10
            moves = self.get_open_positions(new_board)
            for move in moves:
                self.make_next_move(move, new_board, marker)
                move_value = self.minimax(new_board, depth + 1, marker)  
                best_value = max(move_value, best_value)
                self.make_next_move(move, new_board, marker = 0)
            return best_value

        if marker == 2:  
            best_value = 10
            moves = self.get_open_positions(new_board)
            for move in moves: 
                self.make_next_move(move, new_board, marker)
                move_value = self.minimax(new_board, depth + 1, marker) 
                best_value = min(move_value, best_value)
                self.make_next_move(move, new_board, marker = 0)
            return best_value

    def best_move(self, board, depth, marker): 
        draw = 0
        choices = []
        best_choices = []
        moves = self.get_open_positions(board)
        for move in moves:
            self.make_next_move(move, board, marker)
            move_value = self.minimax(board, depth + 1, marker) 
            self.make_next_move(move, board, marker = 0)
            if move_value > draw: 
                best_choices.append(move)
                return best_choices[0]
            elif move_value == draw: 
                choices.append(move)
        print("choices", choices)
        print("best_choices", best_choices)
                
        if len(choices) > 0: 
            move = random.choice(choices)
            return move
        else: 
            move = random.choice(moves)
            return move

if __name__ == "__main__":
    a = Computer(marker = 1)
    marker = 1
    board = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    depth = 0 
    a.best_move(board, depth, marker)












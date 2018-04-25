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

    def board_is_terminal(self, new_board):
        i = 0
        if self.x_win(new_board) == True: 
            return True
        elif self.o_win(new_board) == True: 
            return True
        elif all(board) != 0: 
            return True
        while i < len(new_board): 
            for num in board: 
                if board[i] == 0: 
                    return False
                i += 1

  #  def get_move(self, board): 
  #      open_positions = self.get_open_positions(board)
  #      for num in open_positions: 
  #          return num 

  #  def minimax(self, board, depth, player_marker):
  #      new_board = board[:]
  #      draw_val = 0 
  #      choices = []

  #      if self.board_is_terminal == True or depth == 3: 
  #          if self.x_win(board) == True: 
  #              print("x_win -100")
  #              return -100
  #          elif self.o_win(board) == True: 
  #              print("o_Win 100")
  #              return 100 
  #          else: 
  #              print("draw 0")
  #              return 0

  #      '''maximizing player (o)'''
  #      if player_marker == 2: 
  #          print("player 2")
  #          best_val = -100
  #          available_moves = self.get_open_positions(board)

  #          for move in available_moves: 
  #              index = super(Computer, self).find_index_of_move(board)
  #              x_moves, o_moves = super(Computer, self).all_moves(board)
  #              player_marker = super(Computer, self).set_player_marker(x_moves, o_moves)
  #              super(Computer, self).make_move(index, board, player_marker)
  #              print(board)
  #              #-------------------  
  #              move_val = self.minimax(board, depth - 1, player_marker)
  #              #-------------------
  #              best_val = max(best_val, move_val)
  #          print(best_val, "best val for o")
  #          return best_val

  #      '''minimizing player (x)'''
  #      if player_marker == 1:  
  #          print("player 1")
  #          best_val = 100 
  #          available_moves = self.get_open_positions(board)

  #          for move in available_moves: 
  #              index = super(Computer, self).find_index_of_move(board)
  #              x_moves, o_moves = super(Computer, self).all_moves(board)
  #              player_marker = super(Computer, self).set_player_marker(x_moves, o_moves)
  #              super(Computer, self).make_move(index, board, player_marker)
  #              print(board, "new_board")
  #              #------------------------
  #              move_val = self.minimax(board, depth - 1, player_marker)
  #              #-------------------------
  #              best_val = min(best_val, move_val)
  #          print(best_val, "best val for x")
  #          return best_val

  #  def best_move(self): 
  #      available_moves = self.get_open_positions(board)
  #      for move in available_moves: 
  #          index = super(Computer, self).find_index_of_move(board)
  #          x_moves, o_moves = super(Computer, self).all_moves(board)
  #          player_marker = super(Computer, self).set_player_marker(x_moves, o_moves)
  #          super(Computer, self).make_move(index, board, player_marker)
  #          move_val = self.minimax(board, depth - 1, player_marker)
  #          
  #          if move_val > draw_val: 
  #              choices = move 
  #          elif move_val == draw_val: 
  #              choices.append(move)

  #          print(choices, "choices")

  #          if len(choices) > 0: 
  #              move = random.choice(choices)
  #              print(move)
  #              return move 
  #          else: 
  #              move = random.choice(available_moves)
  #              print(move)
  #              return move

#if __name__ == "__main__": 
#    a = Computer()
#    board = [0, 0, 0, 0, 0, 0, 0, 0, 0]
#    depth = 9 
#    player_marker = 1 
#    a.best_move()
    


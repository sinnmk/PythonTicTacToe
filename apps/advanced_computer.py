
   # def get_possible_win_combos(self, board):
   #     winning_moves = []
   #     for i in self.win_combos:
   #         if board[i[0]] == 1 and board[i[1]] == 1 and board[i[2]] == 0:
   #             move = self.num_board[i[2]]
   #             winning_moves.append(move)
   #         if board[i[0]] == 0 and board[i[1]] == 1 and board[i[2]] == 1:
   #             move = self.num_board[i[0]]
   #             winning_moves.append(move)
   #         if board[i[0]] == 1 and board[i[1]] == 0 and board[i[2]] == 1:
   #             move = self.num_board[i[1]]
   #             winning_moves.append(move)
   #     return winning_moves

   # def get_possible_lose_combos(self, board):
   #     blocking_moves = []
   #     for i in self.win_combos:
   #         if board[i[0]] == 2 and board[i[1]] == 2 and board[i[2]] == 0:
   #             move = self.num_board[i[2]]
   #             blocking_moves.append(move)
   #         if board[i[0]] == 0 and board[i[1]] == 2 and board[i[2]] == 2:
   #             move = self.num_board[i[0]]
   #             blocking_moves.append(move)
   #         if board[i[0]] == 2 and board[i[1]] == 0 and board[i[2]] == 2:
   #             move = self.num_board[i[1]]
   #             blocking_moves.append(move)
   #     return blocking_moves

   # def make_intermediate_move(self, board): 
   #     winning_moves = self.get_possible_win_combos(board)
   #     blocking_moves = self.get_possible_lose_combos(board)
   #     open_positions = self.get_open_positions(board)
   #     if len(winning_moves) > 0: 
   #         move = random.choice(winning_moves)
   #         board[move - 1] = self.marker
   #     if len(blocking_moves) > 0: 
   #         move = random.choice(blocking_moves)
   #         board[move - 1] = self.marker
   #     move = random.choice(self.num_board)
   #     if move in open_positions: 
   #         board[move - 1] = self.marker
   #     else: 
   #         return self.get_move(board)

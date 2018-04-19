class Minimax(object):

    def __init__(self): 
        self.win_combos = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
        self.game_running = True
        self.game_engine = GameEngine()
        self.computer = Computer()
        self.human = Human()
        self.scores = []
        self.counter = 0

    def is_moves_left(self, board): 
        for i in board: 
            if i == 0: 
                return True
            else: 
                return False

    def get_available_moves(self, board): 
        available_moves = [index for index, value in enumerate(board) if value == 0]
        return available_moves

    def x_win(self, board):
        for i in self.win_combos:
            if board[i[0]] == 1 and board[i[1]] == 1 and board[i[2]] == 1:
                print("x_win")
                self.game_running = False
                return True

    def o_win(self, board):
        for i in self.win_combos:
            if board[i[0]] == 2 and board[i[1]] == 2 and board[i[2]] == 2:
                print("o_win")
                self.game_running = False
                return True

    def minimax(self, board, depth, is_max_player):
        empty_positions = self.get_available_moves(board)

        if self.game_running == False or depth == 9: 
            return  
        
        if is_max_player == True: 

            best_score = -10 
            self.game_engine.take_turn(self.computer)
           # for i in board: 
           #     if len(empty_positions) > 0 and i == 0: 
           #         print(board[i], "i")
           #         move = self.get_index(board)
           #         print(move, "move")
           #         board[i] = move
           #         print(empty_positions[0])
            score = self.minimax(board, depth + 1, False)
            print(score, "max score")
            best_score = max(best_score, score)
            print(board)
            print(best_score, "max best score")
            return best_score

        else: 

            best_score = 10
            self.game_engine.take_turn(self.computer)
           # for i in board: 
           #     score = self.minimax(board, depth + 1, True)
           #     best_score = min(best_score, score)

            print(board)
            print(best_score, "min best score")
            return best_score
            
if __name__ == "__main__": 
    a = Minimax()
    board = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    is_max_player = True
    depth = 0
    a.score_board(board)
    a.get_available_moves(board)
    a.minimax(board, depth, is_max_player)


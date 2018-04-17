import math

class Minimax(object):

    def __init__(self):
        self.scores = []

    def evaluate_win_state(self, board):
        win_combos = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
        for i in win_combos:
            if board[i[0]] == player_num and board[i[1]] == player_num and board[i[2]] == player_num:
                return True
            else: 
                return False

    def get_open_positions(self, game_state):
        copy_board = board[:]
        open_positions = []
        i = 0
        while i < len(board):
            for digit in game_state:
                if board[i] == 0:
                    open_positions.append(i + 1)
                if board[i] != 0:
                    open_positions.append("")
                i += 1
        return open_positions

    def payoff(self): 
        win = self.evaluate_win_state(game_state)
        if win == True: 
            score = math.inf - depth
            self.scores.append(score)
        elif win == False: 
            score = -math.inf - depth
            self.scores.append(score)
        else: 
            score = 0
            self.scores.append(score)

    def minimax(self, game_state, depth, maximizing_player):
        if depth == 0 or self.evaluate_win_state(game_state) == True: 
            return self.payoff() 

        if maximizing_player: 
            best_value = -math.inf
            for move in game_state: 
                value = self.minimax(game_state, depth - 1, True)
                best_value = max(best_value, value)
            return best_value

        else:
            best_value = math.inf
            for move in game_state: 
                value = self.minimax(game_state, depth - 1, False)
                best_value = min(best_value, value)
            return best_value

    def run_minimax(self): 
        pass

if __name__ == "__main__":
    a = Minimax()
    game_state = [0, 1, 2, 2, 2, 0, 0, 1, 1]
    depth = 4 
    maximizing_player = True
    a.minimax(game_state, depth, maximizing_player)


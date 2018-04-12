from player import Player
from human import Human
from computer import Computer

class Minimax(object): 

    #Rename class????

    def __init__(self): 
        self.human = Human()
        self.computer = Computer()
        self.win_combos = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))

    def evaluate_win_state(self, board):

        #NOT COMPLETED

        # this function should evaluate each possible future board state's possibility of win

        # find a way to use the check for win function to avoid duplication


        for i in self.win_combos:
            if board[i[0]] == 2 and board[i[1]] == 2 and board[i[2]] == 2:
                return True

            if board[i[0]] == 1 and board[i[1]] == 1 and board[i[2]] == 1:
                return True


    def future_board_states(self, board): 
        #NOT COMPLETED

        #need to figure out how to create a list of all future board states based of of the most recent turn/player 

        #then pass all board states that include all future x and o moves to evaluate win and to check for terminal states

        #needs to then score the move based on the outcome of the move: win 10, lose -10, draw 0

        #then choose best move with choosing the maximized score's move for x and minimized score's move for o(separate in different function?)
        i = 0
        j = 0
        new_board = board[:]
        board_states = []
        while j < len(new_board): 
            if new_board[j] == 0: 
                new_board[j] = 1
                board_states.append(new_board)
            new_board = board[:]
            j += 1
        while i < len(new_board): 
            if new_board[i] == 0: 
                new_board[i] = 2 
                board_states.append(new_board)
            new_board = board[:]
            i += 1
        print(board_states)

    def score_board(self): 

        #this function will take the future board states and score them according to the win or lose outcome after passed through the evaluate win function

        score = []
        if self.evaluate_win_state(board) == True: 
            score.append(10)
            print(score)
            return score
        if self.evaluate_win_state(board) == False: 
            score.append(-10)
            print(score)
            return score
        if self.evaluate_win_state(board) != True and self.evaluate_win_state(board) != False: 
            score.append(0)
            return score

    def return_best_move(self): 
        pass

if __name__ == "__main__": 
    a = Minimax()
    board = [1, 0, 0, 1, 1, 0, 0, 1, 0]
    a.future_board_states(board)
    a.score_board()


            

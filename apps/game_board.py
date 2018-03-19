import numpy as np
import random
from user_interface import UserInterface

class GameBoard(object): 
    
    def __init__(self): 
        self.user_interface = UserInterface()

        self.board = np.array([[0, 0, 0],
                          [0, 0, 0],
                          [0, 0, 0]])

    def create_board(self): 

        num_board = np.array([[1, 2, 3],
                              [4, 5, 6], 
                              [7, 8, 9]])
        return num_board

    def empty_slots(self): 
        open_slots = []
        bool_arr = (self.board == 0)
        flat_bool_arr = bool_arr.flatten()

        for i in range(0, len(flat_bool_arr)): 
            if flat_bool_arr[i] == True: 
                open_slots.append(i + 1)
        return open_slots

    def place_o(self): 
        index = self.find_index_of_user_move()
        self.board[index] = 1 

    def place_x(self): 
        index = self.find_index_of_comp_move()
        self.board[index] = 2

    def display_board(self): 
        board_list = []
        game_board = self.board.flatten()

        for i in range(0, 9): 
            if game_board[i] == 1: 
                board_list.append('X')
            elif game_board[i] == 2: 
                board_list.append('O')
            elif game_board[i] == 0: 
                board_list.append(' ')
            else: 
                raise Exception("This is not a valid entry")
        print("""
         {} | {} | {}
        ---+---+---
         {} | {} | {}
        ---+---+---
         {} | {} | {}
        """.format(*board_list))
        return game_board

    def user_move(self):
        empty_slots = self.empty_slots()
        user_move = self.user_interface.get_game_move()
        user_move = int(user_move)
        if user_move in empty_slots: 
            return user_move
        else: 
            print("That is not an open position. ")
            return self.user_move()

    def comp_move(self): 
        empty_slots = self.empty_slots()
        comp_move = random.choice(empty_slots)
        return comp_move

    def find_index_of_user_move(self): 
        user_move = self.user_move()
        board = self.create_board()  
        index = np.where(board == user_move)
        board[index] = user_move
        return index

    def find_index_of_comp_move(self): 
        comp_move = self.comp_move()
        board = self.create_board()
        index = np.where(board == comp_move)
        board[index] = comp_move
        return index

    def check_for_win(self): 
        board = self.display_board()
        if board[0] == board[1] == board[2] == 1: 
            game_running = False
            print("P1 wins!")
        elif board[0] == board[1] == board[2] == 2: 
            game_running = False
            print("P2 wins!")

        if board[3] == board[4] == board[5] == 1: 
            print("P1 wins!")
            quit()
        elif board[3] == board[4] == board[5] == 2: 
            print("P2 wins!")
            quit()

        if board[6] == board[7] == board[8] == 1: 
            print("P1 wins!")
            quit()
        elif board[6] == board[7] == board[8] == 2: 
            print("P2 wins!")
            quit()
                    
        if board[0] == board[3] == board[6] == 1: 
            print("P1 wins!")
            quit()
        elif board[0] == board[3] == board[6] == 2: 
            print("P2 wins!")
            quit()
            
        if board[1] == board[4] == board[7] == 1: 
            print("P1 wins!")
            quit()
        elif board[1] == board[4] == board[7] == 2: 
            print("P2 wins!")
            quit()

        if board[2] == board[5] == board[8] == 1: 
            print("P1 wins!")
            quit()
        elif board[2] == board[5] == board[8] == 2: 
            print("P2 wins!")
            quit()

        if board[2] == board[4] == board[6] == 1: 
            print("P1 wins!")
            quit()
        elif board[2] == board[4] == board[6] == 2: 
            print("P2 wins!")
            quit()

        if board[0] == board[4] == board[8] == 1: 
            print("P1 wins!")
            quit()
        elif board[0] == board[4] == board[8] == 2: 
            print("P2 wins!")
            quit()


        
    



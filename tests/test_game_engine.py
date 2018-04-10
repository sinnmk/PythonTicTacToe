import unittest
from unittest.mock import patch, Mock
from apps.game_engine import GameEngine

class TestGameEngine(unittest.TestCase): 

    def setUp(self): 
        self.game_engine = GameEngine()

    def test_display_blank_board(self): 
        board = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        modified_board = self.game_engine.modify_game_board_list(board)
        self.assertEqual(modified_board, [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '])

    def test_modify_board(self):
        board =[1, 1, 2, 2, 0, 0, 0, 0, 0]
        modified_board = self.game_engine.modify_game_board_list(board)
        self.assertEqual(modified_board, ['X', 'X', 'O', 'O', ' ', ' ', ' ', ' ', ' '])

    def test_x_can_win(self): 
        board = [1, 1, 1, 0, 0, 0, 0, 0, 0]
        x_win = self.game_engine.x_win(board)
        self.assertEqual(x_win, True)

    def test_x_no_win(self): 
        board = [0, 1, 0, 0, 0, 0, 2, 0, 0]
        no_win = self.game_engine.x_win(board)
        self.assertEqual(no_win, False)

    def test_o_can_win(self): 
        board = [2, 2, 2, 0, 0, 0, 0, 0, 0]
        o_win = self.game_engine.o_win(board)
        self.assertEqual(o_win, True)

    def test_o_no_win(self): 
        board = [0, 2, 0, 0, 0, 0, 1, 0, 0]
        no_win = self.game_engine.o_win(board)
        self.assertEqual(no_win, False)







        


        
        

        

        

        







        

    
        

        
        




        
    



        
        
    




        

        
        
    
        



        
        



    

    


    

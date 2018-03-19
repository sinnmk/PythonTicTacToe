import unittest
from apps.game_engine import GameEngine
from apps.game_board import GameBoard

class TestGameEngine(unittest.TestCase): 

    def setUp(self): 
        self.game_engine = GameEngine()
        self.game_board = GameBoard()

    def test_for_win_index_0_1_2_position(self): 
        win = self.game_engine.check_for_win()
        board = self.game_board.display_board()
        board[0] == 1
        board[1] == 1
        board[3] == 1
        self.assertEqual(win, True)




    


    

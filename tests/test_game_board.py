import unittest
from apps.game_board import GameBoard

class TestGameBoard(unittest.TestCase): 

    def setUp(self): 
        self.game_board = GameBoard()

    def test_can_get_empty_board(self): 
        board = self.game_board.display_board()
        self.assertEqual(board.all(), 0)

    def test_can_change_empty_board(self): 
        board = self.game_board.display_board()
        board[0] = 1
        self.assertEqual(board.any(), 1)




        

    


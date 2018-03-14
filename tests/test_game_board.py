import unittest
from apps.game_board import GameBoard

class TestGameBoard(unittest.TestCase): 

    def setUp(self): 
        self.game_board = GameBoard()

    def test_can_create_board(self): 
        board = self.game_board.create_new_board()
        self.assertEqual(board.all(), 0)

    


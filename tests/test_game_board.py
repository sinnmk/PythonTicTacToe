import unittest
from apps.game_board import GameBoard

class TestGameBoard(unittest.TestCase): 

    def setUp(self): 
        self.game_board = GameBoard()

    def test_can_place_o(self): 
        place_o = self.game_board.check_for_win()
        board = self.game_board.display_board()
        board[0] = 1
        board[1] = 1
        board[2] = 1
        self.assertEqual(board, ([1, 1, 1, 0, 0, 0, 0, 0, 0]))

    


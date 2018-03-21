import unittest
from unittest.mock import Mock
import numpy as np
import random
from apps.game_board import GameBoard

class TestGameBoard(unittest.TestCase): 

    def setUp(self): 
        self.game_board = GameBoard()

    def test_can_create_num_board(self): 
        numpy_board = self.game_board.create_board()
        board_list = numpy_board.flatten()
        self.assertEqual(len(board_list), 9)

    def test_can_create_placeholder_board(self): 
        board = self.game_board.display_board()
        self.assertEqual(board.all(), 0)

    def test_can_change_empty_board_to_x(self): 
        board = self.game_board.display_board()
        board[0] = 1
        self.assertEqual(board.any(), True)

    def test_can_change_empty_board_to_o(self): 
        board = self.game_board.display_board()
        board[0] = 2
        self.assertEqual(board.any(), True)

    def test_can_display_board(self): 
        board = self.game_board.display_board()
        self.assertEqual(len(board), 9)

    def test_can_return_comp_move(self): 
        random.seed(1)
        move = self.game_board.comp_move()
        self.assertEqual(move, 3)

    def test_can_return_user_move(self): 
        move = self.game_board.user_move()
        self.assertEqual(move, 2)

   # def test_check_For_row_win(self): 
   #     board = self.game_board.display_board()
   #     win = self.game_board.check_for_win()
   #     board[0] = 1
   #     board[1] = 1
   #     board[2] = 1
   #     self.assertEqual(win , "Player one wins!")





        

    


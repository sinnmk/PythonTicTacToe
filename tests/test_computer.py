from apps.computer import Computer
import unittest

class TestComputer(unittest.TestCase): 

    def setUp(self): 
        self.computer = Computer(marker = 1)

    def test_get_best_move_with_board_empty_starting_board(self): 
        board = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        depth = 6
        marker = 1
        best_move = self.computer.best_move(board, depth, marker)
        self.assertEqual(best_move, 1)

    def test_get_best_move_with_board_100112220_depth_6_marker_1(self): 
        board = [1, 0, 0, 1, 1, 2, 2, 2, 0]
        depth = 6
        marker = 1
        best_move = self.computer.best_move(board, depth, marker)
        self.assertEqual(best_move, 9)

    def test_get_best_move_with_board_011022102_depth_6_marker_1(self): 
        board = [0, 1, 1, 0, 2, 2, 1, 0, 2]
        depth = 6
        marker = 1
        best_move = self.computer.best_move(board, depth, marker)
        self.assertEqual(best_move, 1)

    def test_get_best_move_with_board_110020221_depth_6_marker_1(self): 
        board = [1, 1, 0, 0, 2, 0, 2, 2, 1]
        depth = 6
        marker = 1
        best_move = self.computer.best_move(board, depth, marker)
        self.assertEqual(best_move, 3)
        
    def test_get_best_move_with_board_210112002_depth_6_marker_1(self): 
        board = [2, 1, 0, 1, 1, 2, 0, 0, 2]
        depth = 6
        marker = 1
        best_move = self.computer.best_move(board, depth, marker)
        self.assertEqual(best_move, 3)

    def test_get_best_move_with_board_102022011_depth_6_marker_1(self): 
        board = [1, 0, 2, 0, 2, 2, 0, 1, 1]
        depth = 6
        marker = 1
        best_move = self.computer.best_move(board, depth, marker)
        self.assertEqual(best_move, 7)
        
    def test_get_best_move_with_board_122012010_depth_6_marker_1(self): 
        board = [1, 2, 2, 0, 1, 2, 0, 1, 0]
        depth = 6
        marker = 1
        best_move = self.computer.best_move(board, depth, marker)
        self.assertEqual(best_move, 9)

    def test_get_best_move_with_board_002012001_depth_4_marker_1(self): 
        board = [0, 0, 2, 0, 1, 2, 0, 0, 1]
        depth = 4
        marker = 1
        best_move = self.computer.best_move(board, depth, marker)
        self.assertEqual(best_move, 1)

    def test_get_best_move_with_board_110220000_depth_4_marker_1(self): 
        board = [1, 1, 0, 2, 2, 0, 0, 0, 0]
        depth = 4
        marker = 1
        best_move = self.computer.best_move(board, depth, marker)
        self.assertEqual(best_move, 3)

    def test_get_best_move_with_board_002010201_depth_4_marker_1(self): 
        board = [0, 0, 2, 0, 1, 0, 2, 0, 1]
        depth = 4
        marker = 1
        best_move = self.computer.best_move(board, depth, marker)
        self.assertEqual(best_move, 1)

    def test_get_best_move_with_board_002010201_depth_4_marker_1(self): 
        board = [1, 0, 0, 1, 1, 2, 0, 2, 0]
        depth = 4
        marker = 1
        best_move = self.computer.best_move(board, depth, marker)
        self.assertEqual(best_move, 2) 
        
    @unittest.skip
    def test_get_best_move_with_board_002010201_depth_2_marker_1(self): 
        board = [1, 2, 0, 0, 0, 0, 0, 0, 0]
        depth = 2
        marker = 1
        best_move = self.computer.best_move(board, depth, marker)
        self.assertEqual(best_move, 5) 



    


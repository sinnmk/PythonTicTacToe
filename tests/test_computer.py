from apps.computer import Computer
import unittest

class TestComputer(unittest.TestCase): 

    def setUp(self): 
        self.computer = Computer(marker = 1)

    def test_TWO_get_best_move_with_board_100112220_depth_6_marker_1(self): 
        board = [1, 0, 0, 1, 1, 2, 2, 2, 0]
        depth = 6
        marker = 1
        best_move = self.computer.best_move(board, depth, marker)
        self.assertEqual(best_move, 9)

    def test_THREE_get_best_move_with_board_011022102_depth_6_marker_1(self): 
        board = [0, 1, 1, 0, 2, 2, 1, 0, 2]
        depth = 6
        marker = 1
        best_move = self.computer.best_move(board, depth, marker)
        self.assertEqual(best_move, 1)

    def test_FOUR_get_best_move_with_board_110020221_depth_6_marker_1(self): 
        board = [1, 1, 0, 0, 2, 0, 2, 2, 1]
        depth = 6
        marker = 1
        best_move = self.computer.best_move(board, depth, marker)
        self.assertEqual(best_move, 3)
        
    def test_FIVE_get_best_move_with_board_210112002_depth_6_marker_1(self): 
        board = [2, 1, 0, 1, 1, 2, 0, 0, 2]
        depth = 6
        marker = 1
        best_move = self.computer.best_move(board, depth, marker)
        self.assertEqual(best_move, 8)

    def test_SIX_get_best_move_with_board_102022011_depth_6_marker_1(self): 
        board = [1, 0, 2, 0, 2, 2, 0, 1, 1]
        depth = 6
        marker = 1
        best_move = self.computer.best_move(board, depth, marker)
        self.assertEqual(best_move, 7)

    def test_SEVEN_get_best_move_with_board_122012010_depth_6_marker_1(self): 
        board = [1, 2, 2, 0, 1, 2, 0, 1, 0]
        depth = 6
        marker = 1
        best_move = self.computer.best_move(board, depth, marker)
        self.assertEqual(best_move, 9)
    
    def test_EIGHT_get_best_move_with_board_002012001_depth_4_marker_1(self): 
        board = [0, 0, 2, 0, 1, 2, 0, 0, 1]
        depth = 4
        marker = 1
        best_move = self.computer.best_move(board, depth, marker)
        self.assertEqual(best_move, 1)

    def test_NINE_get_best_move_with_board_110220000_depth_4_marker_1(self): 
        board = [1, 1, 0, 2, 2, 0, 0, 0, 0]
        depth = 4
        marker = 1
        best_move = self.computer.best_move(board, depth, marker)
        self.assertEqual(best_move, 3)

    @unittest.skip
    def test_TEN_get_best_move_with_board_002010201_depth_4_marker_1(self): 
        board = [0, 0, 2, 0, 1, 0, 2, 0, 1]
        depth = 4
        marker = 1
        best_move = self.computer.best_move(board, depth, marker)
        self.assertEqual(best_move, 1)

    @unittest.skip
    def test_ELEVEN_get_best_move_with_board_002010201_depth_4_marker_1(self): 
        board = [1, 0, 0, 1, 1, 2, 0, 2, 0]
        depth = 4
        marker = 1
        best_move = self.computer.best_move(board, depth, marker)
        self.assertEqual(best_move, 2) 

    def test_TWELVE_get_best_move_with_board_121200000_depth_4_marker_1(self): 
        board = [1, 2, 1, 2, 0, 0, 0, 0, 0]
        depth = 4
        marker = 1
        best_move = self.computer.best_move(board, depth, marker)
        self.assertEqual(best_move, 5) 

    def test_get_best_move_with_board_120000000_depth_2_marker_1(self): 
        board = [1, 2, 0, 0, 0, 0, 0, 0, 0]
        depth = 2
        marker = 1
        best_move = self.computer.best_move(board, depth, marker)
        self.assertEqual(best_move, 4) 



    


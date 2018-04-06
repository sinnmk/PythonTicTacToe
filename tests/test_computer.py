from apps.computer import Computer
import unittest

class TestComputer(unittest.TestCase): 

    def setUp(self): 
        self.computer = Computer()

    def test_set_name(self): 
        name = self.computer.set_name()
        self.assertEqual(name, "Computer")

    def test_make_move_based_on_empty_spots_left(self): 
        board = [1, 1, 2, 2, 0, 1, 1, 2, 2]
        move = self.computer.make_move(board) 
        self.assertEqual(move, 5)

    def test_computer_can_get_possible_1_2_3_horizontal_win(self): 
        board = [1, 1, 0, 0, 0, 0, 0, 0, 0]
        possible_win_combo = self.computer.get_possible_win_combos(board)
        self.assertEqual(possible_win_combo, [3])

    def test_computer_can_get_possible_4_5_6_horizontal_win(self):
        board = [0, 0, 0, 1, 1, 0, 0, 0, 0]
        possible_win_combo = self.computer.get_possible_win_combos(board)
        self.assertEqual(possible_win_combo, [6]) 
        
    def test_computer_can_get_possible_7_8_9_horizontal_win(self):
        board = [0, 0, 0, 0, 0, 0, 1, 1, 0]
        possible_win_combo = self.computer.get_possible_win_combos(board)
        self.assertEqual(possible_win_combo, [9]) 

    def test_computer_can_get_possible_1_4_7_vertical_win(self):
        board = [1, 0, 0, 1, 0, 0, 0, 0, 0]
        possible_win_combo = self.computer.get_possible_win_combos(board)
        self.assertEqual(possible_win_combo, [7]) 

    def test_computer_can_get_possible_2_5_8_vertical_win(self):
        board = [0, 1, 0, 0, 1, 0, 0, 0, 0]
        possible_win_combo = self.computer.get_possible_win_combos(board)
        self.assertEqual(possible_win_combo, [8]) 

    def test_computer_can_get_possible_3_6_9_vertical_win(self):
        board = [0, 0, 1, 0, 0, 1, 0, 0, 0]
        possible_win_combo = self.computer.get_possible_win_combos(board)
        self.assertEqual(possible_win_combo, [9]) 

    def test_computer_can_get_possible_1_5_9_diagonal_win(self):
        board = [1, 0, 0, 0, 0, 0, 0, 0, 1]
        possible_win_combo = self.computer.get_possible_win_combos(board)
        self.assertEqual(possible_win_combo, [5]) 

    def test_computer_can_get_possible_3_5_7_diagonal_win(self):
        board = [0, 0, 0, 0, 1, 0, 1, 0, 0]
        possible_win_combo = self.computer.get_possible_win_combos(board)
        self.assertEqual(possible_win_combo, [3]) 

    def test_computer_can_block_1_2_3_possible_win_combo(self): 
        board = [1, 1, 0, 0, 0, 0, 0, 0, 0]
        next_move = self.computer.make_move(board)
        self.assertEqual(next_move, 3)

    def test_computer_can_block_4_5_6_possible_win_combo(self): 
        board = [0, 0, 0, 1, 1, 0, 0, 0, 0]
        next_move = self.computer.make_move(board)
        self.assertEqual(next_move, 6)

    def test_computer_can_block_7_8_9_possible_win_combo(self): 
        board = [0, 0, 0, 0, 0, 0, 1, 1, 0]
        next_move = self.computer.make_move(board)
        self.assertEqual(next_move, 9)

    def test_computer_can_block_1_4_7_possible_win_combo(self): 
        board = [0, 0, 0, 1, 0, 0, 1, 0, 0]
        next_move = self.computer.make_move(board)
        self.assertEqual(next_move, 1)
        
    def test_computer_can_block_2_5_8_possible_win_combo(self): 
        board = [0, 1, 0, 0, 0, 0, 0, 1, 0]
        next_move = self.computer.make_move(board)
        self.assertEqual(next_move, 5)

    def test_computer_can_block_3_6_9_possible_win_combo(self): 
        board = [0, 0, 1, 0, 0, 0, 0, 0, 1]
        next_move = self.computer.make_move(board)
        self.assertEqual(next_move, 6)

    def test_computer_can_block_1_5_9_possible_win_combo(self): 
        board = [0, 0, 0, 0, 1, 0, 0, 0, 1]
        next_move = self.computer.make_move(board)
        self.assertEqual(next_move, 1)

    def test_computer_can_block_3_5_7_possible_win_combo(self): 
        board = [0, 0, 1, 0, 1, 0, 0, 0, 0]
        next_move = self.computer.make_move(board)
        self.assertEqual(next_move, 7)

    


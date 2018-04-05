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
        new_board = self.computer.get_old_moves(board)
        possible_win_combo = self.computer.get_potential_wins(new_board)
        self.assertEqual(possible_win_combo, [1, 2, 3])

    def test_computer_can_get_possible_4_5_6_horizontal_win(self):
        board = [0, 0, 0, 1, 1, 0, 0, 0, 0]
        new_board = self.computer.get_old_moves(board) 
        possible_win_combo = self.computer.get_potential_wins(new_board)
        self.assertEqual(possible_win_combo, [4, 5, 6]) 
        
    def test_computer_can_get_possible_7_8_9_horizontal_win(self):
        board = [0, 0, 0, 0, 0, 0, 1, 1, 0]
        new_board = self.computer.get_old_moves(board) 
        possible_win_combo = self.computer.get_potential_wins(new_board)
        self.assertEqual(possible_win_combo, [7, 8, 9]) 

    def test_computer_can_block_1_2_3_possible_win_combo(self): 
        board = [1, 1, 0, 0, 0, 0, 0, 0, 0]
        new_board = self.computer.get_old_moves(board)
        next_move = self.computer.block_winning_horizontal_move(new_board)
        self.assertEqual(next_move, 3)

    def test_computer_can_block_4_5_6_possible_win_combo(self): 
        board = [0, 0, 0, 1, 1, 0, 0, 0, 0]
        new_board = self.computer.get_old_moves(board)
        next_move = self.computer.block_winning_horizontal_move(new_board)
        self.assertEqual(next_move, 6)

    def test_computer_can_block_7_8_9_possible_win_combo(self): 
        board = [0, 0, 0, 0, 0, 0, 1, 1, 0]
        new_board = self.computer.get_old_moves(board)
        next_move = self.computer.block_winning_horizontal_move(new_board)
        self.assertEqual(next_move, 9)

    


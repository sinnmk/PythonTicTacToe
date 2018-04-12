from apps.minimax import Minimax
import unittest

class TestMinimax(unittest.TestCase): 

    def setUp(self): 
        self.minimax = Minimax()

    def test_can_get_future_board_state(self): 
        new_board = [1, 0, 2, 0, 0, 1, 1, 0, 0]
        future_board_states = self.minimax.future_board_states()
        self.assertEqual(future_board_states, [1, 1, 2, 0, 0, 1, 1, 0, 0])

    

    

from apps.human import Human
import unittest
from unittest.mock import Mock, patch

class TestHuman(unittest.TestCase): 
    
    def setUp(self): 
        self.human = Human()

    def test_make_move(self): 
        board = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        move = self.human.make_move(board)
        self.assertTrue(move)

    def test_set_turn(self):
        turn = self.human.set_turn()
        self.assertTrue(turn)
    

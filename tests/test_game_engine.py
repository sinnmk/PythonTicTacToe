import unittest
from apps.game_engine import GameEngine

class TestGameEngine(unittest.TestCase): 

    def setUp(self): 
        self.game_engine = GameEngine()

    def test_can_store_moves_after_human_turn(self): 
        moves = self.game_engine.store_player_one_moves()
        self.assertEqual(len(moves), 1)

    def test_can_store_moves_after_comp_turn(self): 
        moves = self.game_engine.store_player_two_moves()
        self.assertEqual(len(moves), 1)


    


    

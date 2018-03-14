import unittest
from apps.computer_logic import ComputerLogic

class TestComputerLogic(unittest.TestCase): 

    def setUp(self): 
        self.game_logic = GameLogic()

    def test_computer_can_make_first_move(self): 
        first_move = self.game_logic.make_comp_move()
        assert self.game_logic.make_computer_move is not None



    



        



        

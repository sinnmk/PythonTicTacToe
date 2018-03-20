import unittest
from apps.computer_logic import ComputerLogic 

class ComputerLogic(unittest.TestCase):
    
    def setUp(self): 
        self.computer_logic = ComputerLogic()

#    def test_can_make_random_move(self): 
#        move = self.computer_logic.make_comp_move()
#        assert self.computer_logic.make_comp_move() is not None
#

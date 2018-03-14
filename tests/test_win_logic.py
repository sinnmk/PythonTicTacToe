import unittest
from apps.win_logic import WinLogic

class TestWinLogic(unittest.TestCase): 

    def setUp(self): 
        self.win_logic = WinLogic()

    def test_that_the_game_can_win(self): 
        win = self.win_logic.is_win()
        self.assertEqual(win, True)

    def test_check_if_win(self): 
        checked_win = self.win_logic.check_if_win()
        self.assertEqual(checked_win, [1, 4, 7])



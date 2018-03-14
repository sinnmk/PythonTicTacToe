import unittest
from apps.user_interface import UserInterface

class TestUserInterface(unittest.TestCase): 

    def setUp(self): 
        self.user_interface = UserInterface()

    def test_display_rules(self):
        rules = self.user_interface.display_rules()
        self.assertEqual(rules,"The object of the game Tic Tac Toe is to get three in a row. You play on a three by three game board. The first player is known as X and the second is O. Players alternate placing X's and O's on the game board until either opponent has three in a row or all nine squares are filled. X always goes first, and in the even that no one has three in a row, the stalemate is called a cat game.")    

    def test_can_get_menu_choice_to_display_rules(self): 
        menu_choice = self.user_interface.get_menu_choice()
        self.assertEqual(menu_choice, 2)

    def test_can_display_user_prompt(self): 
        user_prompt = self.user_interface.display_user_prompt()
        self.assertEqual(user_prompt, ("Welcome to Tic Tac Toe!"))

    def test_can_get_game_move_number_2(self): 
        user_move = self.user_interface.get_game_move()
        self.assertEqual(user_move, 2)

    



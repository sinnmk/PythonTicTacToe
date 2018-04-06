import unittest
from unittest.mock import patch, Mock
from apps.game_engine import GameEngine

class TestGameEngine(unittest.TestCase): 

    def setUp(self): 
        self.game_engine = GameEngine()

    def test_display_blank_board(self): 
        board = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        display_board = self.game_engine.display_board(board)
        self.assertEqual(display_board, [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '])

    def test_modify_board(self):
        board =[1, 1, 2, 2, 0, 0, 0, 0, 0]
        display_board = self.game_engine.display_board(board)
        self.assertEqual(display_board, ['X', 'X', 'O', 'O', ' ', ' ', ' ', ' ', ' '])

    def test_check_for_win(self): 
        pass

    def test_check_for_non_win(self): 
        pass

    def test_place_x(self): 
        index = 1
        board = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        place_x = self.game_engine.place_x(index, board)
        self.assertEqual(board, [0, 1, 0, 0, 0, 0, 0, 0, 0])

    def test_place_o(self): 
        index = 0
        board = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        place_o = self.game_engine.place_o(index, board)
        self.assertEqual(board, [2, 0, 0, 0, 0, 0, 0, 0, 0])

    def test_mocking_display_board_function(self): 
        mock = Mock()
        board = [1, 2, 0, 0, 0, 0, 0, 0, 0]
        display = self.game_engine.display_board(board)
        mock.display.return_value = 1
        print(mock.display(board))
        mock.display.assert_called_once_with(board)

    @patch.object(GameEngine, 'display_players_name')
    def test_mock_calling_display_players_name(self, mock_display_players_name):
        GameEngine.display_players_name(1)
        mock_display_players_name.assert_called_with(1)

    @patch.object(GameEngine, 'computer_vs_computer')
    def test_mocking_computer_vs_computer_function(self, mock_computer_vs_computer): 
        mock_computer_vs_computer.return_value = "You have mocked computer_vs_computer function"
        result = GameEngine.computer_vs_computer()
        print(result)

    @patch.object(GameEngine, 'place_x')
    def test_mocking_place_x_function(self, mock_place_x): 
        mock_place_x.return_value = "You have mocked place_x function"
        result = GameEngine.place_x()
        count_of_calls = mock_place_x.call_count
        self.assertEqual(count_of_calls, 1)

    @patch.object(GameEngine, 'choose_menu_choice')
    def test_mocking_choose_menu_choice(self, mock_menu_choice): 
        mock_menu_choice.return_value = "You have mocked choose menu choice"
        result = GameEngine.choose_menu_choice()
        count_of_calls = mock_menu_choice.call_count
        self.assertEqual(count_of_calls, 1)






        


        
        

        

        

        







        

    
        

        
        




        
    



        
        
    




        

        
        
    
        



        
        



    

    


    

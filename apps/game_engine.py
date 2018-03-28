from user_interface import UserInterface 
from player import Player, Human, Computer
import time

class GameEngine(object): 

    def __init__(self): 
        #_______IMPORTS________
        self.user_interface = UserInterface()
        self.computer_player = Computer()
        self.human_player = Human()
        #_______MESSAGES________
        self.invalid_input_msg = ("You have given an invalid choice, please try again: ")
        self.menu_choice_msg = ("\nTIC TAC TOE MENU \n1. Player vs Computer \n2. Player vs Player \n3. Computer vs Computer \n4. Display Rules \n5. Quit")
        self.welcome_pvc_msg = ("Welcome to Player vs Computer Tic Tac Toe!")
        self.invalid_entry_msg = ("This is not a valid entry")
        self.not_open_msg = ("POSITION TAKEN")
        self.input_choice_msg = ("""Please pick menu choice(1-5): """)
        #_______VARIABLES________
        self.place_board = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.game_running = True

    def display_players_name(self): 
        print("It is " + self.human_player.set_name() + " turn")

    #_____DISPLAY AND MODIFY BOARD_____
    def display_board(self): 
        self.game_board_list = []

        for i in range(0, 9): 
            if self.place_board[i] == 1: 
                self.game_board_list.append('X')
            elif self.place_board[i] == 2: 
                self.game_board_list.append('O')
            elif self.place_board[i] == 0: 
                self.game_board_list.append(' ')

        print("""
         {} | {} | {}
        ---+---+---
         {} | {} | {}
        ---+---+---
         {} | {} | {}
        """.format(*self.game_board_list))
        return self.place_board

    #__________EVALUATE WIN___________
    def check_for_win(self): 
        win_combos = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))

        for i in win_combos:
            if self.place_board[i[0]] == 1 and self.place_board[i[1]] == 1 and self.place_board[i[2]] == 1: 
                print("Player X WINS")
                self.game_running = False

            elif self.place_board[i[0]] == 2 and self.place_board[i[1]] == 2 and self.place_board[i[2]] == 2: 
                print("Player O WINS")
                self.game_running = False

    #________CHECK OPEN POSITIONS_______ 
    def is_position_open(self, index): 
        for digit in self.place_board: 
            if self.place_board[index] == 0: 
                return True
            elif self.place_board[index] != 0: 
                return False

   #_____________PLACE MOVE____________
    def place_x(self, index): 
        if self.is_position_open(index) == True: 
            self.place_board[index] = 1
        else: 
            print(self.not_open_msg)

    def place_o(self, index): 
        if self.is_position_open(index) == True: 
            self.place_board[index] = 2
        else: 
            print(self.not_open_msg)

    #____________GAME CHOICES____________
    def player_vs_computer(self): 
        while self.game_running:
            self.user_interface.print_example_board()
            index = self.human_player.find_index_of_move()
            self.place_x(index) 
            index = self.computer_player.find_index_of_move()
            self.place_o(index)
            self.display_board()
            self.check_for_win()

    def player_vs_player(self): 
        while self.game_running: 
            index = self.human_player.find_index_of_move()
            self.place_x(index)
            self.display_board()
            index = self.human_player.find_index_of_move()
            self.place_o(index)
            self.display_board()
            self.check_for_win()

    def computer_vs_computer(self): 
        while self.game_running: 
            index = self.computer_player.find_index_of_move()
            self.place_x(index)
            self.display_board()
            time.sleep(1)
            index = self.computer_player.find_index_of_move()
            self.place_o(index)
            self.display_board()
            self.check_for_win()
            time.sleep(1)
            
    def display_rules(self): 
        self.user_interface.display_rules()
        return self.choose_menu_choice()

    def exit_game(self): 
        exit()

    #__________MENU___________
    def choose_menu_choice(self): 
        self.user_interface.display_game_prompt()
        self.user_interface.display_menu()
        menu_choices = [self.player_vs_computer, self.player_vs_player, self.computer_vs_computer, self.display_rules, self.exit_game]
        menu_choice = int(input(self.input_choice_msg)) - 1 
        menu_choices[menu_choice]()

if __name__ == "__main__": 
    a = GameEngine()
    a.choose_menu_choice()

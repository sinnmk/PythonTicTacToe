import os

class UserInterface(object): 

    def __init__(self): 
        pass

    def get_open_positions(self, board): 
        open_positions = []
        i = 0
        while i < len(board): 
            for digit in board: 
                if board[i] == 0: 
                    open_positions.append(i + 1)
                if board[i] != 0: 
                    open_positions.append("")
                i += 1
        return open_positions

    def input_move(self, board): 
        open_positions = self.get_open_positions(board)
        while True: 
            try: 
                move = int(input(self.display_move_choice_msg()))
                if move in open_positions: 
                    return move
                else: 
                    self.display_invalid_move_msg()
                    return self.input_move(board)
            except ValueError: 
                return self.display_invalid_input_msg()

    def input_turn_choice(self): 
        while True: 
            try: 
                turn_choice = int(input(self.display_player_turn_choice_msg()))
                return turn_choice
            except ValueError: 
                return self.display_invalid_input_msg()

    def input_difficulty_choice(self): 
        while True: 
            try: 
                difficulty_choice = int(input(self.display_difficulty_choices()))
                return difficulty_choice 
            except ValueError: 
                return self.input_difficulty_choice()

    def input_name(self): 
        while True: 
            try: 
                name = input(self.display_input_name_msg())
                return name
            except ValueError: 
                return self.display_invalid_input_msg()

    def input_menu_choice(self): 
        while True: 
            try: 
                choice = int(input(self.display_input_choice_msg()))
            except ValueError: 
                return self.display_invalid_input_msg()
            else: 
                return choice

    def input_play_again_choice(self): 
        while True: 
            try: 
                choice = str(input(self.display_play_again_msg()))
            except ValueError: 
                return self.display_invalid_input_msg()
            else: 
                return choice

    def input_size_of_board(self): 
        while True: 
            try: 
                size = int(input(self.display_size_msg()))
            except ValueError: 
                return self.display_invalid_input_msg()
            else: 
                return size

    def display_size_msg(self): 
        size_msg = ("Choose size of board: ")
        return (size_msg)
            
    def modify_game_board_list(self, board):
        game_board_list = []
        for i in range(0, 9):
            if board[i] == 1:
                game_board_list.append('X')
            elif board[i] == 2:
                game_board_list.append('O')
            elif board[i] == 0: game_board_list.append(i + 1)
        return game_board_list

    def display_difficulty_choices(self): 
        difficulty_choice = ("\n1. Novice Computer \n2. Intermediate Computer \n3. Master Computer \n Please choose your difficulty: ")
        return difficulty_choice

    def display_game_board(self, game_board_list): 
        print("""
         {} | {} | {}
        ---+---+---
         {} | {} | {}
        ---+---+---
         {} | {} | {}
        """.format(*game_board_list))

    def display_example_board(self): 
        example_board = ("""
        1 | 2 | 3 
       ---+---+---
        4 | 5 | 6
       ---+---+---
        7 | 8 | 9

        """)
        print(example_board)

    def display_goodbye_msg(self): 
        goodbye_msg = ("Thanks for playing, Goodbye!")
        print(goodbye_msg)

    def display_game_prompt(self): 
        game_prompt = ("----------Welcome to TIC TAC TOE--------")
        print(game_prompt)

    def display_menu(self): 
        menu = ("\n1. Player vs Computer \n2. Player vs Player \n3. Computer vs Computer \n4. Display Rules \n5. Quit")
        print(menu)

    def display_menu_choice_msg(self): 
        menu_choice_msg = ("\nTIC TAC TOE MENU \n1. Player vs Computer \n2. Player vs Player \n3. Computer vs Computer \n4. Display Rules \n5. Quit")
        print(menu_choice_msg)

    def display_winning_msg(self): 
        win_msg = "Winner"
        print(win_msg)

    def display_cat_game_msg(self): 
        cat_game_msg = "CAT GAME! Better luck next time!"
        print(cat_game_msg)

    def display_invalid_input_msg(self): 
        invalid_input_msg = "This is not a valid entry, please try again: "
        print(invalid_input_msg)

    def display_game_rules(self):
        game_rules = "The object of the game Tic Tac Toe is to get three in a row. You play on a three by three game board. The first player is known as X and the second is O. Players alternate placing X's and O's on the game board until either opponent has three in a row or all nine squares are filled. In the event that no one has three in a row, the stalemate is called a cat game."    
        print(game_rules)

    def display_invalid_move_msg(self): 
        not_valid_position_msg = ("Position is not open, please choose an open position.")
        print(not_valid_position_msg)

    def display_game_over_msg(self): 
        game_over_msg = print("Game Over")
        print(game_over_msg)

    def display_pvp_prompt_msg(self): 
        pvp_prompt_msg = "X goes first, O goes second."
        print(pvp_prompt_msg)

    def display_move_choice_msg(self): 
        game_move_choice_msg = "Enter your move: "
        return game_move_choice_msg

    def display_input_choice_msg(self): 
        input_choice_msg = "Please pick menu choice(1-5): "
        return input_choice_msg

    def display_player_turn_choice_msg(self): 
        player_turn_choice_msg = "Which player are you, Player[1] or Player[2]?: "
        return player_turn_choice_msg

    def display_input_name_msg(self): 
        input_name_msg = "Please enter your name: "
        return input_name_msg

    def display_play_again_msg(self): 
        play_again_msg = ("Would you like to play again? [Y]es or [N]o: ")
        return play_again_msg

    def clear_screen(self): 
        os_name = os.name
        if os_name == 'nt':
            clear_message = 'cls'
        else: 
            clear_message = 'clear'
        os.system(clear_message)

class UserInterface(object): 

    def __init__(self): 
        self.game_rules = ("The object of the game Tic Tac Toe is to get three in a row. You play on a three by three game board. The first player is known as X and the second is O. Players alternate placing X's and O's on the game board until either opponent has three in a row or all nine squares are filled. In the event that no one has three in a row, the stalemate is called a cat game.")    
        self.game_move_choice_msg = ("Please enter your move (1-9): ")
        self.player_choice_msg = ("To go first, enter 1. To go second, enter 2: ")
        self.input_name_msg = ("Please enter your name: ")
        self.user_choice_msg = ("Please enter your menu choice: ")
        self.invalid_input_msg = ("This is not a valid entry, please try again: ")
        self.not_valid_position_msg = ("Position is not open, please choose an open position.")

    def print_example_board(self): 
        example_board = ("""
        1 | 2 | 3 
       ---+---+---
        4 | 5 | 6
       ---+---+---
        7 | 8 | 9

        """)
        print(example_board)

    def display_rules(self):
        print(self.game_rules)

    def display_game_prompt(self): 
        game_prompt = ("""----------Welcome to TIC TAC TOE--------""")
        print(game_prompt)

    def display_menu(self): 
        menu = ("""
                [1] Player vs Computer
                [2] Player vs Player 
                [3] Computer vs Computer
                [4] Display Rules 
                [5] Exit Game\n""")

        print(menu)

    def display_pvc_prompt(self): 
        pvc_prompt = ("""
                Welcome to Player vs. Computer mode!\n
                Please choose your opponent's difficulty level: """)
        print(pvc_prompt)

    def display_pvc_sub_menu(self): 
        sub_menu = ("""
                [1] Novice Computer
                [2] Intermediate Computer
                [3] Master Computer
                [4] Go back to Main Menu
                [5] Exit Game\n""")
        print(sub_menu)

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
                move = int(input(self.game_move_choice_msg))
                if move in open_positions: 
                    return move
                else: 
                    self.not_valid_position_msg()
                    return self.input_move(board)
            except ValueError: 
                print(self.invalid_input_msg)

    def input_turn_choice(self): 
        while True: 
            try: 
                turn_choice = int(input(self.player_choice_msg))
                return turn_choice
            except ValueError: 
                print(self.invalid_input_msg)

    def input_name(self): 
        while True: 
            try: 
                name = input(self.input_name_msg)
                return name
            except ValueError: 
                print(self.invalid_input_msg)

    def input_menu_choice(self): 
        while True: 
            try: 
                choice = int(input(self.user_choice_msg))
            except ValueError: 
                print(self.invalid_input_msg)
            else: 
                return choice

    def input_sub_menu_choice(self): 
        while True: 
            try: 
                choice = int(input(self.user_choice_msg))
            except ValueError: 
                print(self.invalid_input_msg)
            else: 
                return choice






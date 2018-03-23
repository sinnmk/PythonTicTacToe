class UserInterface(object): 

    def __init__(self): 
        #prompts
        self.user_prompt = ("Welcome to Tic Tac Toe!")
        self.menu_prompt = ("Tic Tac Toe's MENU")
        #rules display
        self.game_rules = ("The object of the game Tic Tac Toe is to get three in a row. You play on a three by three game board. The first player is known as X and the second is O. Players alternate placing X's and O's on the game board until either opponent has three in a row or all nine squares are filled. In the event that no one has three in a row, the stalemate is called a cat game.")    
        #input/output msgs 
        self.game_move_choice_msg = ("Please enter your move (1-9): ")
        self.player_choice_msg = ("To go first, enter 1. To go second, enter 2: ")
        self.input_name_msg = ("Please enter your name: ")
        self.user_choice_msg = ("Please enter your menu choice: ")
        self.invalid_input_msg = ("You have entered an invalid choice, please try again: ")
        #Menus
        self.top_menu_title = ("TIC TAC TOE: MAIN MENU")
        self.top_menu_choices = ("1. Play Person vs Computer \n2. Play Person vs Person \n3. Play Computer vs Computer \n4. Display Rules\n5. Quit")
        self.line_divide = ("------------")

    def display_rules(self):
        return self.game_rules

    def input_move(self): 
        while True: 
            try: 
                move = int(input(self.game_move_choice_msg))
                return move
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

    def display_user_prompt(self): 
        return self.user_prompt

    def display_menu_prompt(self): 
        return self.menu_prompt

    def input_menu_choice(self): 
        while True: 
            try: 
                choice = int(input(self.user_choice_msg))
                return choice
            except ValueError: 
                print(self.invalid_input_msg)

    def display_menu(self): 
        print(self.line_divide)
        print(self.top_menu_title)
        print(self.top_menu_choices)
        print(self.line_divide)

        


    

    




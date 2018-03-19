class UserInterface(object): 

    def __init__(self): 
        self.user_choice_msg = ("Please enter your menu choice: ")
        self.invalid_input_msg = ("You have entered an invalid choice, please try again: ")
        self.user_prompt = ("Welcome to Tic Tac Toe!")
        self.game_rules = ("The object of the game Tic Tac Toe is to get three in a row. You play on a three by three game board. The first player is known as X and the second is O. Players alternate placing X's and O's on the game board until either opponent has three in a row or all nine squares are filled. X always goes first, and in the even that no one has three in a row, the stalemate is called a cat game.")    
        self.menu_prompt = ("Welcome to Tic Tac Toe's MENU")
        self.game_move_choice_msg = ("Please enter your move. You can pick from numbers 1-9: ")
        self.player_choice_msg = ("Please choose turn. If you want to go first, enter 1. If you want to go second, enter 2: ")
        self.game_title = ("TIC TAC TOE")
        self.choice_one = ("1. Play Game")
        self.choice_two = ("2. Display Rules")
        self.choice_three = ("3. Quit")
        self.lines = ("-------------------")

    def display_rules(self):
        return self.game_rules

    def get_game_move(self): 
        user_move = int(raw_input(self.game_move_choice_msg))
        return user_move

    def get_player_turn_choice(self): 
        player_turn_choice = int(raw_input(self.player_choice_msg))
        choice = player_turn_choice
        return choice 

    def get_players_name(self): 
        player_name = raw_input("Input your name: ")
        name = player_name
        return name 

    def display_user_prompt(self): 
        return self.user_prompt

    def menu_prompt(self): 
        return self.menu_prompt

    def display_menu(self): 
        print(self.lines)
        print(self.game_title)
        print(self.choice_one)
        print(self.choice_two)
        print(self.choice_three)
        print(self.lines)

    def get_menu_choice(self): 
        while True: 
            try: 
                choice = int(raw_input(self.user_choice_msg))
                return choice
            except ValueError: 
                print(self.invalid_input_msg)

        


    

    




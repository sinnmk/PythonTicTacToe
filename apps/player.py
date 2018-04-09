class Player(object): 
    move = '' 
    index = '' 
    name = ''

    def __init__(self, move, index, name): 
        self.move = move 
        self.index = index
        self.name = name 
        self.num_board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.game_engine = GameEngine()

    def get_name(self): 
        return self.name

    def make_move(self, board):
        return self.move

    def find_index_of_move(self, board):
        move = self.make_move(board)
        move_index = 0
        for num in self.num_board: 
            if num == move:
                move_index = move - 1
        return move_index
    
    def display_players_name(self): 
        print (self.set_name() + "'s" + " turn...")

def move(Player): 
    Player.make_move(board)

def name(Player): 
    Player.set_name()

def display_name(Player): 
    Player.display_players_name()

def set_turn(Player): 
    Player.set_turn()

def find_index_of_move(Player):
    Player.find_index_of_move(board)

def set_player_turn_position(Player): 
    Player.get_current_player(turn)




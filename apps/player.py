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

    def get_move(self, board):
        return self.move

    def find_index_of_move(self, board):
        move = self.get_move(board)
        move_index = [move - 1 for num in self.num_board if num == move]
        index = move_index[0]
        return index

    def make_move(self, index, board, player_marker):
        x = 1
        o = 2
        if player_marker == x:
            board[index] = 1
        if player_marker == o:
            board[index] = 2

    def display_players_name(self):
        print (self.set_name() + "'s" + " turn...")

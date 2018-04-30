from user_interface import UserInterface

class Human(object):

    def __init__(self, marker):
        self.user_interface = UserInterface()
        self.stored_moves = []
        self.num_board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.marker = marker

    def get_move(self, board):
        move = self.user_interface.input_move(board)
        return move

    def make_move(self, board):
        print("human move")

    def set_name(self):
        name = self.user_interface.input_name()
        return name


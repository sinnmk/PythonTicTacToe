import random 

class ComputerLogic(object): 

    def __init__(self): 
        self.game_board = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    def get_comp_move(self):
        comp_game_move = random.choice(self.game_board)
        return comp_game_move

    



        
        
        
        


        
        
        
        

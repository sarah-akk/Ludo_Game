from algorithm import Algorithm
from state import State
import math

class Player:
    def __init__(self, id, name, color, symbol, is_human=True):
        self._id = id
        self._name = name
        self._color = color
        self._symbol = symbol 
        self._is_human = is_human
        self._is_ai = not is_human
        self._pawns = []  
        self.indices = {}
        self.algorithm = Algorithm()

    def set_indices(self, data):
        self.indices = data

    def get_road_cells(self):
        return self.indices.get("roadCells", [])

    def get_start_cell(self):
        return self.indices.get("startCell", None)

    def get_home_cell(self):
        return self.indices.get("homeCell", None)

    def get_end_cell(self):
        return self.indices.get("endCell", None)

    def get_id(self):
        return self._id

    def set_id(self, id):
        self._id = id

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_color(self):
        return self._color

    def set_color(self, color):
        self._color = color

    def get_is_human(self):
        return self._is_human

    def set_is_human(self, is_human):
        self._is_human = is_human
        self._is_ai = not is_human

    def get_is_ai(self):
        return self._is_ai

    def get_symbol(self):
        return self._symbol  

    def set_symbol(self, symbol):
        self._symbol = symbol  

    def get_pawns(self):
        return self._pawns

    def set_pawns(self, pawns):
        self._pawns = pawns


    def input_pawn_id(self , game , moves , roll_res):
        if(self.get_is_human()):
           pawn_id = input("Enter the id of the pawn you want to move: ")

        else:
            # get moves 
            pawn_id = moves[0]
            maxRes = - math.inf
            for move in moves:
                #For each move, it generates a new state and calls expectiminmax recursively.
                print('lets try move : ' , move  % 10)
                tmpState = State(game).new_state(move , roll_res)
                tmpRes = self.algorithm.expectiminmax(tmpState , False , roll_res , 1 , self)
                if(tmpRes > maxRes):
                    print('tmp is ' , tmpRes , ' max is ' , maxRes , 'new pawn is ' , move)
                    maxRes = tmpRes
                    pawn_id = move % 10
            # return max moves pawn    
        return pawn_id
    
    def get_corner_cells(self):
        """
        Returns a list of corner cell coordinates where the player's pawns start.
        """
        if not self._pawns:
            print(f"Player {self.get_name()} has no pawns set.")
            return []

        # Extract the positions of the player's pawns
        corner_cells = [pawn.get_cell().get_position() for pawn in self._pawns]
        return corner_cells


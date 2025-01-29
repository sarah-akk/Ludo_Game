from cell import Cell

class Pawn:
    def __init__(self,id, x, y, color=None, player_id=None, position=None, symbol=None, cell=None):
        self.corner_x = x 
        self.corner_y = y
        self.id = id
        self.x = x  # X position
        self.y = y  # Y position
        self.cell = cell  # Associated cell
        self.color = color
        self.player_id = player_id
        self.position = position
        self.symbol = symbol
        
    def __str__(self):
        return f"pawn {self.id} in {self.x} , {self.y} for player {self.player_id} cell {self.cell}"

    def get_color(self):
        return self.color

    def set_color(self, color):
        self.color = color

    def get_position(self):
        return self.position

    def set_position(self, position):
        self.position = position

    # Getter and Setter for symbol
    def get_symbol(self):
        return self.symbol

    def set_symbol(self, symbol):
        self.symbol = symbol

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id    

    def get_cell(self):
        return self.cell

    def set_cell(self, cell):
        if isinstance(cell, Cell):
            self.cell = cell
            self.x = cell.x
            self.y = cell.y
        else:
            raise ValueError("Invalid cell type: must be an instance of Cell")

    
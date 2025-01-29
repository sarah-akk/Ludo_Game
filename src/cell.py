from constants import Constants

class Cell:
    def __init__(self, x, y, color=Constants.Color.WHITE, type = Constants.Type.ROAD , direction = None , home_base_direction = None):
        self.x = x
        self.y = y
        self.color = color
        self.type = type
        self.direction = direction
        self.home_base_direction = home_base_direction

    def __str__(self):
        return f"Cell({self.x}, {self.y}, {self.color}, {self.type})"
    
    def get_position(self):
        return (self.x , self.y)

    def get_x(self):
        return self.x

    def set_x(self, x):
        self.x = x

    def get_y(self):
        return self.y

    def set_y(self, y):
        self.y = y

    def get_color(self):
        return self.color

    def set_color(self, color):
        self.color = color

    def get_type(self):
        return self.type

    def set_type(self, type):
        self.type = type

    def get_direction(self):
        return self.direction

    def set_direction(self, direction):
        self.direction = direction

    def get_home_base_direction(self):
        return self.home_base_direction

    def set_home_base_direction(self, home_base_direction):
        self.home_base_direction = home_base_direction

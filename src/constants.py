
class Constants:
    class Direction:
        UP = "up"
        RIGHT = "right"
        DOWN = "down" 
        LEFT = "left"
        UP_RIGHT = 'up-right'
        RIGHT_UP = 'right-up'
        UP_LEFT = 'up-left'
        LEFT_UP = 'left-up'
        DOWN_RIGHT = 'down-right'
        RIGHT_DOWN = 'right-down'
        DOWN_LEFT = 'down-left'
        LEFT_DOWN = 'left-down'

    class Color:
        RED = "red"
        GREEN = "green" 
        YELLOW = "yellow"
        BLUE = "blue"
        WHITE = "white"
        BLACK = "black"
        BROWN = "brown"

    class Type:
        ROAD = "road"
        HOME_BASE = "home_base" 
        CORNER = "corner" 
        START = "start"
        END = "end"

    GRID_SIZE = 15

    def __init__(self):
        pass

    def get_grid_size(self):
        return self.GRID_SIZE
    
    def get_corners_indices(self, TopLeftPlayer , TopRightPlayer , BottomRightPlayer, BottomLeftPlayer ):

        # Initialize an empty list for corners
        corners = []

        # Top left corner (1-6, 1-6)
        corners.extend([(
            x,
            y,
            self.Color.BROWN,
            self.Type.CORNER
        ) for x in range(1, 7) for y in range(1, 7)])

        # Top right corner (10-15, 1-6)
        corners.extend([(
            x,
            y,
            self.Color.BROWN,
            self.Type.CORNER
        ) for x in range(1, 7) for y in range(10, 16)])

        # Bottom right corner (10-15, 10-15)
        corners.extend([(
            x,
            y,
            self.Color.BROWN,
            self.Type.CORNER
        ) for x in range(10, 16) for y in range(10, 16)])

        # Bottom left corner (1-6, 10-15)
        corners.extend([(
            x,
            y,
            self.Color.BROWN,
            self.Type.CORNER
        ) for x in range(10, 16) for y in range(1, 7)])
        
        return corners

##########################################################################################
            
    def get_home_base_indices(self , color = Color().BROWN):
        # Return list of tuples containing coordinates for middle 3x3 square
        middle = []
            
        # Middle square (7-9, 7-9)
        middle = [(x, y , color  , self.Type.HOME_BASE) for x in range(7, 10) for y in range(7, 10)]
            
        return middle
    
    def get_start_indices(self, TopLeftPlayer = None, TopRightPlayer = None, BottomRightPlayer = None, BottomLeftPlayer = None):
        starts = []
        
        starts.append((7 , 2 , TopLeftPlayer.get_color() if TopLeftPlayer else self.Color.BROWN , self.Type.START))
        starts.append((2 , 9 , TopRightPlayer.get_color() if TopRightPlayer else self.Color.BROWN , self.Type.START))
        starts.append((9 , 14 , BottomRightPlayer.get_color() if BottomRightPlayer else self.Color.BROWN , self.Type.START))
        starts.append((14 , 7 , BottomLeftPlayer.get_color() if BottomLeftPlayer else self.Color.BROWN , self.Type.START))
        
        return starts

##########################################################################################
        
    def get_end_indices(self, TopLeftPlayer = None, TopRightPlayer = None, BottomRightPlayer = None, BottomLeftPlayer = None):
        ends = []
        
        # Top left corner
        ends.extend([(
            8,
            y,
            TopLeftPlayer.get_color() if TopLeftPlayer else self.Color.BROWN , 
            self.Type.END
        ) for y in range(2, 7)])
        
        # Top right corner
        ends.extend([(
            x,
            8,
            TopRightPlayer.get_color() if TopRightPlayer else self.Color.BROWN , 
            self.Type.END
        ) for x in range(2, 7)])
        
        # Bottom right corner
        ends.extend([(
            8,
            y,
            BottomRightPlayer.get_color() if BottomRightPlayer else self.Color.BROWN , 
            self.Type.END
        ) for y in range(10, 15)]) 
        
        # Bottom left corner
        ends.extend([(
            x,
            8,
            BottomLeftPlayer.get_color() if BottomLeftPlayer else self.Color.BROWN , 
            self.Type.END
        ) for x in range(10, 15)])
        
        return ends 
    

 ##########################################################################################
   
    def players_indices(TopLeftPlayer = None, TopRightPlayer = None, BottomRightPlayer = None, BottomLeftPlayer = None):
        players_data = {}

        # Define the data for each player, if they exist
        if TopLeftPlayer:
            players_data[TopLeftPlayer.get_id()] = {
                "startCell": (7, 2),
                "endCell": [(8, 2), (8, 3), (8, 4), (8, 5), (8, 6)],
                "homeCell": (8, 7),
                "roadCells": [
                    (7, 2), (7, 3), (7, 4), (7, 5), (7, 6),
                    (6, 7), (5, 7), (4, 7), (3, 7), (2, 7), (1, 7),
                    (1, 8), (1, 9), (2, 9), (3, 9), (4, 9), (5, 9),
                    (6, 9), (7, 10), (7, 11), (7, 12), (7, 13), (7, 14), (7, 15),
                    (8, 15), (9, 15), (9, 14), (9, 13), (9, 12), (9, 11),
                    (9, 10), (10, 9), (11, 9), (12, 9), (13, 9), (14, 9), (15, 9),
                    (15, 8), (15, 7), (14, 7), (13, 7), (12, 7), (11, 7), (10, 7),
                    (9, 6), (9, 5), (9, 4), (9, 3), (9, 2), (9, 1),
                    (8, 1), (8, 2), (8, 3), (8, 4), (8, 5), (8, 6),
                    (8, 7)
                ]
            }

        if TopRightPlayer:
            players_data[TopRightPlayer.get_id()] = {
                "startCell": (2, 9),
                "endCell": [(2,8), (3,8), (4,8), (5,8), (6,8)],
                "homeCell": (7, 8),
                "roadCells": [
                    (2,9), (3,9), (4,9), (5,9), (6,9),
                    (7,10), (7,11), (7,12), (7,13), (7,14), (7,15),
                    (8,15), (9,15), (9,14), (9,13), (9,12), (9,11), (9,10),
                    (10,9), (11,9), (12,9), (13,9), (14,9), (15,9),
                    (15,8), (15,7), (14,7), (13,7), (12,7), (11,7), (10,7),
                    (9,6), (9,5), (9,4), (9,3), (9,2), (9,1),
                    (8,1), (7,1), (7,2), (7,3), (7,4), (7,5), (7,6),
                    (6,7), (5,7), (4,7), (3,7), (2,7), (1,7),
                    (1,8), (2,8), (3,8), (4,8), (5,8), (6,8),
                    (7, 8)
                ]
            }

        if BottomRightPlayer:
            players_data[BottomRightPlayer.get_id()] = {
                "startCell": (9, 14),
                "endCell": [(8,14), (8,13), (8,12), (8,11), (8,10)],
                "homeCell": (9, 8),
                "roadCells": [
                    (9,14), (9,13), (9,12), (9,11), (9,10),
                    (10,9), (11,9), (12,9), (13,9), (14,9), (15,9),
                    (15,8), (15,7), (14,7), (13,7), (12,7), (11,7), (10,7),
                    (9,6), (9,5), (9,4), (9,3), (9,2), (9,1),
                    (8,1), (7,1), (7,2), (7,3), (7,4), (7,5), (7,6),
                    (6,7), (5,7), (4,7), (3,7), (2,7), (1,7),
                    (1,8), (1,9), (2,9), (3,9), (4,9), (5,9), (6,9),
                    (7,10), (7,11), (7,12), (7,13), (7,14), (7,15),
                    (8,15), (8,14), (8,13), (8,12), (8,11), (8,10),
                    (8, 9)
                ]
            }

        if BottomLeftPlayer:
            players_data[BottomLeftPlayer.get_id()] = {
                "startCell": (14, 7),
                "endCell": [(14,8), (13,8), (12,8), (11,8), (10,8)],
                "homeCell": (8, 7),
                "roadCells": [
                    (14,7), (13,7), (12,7), (11,7), (10,7),
                    (9,6), (9,5), (9,4), (9,3), (9,2), (9,1),
                    (8,1), (7,1), (7,2), (7,3), (7,4), (7,5), (7,6),
                    (6,7), (5,7), (4,7), (3,7), (2,7), (1,7),
                    (1,8), (1,9), (2,9), (3,9), (4,9), (5,9), (6,9),
                    (7,10), (7,11), (7,12), (7,13), (7,14), (7,15),
                    (8,15), (9,15), (9,14), (9,13), (9,12), (9,11), (9,10),
                    (10, 9), (11, 9), (12, 9), (13, 9), (14, 9), (15, 9),
                    (15,8), (14,8), (13,8), (12,8), (11,8), (10,8),
                    (9, 8)
                ]
            }

        return players_data



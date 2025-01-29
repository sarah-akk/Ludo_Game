from cell import Cell
from constants import Constants
from player import Player
from rich.console import Console


console = Console()
class Grid:
    def __init__(self, TopLeftPlayer: Player , TopRightPlayer: Player , BottomRightPlayer: Player , BottomLeftPlayer: Player ):
        corners_indices = Constants().get_corners_indices(TopLeftPlayer, TopRightPlayer, BottomRightPlayer, BottomLeftPlayer)
        home_base_indices = Constants().get_home_base_indices()
        start_indices = Constants().get_start_indices(TopLeftPlayer, TopRightPlayer, BottomRightPlayer, BottomLeftPlayer)
        end_indices = Constants().get_end_indices(TopLeftPlayer, TopRightPlayer, BottomRightPlayer, BottomLeftPlayer)
        indices = []
        indices.extend(corners_indices)
        indices.extend(home_base_indices)
        indices.extend(start_indices)
        indices.extend(end_indices)

         # Store players and their pawns
        self.players = [player for player in [TopLeftPlayer, TopRightPlayer, BottomRightPlayer, BottomLeftPlayer] if player is not None]
        players_data = Constants.players_indices(TopLeftPlayer , TopRightPlayer , BottomRightPlayer, BottomLeftPlayer)
        
        
        for player in self.players:
            player_id = player.get_id()
            p_data = players_data.get(player_id)
            player.set_indices(p_data)

        self.grid = []
        # Create the grid
        for x in range(Constants().get_grid_size()):
            raw = []
            for y in range(Constants().get_grid_size()):
                cell_data = self.find_cell_data(indices, x, y)
                # cell_data[3] is the player_id
                raw.append(Cell(x=cell_data[0], y=cell_data[1], color=cell_data[2],type=cell_data[3]))
            self.grid.append(raw)
        self.set_pawns_on_grid()

        

    def set_pawns_on_grid(self):
        """Set pawns on the grid by matching their positions with the grid cells."""
        for row in self.grid:
            for cell in row:
                for player in self.players:
                    for pawn in player.get_pawns():
                        if cell.x == pawn.x and cell.y == pawn.y:
                            pawn.set_cell(cell)



    def get_pawn_symbol_at_cell(self, x, y):
        for player in self.players:
            for pawn in player.get_pawns():
                if pawn.x == x and pawn.y == y:
                    return pawn.symbol  
        return None
    
    def get_pawns_at_cell(self, x, y):
        pawns = []
        for player in self.players:
            for pawn in player.get_pawns():
                if pawn.x == x and pawn.y == y:
                    pawns.append(pawn)
        return pawns
    

    def draw(self):
        for row in self.grid:
            for cell in row:
                color = cell.get_color()
                pawns_here = []
                for player in self.players:
                    for i_pawn in player.get_pawns():
                        pawn_cell = i_pawn.get_cell()
                        if(pawn_cell == cell):
                            pawns_here.append(i_pawn)
                
                pawn_symbol = self.get_pawn_symbol_at_cell(cell.x, cell.y)
                if(len(pawns_here) > 1):
                   console.print(pawns_here[0].get_symbol() + pawns_here[1].get_symbol() , end="")
                   continue
                if pawn_symbol:
                    console.print(" " + pawn_symbol , end="")
                elif color == Constants.Color.WHITE :
                    print("⬜", end="")
                elif color == Constants.Color.RED:
                    print("🟥", end="")
                elif color == Constants.Color.GREEN:
                    print("🟩", end="")
                elif color == Constants.Color.YELLOW:
                    print("🟨", end="")
                elif color == Constants.Color.BLUE:
                    print("🟦", end="")
                elif color == Constants.Color.BLACK:
                    print("⬛", end="")
                elif color == Constants.Color.BROWN:
                    print("🟫", end="")
                else:
                    print("❔", end="")
            print()  # New line after each row

    def find_cell_data(self, indices, x, y):
        for index in indices:
            if (x + 1, y + 1) == (index[0], index[1]):
                # x y color player_id type
                return (index[0], index[1], index[2], index[3],)
            # todo the type is road
        return (x + 1, y + 1, Constants.Color.WHITE, Constants.Type.ROAD)
    


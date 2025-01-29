from dice import Dice
from player import Player
from constants import Constants
from cell import Cell
from time import sleep
from state import State
import pygame

RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
PURPLE = "\033[95m"
CYAN = "\033[96m"
RESET = "\033[0m"
GRAY = "\033[90m"
BOLD = "\033[1m"
PINK = "\033[38;2;255;182;193m"
BRIGHT_RED = "\033[38;2;255;69;0m"

class Game:
    def __init__(self, TopLeftPlayer, TopRightPlayer, BottomRightPlayer, BottomLeftPlayer, grid):
        # Initialize players
        self.players = [player for player in [TopLeftPlayer, TopRightPlayer, BottomRightPlayer, BottomLeftPlayer] if player is not None]
        self.current_turn = 0  
        self.dice = Dice()
        self.grid = grid
        self.current_player = None

        print(f"{CYAN}================================================{RESET}")
        print(f"{PINK}      📱📍⛳  Welcome to Ludo!  🎯🎲💥      {RESET}")
        print(f"{CYAN}================================================{RESET}")

        self.grid.draw()



###################################################################################################

    def roll_dice(self):
        """Roll the dice and return the result."""
        return self.dice.roll()  

###################################################################################################        return True

    def move_pawn(self, pawn_id, current_player, roll_result):
        """
        Moves the pawn with the given ID based on the roll result.
        
        Args:
            pawn_id (int): The ID of the pawn to move.
            roll_result (int): The result of the dice roll.
        """
        capture_opponent = False
        for pawn in current_player.get_pawns():
            if pawn.id == pawn_id:
                current_cell = pawn.get_cell()
                
                if current_cell.get_type() == Constants.Type.CORNER:
                    start_cell_coords  = current_player.get_start_cell()
                    x, y = start_cell_coords
                    start_cell = self.grid.grid[x - 1][y - 1]
                    if start_cell:
                        pawn.set_cell(start_cell)

                    print(f"{YELLOW}Pawn {pawn_id % 10} moved to START.{RESET}")
                else:
                    # todo correct the logic
                    road_cells = current_player.get_road_cells()
                    
                    # print(pawn)

                    current_index = road_cells.index((current_cell.x , current_cell.y))  
                    
                    target_index = current_index + roll_result
                    
                    if target_index < len(road_cells):
                        target_cell_x , target_cell_y = road_cells[target_index]
                        target_cell = self.grid.grid[target_cell_x - 1][target_cell_y - 1]
                        print(f"{GREEN}Pawn {pawn_id % 10} moved to position {target_cell}.{RESET}")
                        
                        if(target_cell.get_type() == Constants.Type.ROAD):
                            
                            other_players_pawns_in_target_cell = []
                            
                            for other_player in self.players:
                                if(other_player.get_id() != current_player.get_id()):
                                    for loop_pawn in other_player.get_pawns():
                                        pawn_cell = loop_pawn.get_cell() 
                                        if(pawn_cell.x == target_cell.x and pawn_cell.y == target_cell.y):
                                            other_players_pawns_in_target_cell.append(loop_pawn)
                            
                            if other_players_pawns_in_target_cell:
                                    self.capture_opponent_pawns(other_players_pawns_in_target_cell)
                                    capture_opponent = True
                            
                        pawn.set_cell(target_cell)
                        return capture_opponent
                return
        
        print(f"{RED}Error: Pawn with ID {pawn_id % 10} not found.{RESET}")

###################################################################################################

    def get_possible_moves(self,current_player, roll_result):
        possible_moves = []
        road_cells = current_player.get_road_cells()
        for pawn in current_player.get_pawns():
            current_cell = pawn.get_cell()
            
            if current_cell.get_type() == Constants.Type.CORNER:
                if roll_result == 6:
                    possible_moves.append(pawn.id)
                continue
            
            
            current_index = road_cells.index((current_cell.x , current_cell.y))

            target_index = current_index + roll_result
            # print(target_index)
            if target_index < len(road_cells):
                target_cell_x , target_cell_y = road_cells[target_index]
                if  self.is_valid_move(target_cell_x , target_cell_y, pawn):
                    possible_moves.append(pawn.id)
                    continue
            
            # if current_cell.get_type() == Constants.Type.END:
            #     if current_cell.distance_to_finish() == roll_result:
            #         possible_moves.append(pawn.id)
            #     continue
            
            #todo 
            #if there is no wall in the road add pawn.id
            
            # if self.can_player_move(pawn.id):
            #     possible_moves.append(pawn.id)
        
        return possible_moves

###################################################################################################

    def is_valid_move(self, target_cell_x , target_cell_y, pawn):
        target_cell = self.grid.grid[target_cell_x - 1 ][ target_cell_y - 1]
        current_cell = pawn.get_cell()
        player = None
        for loop_player in self.players:
            if pawn in loop_player.get_pawns():
                player = loop_player
                
        player_road_cells = player.get_road_cells()
        
        if(current_cell.get_type() == Constants.Type.END and target_cell.get_type() == Constants.Type.END):
            print('you cant move from end to end cell')
            return False

        # 1. Get indices of the current cell and target cell
        try:
            current_index = player_road_cells.index((current_cell.x,current_cell.y))
            target_index = player_road_cells.index((target_cell_x , target_cell_y))
        except ValueError:
            return False  # Either cell is not part of the road cells

        # 2. Check cells between the current cell and the target cell
        step = 1 if target_index > current_index else -1
        #chick the range [[ todo ]]
        for i in range(current_index + step, target_index , step):
            intermediate_cell_x , intermediate_cell_y = player_road_cells[i]
            intermediate_cell = self.grid.grid[intermediate_cell_x - 1 ][intermediate_cell_y - 1]

            # Check if the intermediate cell has a wall (2+ pawns of the same player)
            #loop over all players [[ todo ]]
            for loop_player in self.grid.players :
                loop_player_pawns = []
                for pawn in loop_player.get_pawns() :
                    pawn_cell = pawn.get_cell()
                    if pawn_cell.x == intermediate_cell.x and pawn_cell.y == intermediate_cell_y:
                        loop_player_pawns.append(pawn)
                        if len(loop_player_pawns) >= 2:
                            print(f"{PINK}Cannot pass through a wall at cell {intermediate_cell}.{RESET}")
                            return False
        return True

###################################################################################################
#     
    def capture_opponent_pawns(self, pawns):
        """
        Capture all opponent pawns in a cell and send them back to the first available starting position.

        Args:
            pawns (list[Pawn]): List of opponent pawns to capture.
        """
        for pawn in pawns:
                prev_cell = pawn.get_cell()
                corner_cell = self.grid.grid[pawn.corner_x - 1][pawn.corner_y - 1]
                pawn.set_cell(corner_cell)
                print(f"{RED}{pawn} captured from {prev_cell} to {corner_cell}{RESET}")


 ###################################################################################################
    
    def play(self):
        """Main game loop."""
        while True:
                        
            # Current player turn
            self.current_player = self.players[self.current_turn % len(self.players)]
            
            # print('self curr_player' , self.current_player.get_id())
        
            print(f"{self.current_player.get_symbol()}It's {self.current_player.get_name()}'s turn!{RESET}")
            
            consecutive_sixes = 0
            
            while True:
                # Dice roll
                roll_result = self.roll_dice()
                print(f"{self.current_player.get_symbol()}{self.current_player.get_name()} rolled a {roll_result}.{RESET}")

                # Get possible moves for the roll
                possible_moves = self.get_possible_moves(self.current_player, roll_result)

                if possible_moves:
                    last_digits = [num % 10 for num in possible_moves]
                    print(f"{CYAN}Possible moves: {last_digits}{RESET}")

                    # Validate the pawn_id input
                    pawn_id = None
                    while pawn_id not in [num % 10 for num in possible_moves]:
                        pawn_id = self.current_player.input_pawn_id(self , possible_moves , roll_result)
                        pygame.mixer.Sound("sounds/click.mp3").play()  

                        try:
                            pawn_id = int(pawn_id)  # Ensure it's an integer
                        except ValueError:
                            print(f"{BRIGHT_RED}Invalid input! Please enter a numeric pawn ID.{RESET}")
                            continue  # Retry if the input is not an integer

                        matching_pawn_id = next((num for num in possible_moves if num % 10 == pawn_id), None)
                        if matching_pawn_id is None:
                            print(f"{RED}Invalid move! The pawn ID {pawn_id % 10} is not in possible moves. Try again.{RESET}")

                    # Move the pawn
                    capture_opponent = self.move_pawn(matching_pawn_id, self.current_player, roll_result)
                    if capture_opponent:
                        self.current_turn-=1
                else:
                    print(f"{GRAY}No possible moves for {self.current_player.get_name()} this turn.{RESET}")
                
                self.grid.draw()
                
                if self.check_win(self.current_player): 
                    print(f"{GREEN}Congratulations! ️⛳️🎉 {self.current_player.get_name()} has won the game!{RESET}")
                    return

                if roll_result == 6:
                    consecutive_sixes += 1
                    if consecutive_sixes == 3:
                        print(f"{self.current_player.get_symbol()}{self.current_player.get_name()} rolled three 6s in a row. Turn ends!{RESET}")
                        break  # End turn after rolling 6 three times
                else:
                    consecutive_sixes = 0
                    break

            # Increment the turn
            self.current_turn += 1

 ###################################################################################################           
    def check_win(self, player): 
        home_cell_x, home_cell_y = player.get_home_cell() 
        for pawn in player.get_pawns(): 
            pawn_cell = pawn.get_cell() 
            if pawn_cell.x != home_cell_x or pawn_cell.y != home_cell_y: 
                return False 
        return True



    


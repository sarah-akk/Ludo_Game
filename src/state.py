import copy
from constants import Constants
class State:
    def __init__(self , game):
        self.c_game = copy.deepcopy(game)

#################################################################################################
        
    def evaluate(self , max_player = None):
        
        if(max_player == None) :
            max_player = self.c_game.current_player
        
        add = 0
        sub = 0
        # add
        add += self.evaluateSinglePlayer(max_player)
        
        # sub
        #the same roles for add but for other players
        for player in self.c_game.grid.players:
            if(player.get_id() != max_player.get_id()):
                sub += self.evaluateSinglePlayer(player)
                                
        # res = add - sub / max((len(self.c_game.players) - 1) , 1)
        res = add - sub # the game terminated if one player win
                 
        return res

 #################################################################################################
 #    
    def evaluateSinglePlayer(self , player):
        #take into consideration the the safe cells to be more valuable
        #if home base and my_pawns count * number
        #if road and my_pawns if count == one add the rank
        #if road and more than one add rank * count + add more if others pawn are behind
        valuation = 0 
        
        cell_types_points = {
            Constants.Type.CORNER : 10 ,
            Constants.Type.HOME_BASE : 600 ,
            Constants.Type.START : 1 ,
            Constants.Type.END : 100  ,
            Constants.Type.ROAD : 0 , #based one the player_cell index , #handle if some one behind me
        }
        
        index_strength = 2
        
        road = player.get_road_cells()
        
        all_pawns = []
        
        for ply in self.c_game.players:
            all_pawns.extend(ply.get_pawns())
        
        for pawn in player.get_pawns():
            cell = pawn.get_cell()
            cell_type = cell.get_type()
            valuation += cell_types_points[cell_type]
            if(cell_type in [Constants.Type.ROAD , Constants.Type.START , Constants.Type.END]):
                index = road.index((cell.x , cell.y))
                valuation += (index + 1) * index_strength 
            if(cell_type in [Constants.Type.ROAD , Constants.Type.START]):
                #if there is a enemy infront if me and the dist < 6 : i can kill him add the value of what he could lose 
                #if i and infront of him and he could kill me , sub of road , add if start to stay here
                
                start = max(index - 6, 0)
                end = min(index + 6, len(road))
                
                for i in range(start , end + 1):
                    x , y = road[i]
                    
                    if(i > index):
                        pass
                    elif(i < index) :
                        pass
                    else :
                        if cell_type == Constants.Type.ROAD:
                            pass
                pass
        
        return valuation

#################################################################################################
    
    def new_state(self , move , roll_res):
        copy_game = copy.deepcopy(self.c_game)
        curr_player = copy_game.current_player
        all_players = copy_game.players
        curr_player_index = all_players.index(curr_player)
        
        
        capture_pawns = copy_game.move_pawn(move , copy_game.current_player , roll_res)
        
        if not capture_pawns:
            print('not capture pawns')

            next_player = all_players[(curr_player_index + 1 ) % len(all_players)]
        else:
            next_player = all_players[curr_player_index]
            

        # print(copy_game.current_player.get_id() , 'before change')
        # copy_game.current_player = next_player

    
        # print(copy_game.current_player.get_id() , 'player id')
            
        newState = State(copy_game)
                    
        return newState

#################################################################################################
#    
    def is_terminated(self , roll_res):
        return len(self.c_game.get_possible_moves(self.c_game.current_player , roll_res)) <= 0
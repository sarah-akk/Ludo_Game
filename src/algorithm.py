import math
class Algorithm:
        
    def __init__(self):
        pass
            
    
    def expectiminmax(self , state , is_chance = False , roll_res = 0 , depth = 1 , max_player = None):

        #The chance node returns the expected value to the parent decision node.
        #The decision node selects the move with the highest value (for maximizing player).
        
        # print('depth ' , depth)
    
        if(depth <= 0 or state.is_terminated(roll_res)):
            return state.evaluate(max_player)

        res = 0
        
        if is_chance:
            #For each move, the algorithm evaluates all possible dice rolls [1, 2, 3, 4, 5, 6] and calculates the expected value.       
            for i in range(1 , 7):
                res += self.expectiminmax(
                    state= state , 
                    is_chance= False , 
                    roll_res= i , 
                    depth= depth , # no depth sub in the chance node  
                    max_player= max_player
                ) / state.c_game.dice.get_probability(i)
            return res
        
        #get all moves based on the roll res
        is_max = state.c_game.current_player.get_id() == max_player.get_id()
        
        moves = state.c_game.get_possible_moves(state.c_game.current_player , roll_res)
        
        if(len(moves) <= 0):
            return state.evaluate()
        
        for move in moves:
            #get the max of them
            newState = state.new_state(move,roll_res)
            
            # newstate.c_game.grid.draw()
            
            value = self.expectiminmax(
                        state= newState , 
                        is_chance= True , 
                        roll_res= roll_res ,
                        depth= depth - 1 , 
                        max_player= max_player
                    ) 
                     
            if is_max :
                res = max(value, res)
            else :
                res = min(value, res)
                
        return res
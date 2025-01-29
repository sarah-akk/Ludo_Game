import random

class Dice:
    outcomes = [1, 2, 3, 4, 5, 6]
    weights = [1, 1, 1, 1, 1, 1]
    
    def __init__(self , _outcomes = None , _weights = None):
        if(_outcomes):
            self.outcomes = _outcomes
        if(_weights):
            self.weights = _weights
        pass
    
    def get_probability(outcome, weights):
        total_weight = sum(weights)
        outcome_index = outcome - 1  # Convert outcome (1-6) to index (0-5)
        return weights[outcome_index] / total_weight

    def roll(self):
        return random.choices(self.outcomes, weights=self.weights, k=1)[0]

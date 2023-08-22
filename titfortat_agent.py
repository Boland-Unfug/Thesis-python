#This file contains the titfortat agent class.

import agent

class titfortat(agent.Agent):
    """
    The titfortat class is a subclass of the Agent class.
    It inherits the score, the memory functions, and the helper functions of the Agent class.
    Its strategy is to cooperate on the first move, then copy the opponent's previous move.
    """
    
    def __init__(self):
        """
        The constructor for the titfortat class.
        It sets the score of the agent to 0.
        """
        self.score = 0

    def play(self):
        """
        The play method returns the move of the agent.
        It returns 'C' for cooperate.
        """
        if len(self.opponent_memory) == 0:
            return 'C'
        return self.opponent_memory[0] #starting off with only one move in memory
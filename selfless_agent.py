#This file contains the selfish agent class.

import agent

class selfless(agent.Agent):
    """
    The selfless class is a subclass of the Agent class.
    It inherits the score, the memory functions, and the helper functions of the Agent class.
    Its strategy is to always cooperate.
    """
    
    def __init__(self):
        """
        The constructor for the selfish class.
        It sets the score of the agent to 0.
        """
        self.score = 0

    def play(self):
        """
        The play method returns the move of the agent.
        It returns 'C' for defect.
        """
        return 'C'
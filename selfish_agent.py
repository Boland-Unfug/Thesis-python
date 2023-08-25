#This file contains the selfish agent class.

import agent

class Selfish(agent.Agent):
    """
    The selfish class is a subclass of the Agent class.
    It inherits the score, the memory functions, and the helper functions of the Agent class.
    Its strategy is to always defect.
    """
    def __init__(self, name):
        """
        The constructor for the selfish class.
        It sets the score of the agent to 0.
        """
        self.name = name
        self.score = 0

    def strategy(self, opponent):
        """
        The play method returns the move of the agent.
        It returns 'D' for defect.
        """
        return 'D'

    def __str__(self):
        return "Selfish"
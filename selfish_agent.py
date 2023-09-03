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

    def strategy(self, opponent, round_number):
        """
        The play method returns the move of the agent.
        It returns 1 for defect.
        """
        return 1

    def __str__(self):
        return "Selfish"
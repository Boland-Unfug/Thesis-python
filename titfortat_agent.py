#This file contains the titfortat agent class.

import agent

class Titfortat(agent.Agent):
    memory = []
    """
    The titfortat class is a subclass of the Agent class.
    It inherits the score, the memory functions, and the helper functions of the Agent class.
    Its strategy is to cooperate on the first move, then copy the opponent's previous move.
    """
    def __init__(self, name):
        """
        The constructor for the titfortat class.
        It sets the score of the agent to 0.
        """
        self.name = name

    def strategy(self, opponent, round_number):
        """
        The play method returns the move of the agent.
        If it is the first round, it returns 0 for cooperate.
        """
        game = self.create_hash(round_number-1, self.name, opponent) # get the previous game
        if game == 2 or game == 4: # if the opponent defected last round, defect
            return 1
        else: # otherwise, cooperate
            return 0


    def __str__(self):
        return "Titfortat"
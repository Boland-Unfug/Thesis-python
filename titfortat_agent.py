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
        self.score = 0
        self.memory = []

    def strategy(self, opponent):
        """
        The play method returns the move of the agent.
        It returns 'C' for cooperate.
        """
        if self.memory == []:
            return 'C'
        print(self.memory)

        self.memory.reverse()
        for agent1, play_1, agent2, play_2 in self.memory:
            if agent1 == opponent:
                self.memory.reverse()
                return play_1
            elif agent2 == opponent:
                self.memory.reverse()
                return play_2
        self.memory.reverse()
        return 'C'

    def __str__(self):
        return "Titfortat"
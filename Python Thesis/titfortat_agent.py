#This file contains the titfortat agent class.

import agent
class Titfortat(agent.Agent):
    """
    The titfortat class is a subclass of the Agent class.
    It inherits the score, the memory functions, and the helper functions of the Agent class.
    Its strategy is to cooperate on the first move, then copy the opponent's previous move.
    """
    def __init__(self, name, game_instance):
        """
        The constructor for the titfortat class.
        It sets the score of the agent to 0.
        """
        self.name = name
        self.game_instance = game_instance

    def strategy(self):
        """
        The play method returns the move of the agent.
        If it is the first round, it returns 0 for cooperate.
        """
        # check games until you find the previous game
        #TODO: make the code easier to read
        prev_game = self.game_instance.get_specific_recent_history(self.name)
        if prev_game != None:
            #print("Previous game found")
            if prev_game[1] == 0 or prev_game[1] == 2:
                return 1
            else:
                return 0
        else:
            #print("Error: No previous game found")
            return 0

    def __str__(self):
        return super().__str__() + " Titfortat"

    def get_strategy(self):
        return "Titfortat"

    def get_movement_strategy(self):
        return "Random"
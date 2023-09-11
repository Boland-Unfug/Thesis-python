# This file contains the game class.

import agent
import world

import time
import pygame

class Game():
    #TODO: possibly add a way to get a cells full game history
    """
    A class representing a game object that keeps track of the game history.
    Also contains the rules of the game, the payoff matrix, and the state matrix.
    """

    payoff_matrix = {
        (0, 0): (3, 3),  # Cooperate/Cooperate
        (0, 1): (0, 5),  # Cooperate/Defect
        (1, 0): (5, 0),  # Defect/Cooperate
        (1, 1): (1, 1)   # Defect/Defect
        }

    state_matrix = {
        (0, 0): 1,  # Cooperate/Cooperate
        (0, 1): 2,  # Cooperate/Defect
        (1, 0): 3,  # Defect/Cooperate
        (1, 1): 4   # Defect/Defect
        }
    
    def __init__(self, rounds=100000):
        """
        Initializes the game object.
        The game object is primarily responsible for keeping track of the game history.
        The game history is a dictionary of all games played, with the key being a hash of the game.

        Parameters:
        rounds (int): The number of rounds to play.

        Returns:
        None
        """

        self.history = {} # max size of possible games is 4,294,967,296 (one full 32 bit integer)
        self.recent_history = {} # a dictionary of the last game for each agent

        self.rounds = rounds
        self.round_number = 0



    def play(self, agent, neighbor, collision_point):
        """
        Plays a game between two agents and updates the game history and scores.

        Parameters:
        agent (Agent): The first agent to play.
        neighbor (Agent): The second agent to play.
        collision_point (tuple): The collision point of the two agents.

        Returns:
        None
        """

        # sort the agents by name
        sorted_agents = sorted([agent.get_name(), neighbor.get_name()])
        # create a hash of the game
        game_hash = Game.create_hash(self.get_round(), sorted_agents[0], sorted_agents[1])
        # check if the game has been played before
        if game_hash not in self.history:
            # play the game
            # get agent moves
            play_1 = agent.strategy()
            play_2 = neighbor.strategy()
            # get the resulting state
            state = self.get_state(play_1, play_2)
            # add the game to the history
            self.history[game_hash] = state, collision_point, agent.get_score(), neighbor.get_score()
            # print("Game played: " + str(game_hash))
            # print("Collision point: " + str(collision_point))
            self.recent_history[agent.get_name()] = state, collision_point, self.get_round()
            # get resulting scores
            score_1, score_2 = Game.get_payoff(play_1, play_2)
            # update the scores for the agents, remember they have been sorted
            agent.set_score(agent.get_score() + score_1)
            neighbor.set_score(neighbor.get_score() + score_2)

    @staticmethod
    def create_hash(round_number, agent1, agent2):
        """
        Creates a hash of the game.

        Parameters:
        round_number (int): The current round number.
        agent1 (str): The name of the first agent.
        agent2 (str): The name of the second agent.

        Returns:
        int: The hash of the game.
        """

        return (round_number << 40) + (agent1 << 20) + agent2

    @staticmethod
    def get_payoff(action_1, action_2):
        """
        Gets the payoff for the two actions.

        Parameters:
        action_1 (int): The action of the first agent.
        action_2 (int): The action of the second agent.

        Returns:
        tuple: The payoff for the two actions.
        """

        return Game.payoff_matrix[(action_1, action_2)]

    @staticmethod
    def get_state(action_1, action_2):
        """
        Gets the state for the two actions.

        Parameters:
        action_1 (int): The action of the first agent.
        action_2 (int): The action of the second agent.

        Returns:
        int: The state for the two actions.
        """

        return Game.state_matrix[(action_1, action_2)]

    def get_history(self):
        """
        Gets the game history.

        Returns:
        dict: The game history.
        """

        return self.history

    def get_specific_history(self, game_hash):
        """
        Gets the specific game history for the given game hash.

        Parameters:
        game_hash (int): The hash of the game.

        Returns:
        tuple: The specific game history for the given game hash.
        None if the game hash is not in the history.
        """

        if (game_hash in self.history):
            return self.history[game_hash]
        return None

    def get_recent_history(self):
        """
        Gets the recent game history.

        Returns:
        dict: The recent game history.
        """

        return self.recent_history

    def get_specific_recent_history(self, agent_name):
        """
        Gets the specific recent game history for the given agent name.

        Parameters:
        agent_name (int): The name of the agent.

        Returns:
        tuple: The specific recent game history for the given agent name.
        None if the agent name is not in the recent history.
        """

        if (agent_name in self.recent_history):
            return self.recent_history[agent_name]
        return None
    

    def get_rounds(self):
        """
        Gets the number of rounds.

        Returns:
        int: The number of rounds.
        """

        return self.rounds

    def get_round(self):
        """
        Gets the current round number.

        Returns:
        int: The current round number.
        """

        return self.round_number
        
# This file contains the game class.

import agent
import world

import time
import pygame

class Game():
    """
    The game class manages the payoff matrix, and includes helper functions for playing games between agents and groups.
    it also includes several methods:
    play() plays the game between all agents, calling play_neighbors() for each agent
    play_neighbors() plays the game between an agent and its neighbors, calling duel() for each neighbor
    duel() plays the game between two agents, calling prisoners_dillema() for the payoff
    prisoners_dillema() plays the prisoners dillema game between two agents, returning the score of the two moves
    """


    
    def __init__(self, agents, rounds):

        """
        The constructor for the game class.
        It sets the payoff matrix, the state matrix, and the history of the game.
        """
        self.history = {} # max size of possible games is 4,294,967,296 (one full 32 bit integer)

        self.payoff_matrix = {
        (0, 0): (3, 3),  # Cooperate/Cooperate
        (0, 1): (0, 5),  # Cooperate/Defect
        (1, 0): (5, 0),  # Defect/Cooperate
        (1, 1): (1, 1)   # Defect/Defect
        }

        self.state_matrix = {
        (0, 0): 1,  # Cooperate/Cooperate
        (0, 1): 2,  # Cooperate/Defect
        (1, 0): 3,  # Defect/Cooperate
        (1, 1): 4   # Defect/Defect
        }
        self.rounds = rounds
        self.round_number = 0
        self.agents = agents


    def play(self, agent, neighbor):
        """
        The duel method plays the game between two agents.
        It takes in two agents and plays the game between them.
        """

        # sort the agents by name
        sorted_agents = sorted([agent.get_name(), neighbor.get_name()])
        # create a hash of the game
        game_hash = self.create_hash(self.get_round(), sorted_agents[0], sorted_agents[1])
        # check if the game has been played before
        if game_hash not in self.history:
            # play the game
            # get agent moves
            play_1 = agent.strategy(neighbor.get_name(), self.get_round())
            play_2 = neighbor.strategy(agent.get_name(), self.get_round())
            # get the resulting state
            state = self.get_state(play_1, play_2)
            # add the game to the history
            self.history[game_hash] = state
            # get resulting scores
            score_1, score_2 = self.get_payoff(play_1, play_2)
            # update the scores for the agents, remember they have been sorted
            self.agents[sorted_agents[0]].change_score(score_1)
            self.agents[sorted_agents[1]].change_score(score_2)

    def create_hash(self, round_number, agent1, agent2):
        """
        The create_hash method creates a hash of the game.
        It takes in the round number and the names of the two agents, which are sorted by name.
        It returns the hash of the game.
        The bit shifts are to make sure that the hash is unique
        # 24 bits for rounds, max:16,777,216 (1 round for movement, 9 rounds for drifting)
        # 20 bits for agent1, max:1,048,576
        # 20 bits for agent2
        """
        return (round_number << 40) + (agent1 << 20) + agent2
        

    def get_payoff(self, action_1, action_2):
        """
        @param action_1: the action of the first agent
        @param action_2: the action of the second agent
        @return: the payoff of the two actions
        Payoff matrix:
        (0, 0): (3, 3),  # Cooperate/Cooperate
        (0, 1): (0, 5),  # Cooperate/Defect
        (1, 0): (5, 0),  # Defect/Cooperate
        (1, 1): (1, 1)   # Defect/Defect
        """
        return self.payoff_matrix[(action_1, action_2)]

    def get_state(self, action_1, action_2):
        """
        @param action_1: the action of the first agent
        @param action_2: the action of the second agent
        @return: the state of the two actions
        State matrix:
        (0, 0): 1,  # Cooperate/Cooperate
        (0, 1): 2,  # Cooperate/Defect
        (1, 0): 3,  # Defect/Cooperate
        (1, 1): 4   # Defect/Defect
        """
        return self.state_matrix[(action_1, action_2)]

    def get_history(self):
        """
        The get_history method returns the history of the games played.
        """
        return self.history

    def get_rounds(self):
        """
        The get_rounds method returns the number of rounds played.
        """
        return self.rounds

    def get_round(self):
        """
        The get_round method returns the current round.
        """
        return self.round_number
        
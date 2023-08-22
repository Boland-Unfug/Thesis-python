# This file contains the game class.

import agent
import world

class Game():
    """
    The game class contains the world and the agents.
    It contains the following methods:
    get_world() returns the world
    get_agents() returns the agents
    play() plays the game
    """
    world = world.World()
    agents = world.get_agents()
    
    def __init__(self, world, agents):
        """
        The constructor for the game class.
        It creates a world and adds agents to it.
        """
        self.world = world
        self.agents = agents

    def play(self):
        """
        The play method plays the game.
        It iterates through the agents and plays the game.
        """
        for agent in self.agents:
            for neighbors in agent.get_neighbors():
                play_1 = agent.strategy()
                play_2 = neighbors.strategy()
                print(agent, "played", play_1, "and", neighbors, "played", play_2)
                score_1, score_2 = self.prisoners_dillema(play_1, play_2)
                agent.change_score(score_1)
                neighbors.change_score(score_2)
                agent.forget()
                neighbors.forget()
                agent.memorize(play_1)
                neighbors.memorize(play_2)
                agent.memorize_opponent(play_2)
                neighbors.memorize_opponent(play_1)


    def prisoners_dillema(self, move_1, move_2):
        """
        The prisoners_dillema method plays the prisoners dillema game.
        It takes in two moves and returns the score of the two moves.
        returns an EOFError if the moves are not valid.
        rules:
        both cooperate: both get 3
        both defect: both get 1
        one cooperates, one defects: cooperator gets 0, defector gets 5
        """
        if move_1 == 'C' and move_2 == 'C':
            return 3, 3
        elif move_1 == 'D' and move_2 == 'D':
            return 1, 1
        elif move_1 == 'C' and move_2 == 'D':
            return 0, 5
        elif move_1 == 'D' and move_2 == 'C':
            return 5, 0
        else:
            return EOFError
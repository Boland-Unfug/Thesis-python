# This file contains the game class.

import agent
import world
import visual

import time
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
        for agent in self.agents:
            self.play_neighbors(agent)

    def play_neighbors(self):
        """
        The play method plays the game.
        It iterates through the agents and plays the game.
        """
        for neighbors in self.agent.get_neighbors():
            print("agent " + str(agent) + " is playing agent " + str(neighbors))
            self.duel(agent, neighbors)


    def duel(self, agent, neighbor):
        """
        The duel method plays the game between two agents.
        It takes in two agents and plays the game between them.
        """

        play_1 = agent.strategy(neighbor.get_memory())
        play_2 = neighbor.strategy(agent.get_memory())
        score_1, score_2 = self.prisoners_dillema(play_1, play_2)
        if (str(agent) == "Titfortat" and str(neighbor) == "Selfish") or (str(agent) == "Selfish" and str(neighbor) == "Titfortat"):
            print("agent " + str(agent) + " is playing agent " + str(neighbor))
            print("agent " + str(agent) + " is playing " + play_1)
            print("agent " + str(neighbor) + " is playing " + play_2)
            time.sleep(5)
        agent.change_score(score_1)
        neighbor.change_score(score_2)
        agent.forget_move()
        neighbor.forget_move()
        agent.memorize(play_1)
        neighbor.memorize(play_2)
        



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
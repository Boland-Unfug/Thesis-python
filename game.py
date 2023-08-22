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
    
    def __init__(self):
        """
        The constructor for the game class.
        It creates a world and adds agents to it.
        """
        self.world = world.World()
        self.agents = self.world.get_agents()

    def play(self):
        """
        The play method plays the game.
        It iterates through the agents and plays the game.
        """
        for i in range(len(self.agents)):
            for j in range(len(self.agents)):
                if i != j:
                    self.agents[i].play(self.agents[j])
                    self.agents[j].play(self.agents[i])
                    self.agents[i].update_memory(self.agents[j])
                    self.agents[j].update_memory(self.agents[i])
                    self.agents[i].update_score()
                    self.agents[j].update_score()
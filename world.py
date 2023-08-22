#This file will contain the world class.

import agent
import titfortat_agent
import selfish_agent
import selfless_agent
import random

class world():
    """
    The world class contains the agents on a grid.
    The grid will start as a 2x2 grid, but can be expanded.
    It contains the following methods:
    get_grid() returns the grid
    get_size() returns the size of the grid
    add_agent() adds an agent to the grid
    """
    size = 2
    grid = []
    agents = []
    def __init__(self):
        """
        The constructor for the world class.
        It creates a 2x2 grid.
        """
        self.grid = [[0 for x in range(self.size)] for y in range(self.size)]
        self.agents = []
        for i in range(self.size):
            for j in range(self.size):
                add_agent()
                self.grid[i][j] = agents[-1]

    def add_agent(self):
        """
        The add_agent method adds an agent to the grid.
        It adds a random agent.
        """
        agent_type = random.randint(0,2)
        if agent_type == 0:
            self.agents.append(titfortat_agent.titfortat())
        elif agent_type == 1:
            self.agents.append(selfish_agent.selfish())
        else:
            self.agents.append(selfless_agent.selfless())

    def get_grid(self):
        """
        The get_grid method returns the grid.
        """
        return self.grid

    def get_size(self):
        """
        The get_size method returns the size of the grid.
        """
        return self.size
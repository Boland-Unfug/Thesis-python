#This file will contain the world class.

import agent
import titfortat_agent
import selfish_agent
import selfless_agent
import random

class World():
    """
    The world class contains the agents on a grid.
    The grid will start as a 3x3 grid, but can be expanded.
    It contains the following methods:
    get_grid() returns the grid
    get_size() returns the size of the grid
    add_agent() adds an agent to the grid
    get_agents() returns the agents
    update_neighbors() returns the neighbors of the agents
    """
    size = 1
    grid = []
    agents = []
    
    def __init__(self, size=3, agents=[]):
        """
        The constructor for the world class.
        It crea
        tes a grid.
        """
        self.size = size
        self.agents = agents
        self.grid = [[None for x in range(self.size)] for y in range(self.size)]
        for i in range(self.agents.__len__()):
            while True:
                x = random.randint(0, self.size-1)
                y = random.randint(0, self.size-1)
                if self.grid[x][y] == None:
                    break
            self.agents[i].set_xy(x, y)
            self.grid[x][y] = self.agents[i]


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

    def get_agents(self):
        """
        The get_agents method returns the agents.
        """
        return self.agents

    def update_neighbors(self):
        """
        The update_neighbors method updates the neighbors of the agents.
        """
        for agent in self.agents:
            neighbors = []
            x, y = agent.get_xy()
            for i in range(x-1, x+2):
                for j in range(y-1, y+2):
                    if (i >= 0 and i < self.size and j >= 0 and j < self.size and (i != x or j != y) and self.grid[i][j] != None):
                        neighbors.append(self.grid[i][j])
            agent.set_neighbors(neighbors)


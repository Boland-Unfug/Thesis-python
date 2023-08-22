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
    
    def __init__(self, size=3):
        """
        The constructor for the world class.
        It crea
        tes a grid.
        """
        self.size = size
        self.grid = [[0 for x in range(self.size)] for y in range(self.size)]
        self.agents = []
        for i in range(self.size):
            for j in range(self.size):
                self.add_agent()
                self.grid[i][j] = self.agents[-1]

    def add_agent(self):
        """
        The add_agent method adds an agent to the grid.
        It adds a random agent.
        """
        agent_type = random.randint(0,2)
        if agent_type == 0:
            self.agents.append(selfless_agent.Selfless())
        elif agent_type == 1:
            self.agents.append(selfish_agent.Selfish())
        else:
            self.agents.append(titfortat_agent.Titfortat())

    

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
        for i in range(self.size):
            for j in range(self.size):
                current_agent = self.grid[i][j]
                neighbors = []
                for k in range(i-1, i+2):
                    for l in range(j-1, j+2):
                        if (k >= 0 and k < self.size and l >= 0 and l < self.size and (k != i or l != j)):
                            neighbors.append(self.grid[k][l])
                current_agent.set_neighbors(neighbors)


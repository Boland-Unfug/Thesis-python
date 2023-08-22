# This file contains the visualizer class.

import game
import agent
import world

import sys
import pygame
from pygame.locals import *
import numpy as np

class Visual():
    """
    The visual class visualizes the world and the agents.
    It contains the following methods:
    print_world() prints the world
    print_agents() prints the agents
    """

    world = world.World()
    agents = world.get_agents()
    grid_size = world.get_size()
    cell_size = 200
    clock = pygame.time.Clock()
    
    def __init__(self, world, agents):
        """
        The constructor for the visual class.
        It creates a world and adds agents to it.
        """
        self.world = world
        self.agents = agents
        grid_size = world.get_size()
        cell_size = 200
        print("Visualizing the world...")
        print("The world is a", grid_size, "by", grid_size, "grid.")
        print("With a width and height of " + str(grid_size * cell_size) + " pixels.")
        pygame.init()
        screen = pygame.display.set_mode((grid_size * cell_size, grid_size * cell_size))
        self.clock = pygame.time.Clock()

        
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            
            for x in range(grid_size):
                for y in range(grid_size):
                    #print(self.world.get_grid()[x][y])
                    color = (0, 0, 0)
                    
                    agent_check = self.world.get_grid()[x][y]
                    agent_check = str(agent_check)
                    if agent_check == "Selfless":
                        color = (0, 255, 0)
                    elif agent_check == "Selfish":
                        color = (255, 0, 0)
                    elif agent_check == "Titfortat":
                        color = (0, 0, 255)
                        
                    pygame.draw.rect(screen, color, (x * cell_size, y * cell_size, cell_size, cell_size))
                    self.update(x, y, self.world.get_grid()[x][y], screen)
            
            pygame.display.flip()
            self.clock.tick(10)


    def update(self, x, y, agent, screen):
        # Your logic for updating the grid according to the Prisoner's Dilemma rules
        font = pygame.font.Font(None, 24)
        text = font.render(str([str(agent),agent.score]), 1, (0,0,0))
        screen.blit(text, (x * self.cell_size, y * self.cell_size))
        pygame.display.flip()

    
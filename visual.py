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
    draw_agents() draws the agents
    draw_agent() draws an agent
    label_agents() labels the agents
    flip() flips the screen
    """
    
    world = None
    agents = None
    cells = None
    cell_size = None
    screen = pygame.display.set_mode((100, 100))
    pygame.display.set_caption("Prisoner's Dilemma")

    def __init__(self, world, agents):
        """
        The constructor for the visual class.
        It creates a world and adds agents to it.
        """
        pygame.init()
        self.world = world
        self.agents = agents
        self.cells = self.world.get_size()
        self.cell_size = 600 / self.cells
        self.screen = pygame.display.set_mode((self.cells * self.cell_size, self.cells * self.cell_size))
        
    def draw_agents(self, screen):
        """
        The draw_agents method draws the agents.
        """
        for i in range(self.cells):
            for j in range(self.cells):
                if self.world.get_grid()[i][j] != None:
                    self.draw_agent(i, j, screen)
                    self.label_agents(i, j, self.world.get_grid()[i][j], screen)
        self.flip()

    def draw_agent(self, x, y, screen):
        color = (255, 255, 255)
        agent_type = str(self.world.get_grid()[x][y])
        
        if agent_type == 'Selfless':
            color = (0, 255, 0)
        elif agent_type == 'Selfish':
            color = (255, 0, 0)
        elif agent_type == 'Titfortat':
            color = (0, 0, 255)
        pygame.draw.rect(screen, color, (x * self.cell_size, y * self.cell_size, self.cell_size, self.cell_size))

    def label_agents(self, x, y, agent, screen):
        font = pygame.font.Font(None, 24)
        # draw points
        text = font.render(str([str(agent), agent.get_score()]), 1, (0,0,0))
        screen.blit(text, (x * self.cell_size, y * self.cell_size))
        pygame.display.flip()

    def flip(self):
        pygame.display.flip()
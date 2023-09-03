#This file will contain the world class.

import agent
import titfortat_agent
import selfish_agent
import selfless_agent
import game

import random
import pygame
import time
class World():
    """
    The world class contains the agents, and manages the world
    """

    # agents will be 10 pixel diameter circles
    # screen will be 600x600 pixels


    def __init__(self, agents=[], world_size=600):
        """
        The constructor for the world class.
        """
        # initialize pygame
        pygame.init()
        # create a screen
        self.world_size = world_size
        self.screen = pygame.display.set_mode((world_size, world_size))
        self.caption = pygame.display.set_caption("Prisoner's Dilemma")
        # create a list of agents
        self.agents = agents
        self.agents_size = 10
        # give each agent a random position
        for agent in self.agents:
            agent.set_position(random.randint(0, world_size), random.randint(0, world_size))

    def draw_background(self, screen):
        """
        The draw_background method draws the background of the world.
        """
        screen.fill((0, 0, 0))

    def draw_agents(self, screen):
        """
        The draw_agents method draws the agents.
        """
        for agent in self.agents:
            if str(agent) == "Selfless":
                pygame.draw.circle(screen, (0, 255, 0), agent.get_position(), self.agents_size)
            elif str(agent) == "Selfish":
                pygame.draw.circle(screen, (255, 0, 0), agent.get_position(), self.agents_size)
            elif str(agent) == "Titfortat":
                pygame.draw.circle(screen, (0, 0, 255), agent.get_position(), self.agents_size)

    def flip(self):
        """
        The flip method flips the screen.
        """
        pygame.display.flip()


    def move_agents(self):
        """
        The move_agents method moves the agents.
        """
        for agent in self.agents:
            position = agent.get_position()
            strategy = agent.move_strategy()
            agent.set_position(position[0] + strategy[0], position[1] + strategy[1])

    def update(self):
        """
        The update method updates the world.
        """
        self.move_agents()
        self.draw_background(self.screen)
        self.draw_agents(self.screen)
        self.flip()

    def collision_detection(self, game):
        """
        The collision_detection method detects collisions between agents.
        """
        # TODO, improve the collision detection and bounce
        for agent in self.agents:
            # boundry collision detection
            if agent.get_position()[0] < 0:
                agent.set_position(0, agent.get_position()[1])
            if agent.get_position()[0] > self.world_size:
                agent.set_position(self.world_size, agent.get_position()[1])
            if agent.get_position()[1] < 0:
                agent.set_position(agent.get_position()[0], 0)
            if agent.get_position()[1] > self.world_size:
                agent.set_position(agent.get_position()[0], self.world_size)
            # circle collision detection
            for other_agent in self.agents:
                if agent != other_agent:
                    agent
                    # X collision
                    x1 = agent.get_position()[0]
                    x2 = other_agent.get_position()[0]
                    # Y collision
                    y1 = agent.get_position()[1]
                    y2 = other_agent.get_position()[1]
                    
                    if (x1 + self.agents_size > x2 - self.agents_size and 
                    x1 - self.agents_size < x2 + self.agents_size and 
                    y1 + self.agents_size > y2 - self.agents_size and 
                    y1 - self.agents_size < y2 + self.agents_size):
                        # play a game between the two agents
                        game.play(agent, other_agent)
                        # bounce them off each other by 5 pixels by finding the difference between their positions and adding/subtracting 5
                        agent.set_position(agent.get_position()[0] + 5, agent.get_position()[1] + 5)
                        other_agent.set_position(other_agent.get_position()[0] - 5, other_agent.get_position()[1] - 5)
        
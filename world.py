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


    def __init__(self, agents=[], world_size=600, game=None):
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
        self.agents_size = 20
        # give each agent a random position
        for agent in self.agents:
            agent.set_position(random.randint(0, world_size), random.randint(0, world_size))
        # create a game
        self.game = game

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
            strategy = agent.get_direction()
            if self.game.round_number % 1 == 0:
                strategy = agent.move_strategy()
                # print(strategy)
            agent.set_direction(strategy[0] * 0.8, strategy[1] * 0.8)
            agent.set_position(position[0] + strategy[0], position[1] + strategy[1])

    def update(self):
        """
        The update method updates the world.
        """
        self.game.round_number += 1
        
        self.move_agents()
        self.collision_detection()
        self.draw_background(self.screen)
        self.draw_agents(self.screen)
        self.flip()

    def collision_detection(self):
        """
        The collision_detection method detects collisions between agents.
        """
        # TODO, improve the collision detection and bounce
        for agent in self.agents:

            # circle collision detection
            for agent2 in self.agents:
                if agent != agent2:
                    agent_position = agent.get_position()
                    agent2_position = agent2.get_position()
                    
                    x_diff = agent2_position[0] - agent_position[0] #This represents the difference in x coordinates.
                    # if x_diff < 0: #If the difference is negative, then the second agent is to the left of the first agent.
                    # if x_diff > 0: #If the difference is positive, then the second agent is to the right of the first agent.
                    y_diff = agent2_position[1] - agent_position[1]

                    if ((x_diff ** 2) + (y_diff ** 2)) <= (self.agents_size * 2)**2 + self.agents_size:

                        agent.set_position(agent.get_position()[0] + self.agents_size, agent.get_position()[1] + self.agents_size)
                        agent.set_direction(agent.get_direction()[0] + (agent.get_direction()[0] - x_diff),
                                            agent.get_direction()[1] + (agent.get_direction()[1] - y_diff))




            # boundry collision detection

            # X collision
            if agent.get_position()[0] - self.agents_size < 0:
                agent.set_position(self.agents_size, agent.get_position()[1])
                agent.set_direction(agent.get_direction()[0] * -1, agent.get_direction()[1])
            if agent.get_position()[0] + self.agents_size> self.world_size:
                agent.set_position(self.world_size - self.agents_size, agent.get_position()[1])
                agent.set_direction(agent.get_direction()[0] * -1, agent.get_direction()[1])
            # Y collision
            if agent.get_position()[1] - self.agents_size < 0:
                agent.set_position(agent.get_position()[0], self.agents_size)
                agent.set_direction(agent.get_direction()[0], agent.get_direction()[1] * -1)
            if agent.get_position()[1] + self.agents_size > self.world_size:
                agent.set_position(agent.get_position()[0], self.world_size - self.agents_size)
                agent.set_direction(agent.get_direction()[0], agent.get_direction()[1] * -1)

            # agent.set_position(agent.get_position()[0] + agent.get_direction()[0], agent.get_position()[1] + agent.get_direction()[1])
                        
                        
                        
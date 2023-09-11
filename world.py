#This file will contain the world class.

import agent
import titfortat_agent
import selfish_agent
import selfless_agent
import game
import data


import random
import pygame
import time
class World():
    #TODO: for now, this class can be poorly designed. We can refactor it later.
    """
    The world class contains the agents, and manages the world
    """

    # agents will be 10 pixel diameter circles
    # screen will be 600x600 pixels


    def __init__(self, agents=[], world_size=600, agents_size= 20, game=None):
        """
        The constructor for the world class.
        """
        # initialize pygame
        pygame.init()
        # create a screen
        self.world_size = world_size
        self.screen = pygame.display.set_mode((self.world_size, self.world_size))
        self.caption = pygame.display.set_caption("Prisoner's Dilemma")
        # create a list of agents
        self.agents = agents
        self.agents_size = agents_size
        # give each agent a random position
        for agent in self.agents:
            agent.set_position([random.randint(0, world_size), random.randint(0, world_size)])
            print(agent.get_position())
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


    def gravity(self, agent):
        """
        The gravity method applies gravity to the agents.
        """
        agent.set_direction([agent.get_direction()[0] * 0.95, agent.get_direction()[1] * 0.95])



    def apply_strategies(self, agent):
        if self.game.round_number % 10 == 0:
            agent.update_direction()


    def move_agents(self):
        """
        The move_agents method moves the agents.
        """
        for agent in self.agents:
            self.apply_strategies(agent)
            self.gravity(agent)
            agent.update_position()
            

    def update(self):
        """
        The update method updates the world.
        """
        if self.game.get_round() < self.game.get_rounds():
            self.game.round_number += 1
            self.draw_background(self.screen)
            self.move_agents()
            self.collision()
            self.draw_agents(self.screen)
            self.flip()


    def collision(self):
        """
        The collision method checks for collisions.
        """
        for agent in self.agents:
            for agent2 in self.agents:
                if agent != agent2:
                    x_difference = agent.get_position()[0] - agent2.get_position()[0]
                    y_difference = agent.get_position()[1] - agent2.get_position()[1]

                    if (x_difference)**2 + (y_difference)**2 <= (((self.agents_size+1) *2 )**2):
                        # calculate a hashable collision point
                        collision_point = [agent.get_position()[0] - x_difference/2, agent.get_position()[1] - y_difference/2]
                        self.game.play(agent, agent2, collision_point=collision_point)
                        
                        # friction
                        agent.set_direction([agent.get_direction()[0] * -1, agent.get_direction()[1] * -1])
                        agent2.set_direction([agent2.get_direction()[0] * -1, agent2.get_direction()[1] * -1])
                        agent.set_position([agent.get_position()[0] + agent.get_direction()[0], agent.get_position()[1] + agent.get_direction()[1]])
                        agent2.set_position([agent2.get_position()[0] + agent2.get_direction()[0], agent2.get_position()[1] + agent2.get_direction()[1]])
                        

            if agent.get_position()[0] - self.agents_size <= 0:
                agent.set_position_x(self.agents_size)
                agent.set_direction_x(agent.get_direction()[0] * -1)
            elif agent.get_position()[0] + self.agents_size >= self.world_size:
                agent.set_position_x(self.world_size - self.agents_size)
                agent.set_direction_x(agent.get_direction()[0] * -1)

            if agent.get_position()[1] - self.agents_size <= 0:
                agent.set_position_y(self.agents_size)
                agent.set_direction_y(agent.get_direction()[1] * -1)
            elif agent.get_position()[1] + self.agents_size >= self.world_size:
                agent.set_position_y(self.world_size - self.agents_size)
                agent.set_direction_y(agent.get_direction()[1] * -1)
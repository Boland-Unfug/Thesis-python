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
        self.agents_size = 15
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


    def gravity(self, agent):
        """
        The gravity method applies gravity to the agents.
        """
        agent.set_direction([agent.get_direction()[0] * 0.8, agent.get_direction()[1] * 0.8])



    def apply_strategies(self, agent):
        if self.game.round_number % 10 == 0:
            agent.set_direction([agent.get_direction()[0] + agent.move_strategy()[0],
                                 agent.get_direction()[1] + agent.move_strategy()[1]])

    def move_agents(self):
        """
        The move_agents method moves the agents.
        """
        for agent in self.agents:
            self.apply_strategies(agent)
            agent.set_position(agent.get_position()[0] + agent.get_direction()[0],
             agent.get_position()[1]  + agent.get_direction()[1])
            self.hit_agents(agent)
            agent.set_position(agent.get_position()[0] + agent.get_direction()[0],
             agent.get_position()[1]  + agent.get_direction()[1])
            self.hit_walls(agent)
            agent.set_position(agent.get_position()[0] + agent.get_direction()[0],
             agent.get_position()[1]  + agent.get_direction()[1])
            self.gravity(agent)
            agent.set_position(agent.get_position()[0] + agent.get_direction()[0],
             agent.get_position()[1]  + agent.get_direction()[1])

    def update(self):
        """
        The update method updates the world.
        """
        if self.game.get_round() < self.game.get_rounds():
            self.game.round_number += 1
            self.draw_background(self.screen)
            self.move_agents()
            self.draw_agents(self.screen)
            self.flip()
        else:
            pygame.quit()
            results = data.Data(self.game, "results.csv")
            results.write_to_file()

    def hit_walls(self, agent):
        """
        The hit_walls method detects if an agent has hit a wall.
        """
        x1, y1 = agent.get_position()
        speed1_x, speed1_y = agent.get_direction()

        hit_wall_x = int(((agent.get_position()[0] - self.agents_size) <= 0) # if the agent is at the left wall
        or ((agent.get_position()[0] + self.agents_size) >= self.world_size)) # if the agent is at the right wall

        hit_wall_y = int((agent.get_position()[1] - self.agents_size <= 0) # if the agent is at the top wall
        or (agent.get_position()[1] + self.agents_size >= self.world_size)) # if the agent is at the bottom wall
        
        agent.set_direction(
        [agent.get_direction()[0] * (-1) ** hit_wall_x, # if the agent hits horizontal wall, reverse the x direction
         agent.get_direction()[1] * (-1) ** hit_wall_y] # if the agent hits vertical wall, reverse the y direction
        )

    def hit_agents(self, agent):
        """
        The hit_agents method detects if an agent has hit another agent.
        """

        x1, y1 = agent.get_position()
        speed1_x, speed1_y = agent.get_direction()

        for other_agent in self.agents:

            x2, y2 = other_agent.get_position()
            speed2_x, speed2_y = other_agent.get_direction()

            if agent != other_agent:
                collision = int((x1 - x2)**2 + (y1 - y2)**2 <= (2*self.agents_size)**2)

                speed1_x *= (-1) ** collision
                speed1_y *= (-1) ** collision
                
                agent.set_direction([speed1_x, speed1_y])
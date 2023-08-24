import sys
import agent
import titfortat_agent
import selfish_agent
import selfless_agent
import world
import game
import visual

import pygame
from pygame.locals import *
import random

def main():
        """
        The main method runs the game.
        """
        size = 3
        agents = []
        # create the agents
        for i in range(size*size):
                agent_type = random.randint(1, 3)

                if agent_type == 1:
                        agents.append(selfless_agent.Selfless(name="agent " + str(i)))
                elif agent_type == 2:
                        agents.append(selfish_agent.Selfish(name="agent " + str(i)))
                elif agent_type == 3:
                        agents.append(titfortat_agent.Titfortat(name="agent " + str(i)))

        # create the world
        game_world = world.World(size=size, agents=agents)
        # create the visual
        game_display = visual.Visual(game_world, agents)
        # display the world
        while True:
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                pygame.quit()
                                sys.exit()
                game_display.draw_agents(game_display.screen)

                

                        # update the neighbors
                game_world.update_neighbors()
                # play the game
                turn = game.Game(game_world, agents)
                # I want to add a loop that allows for me to see each individual game between two agents
                agent_num = 0
                for agent in agents:
                        agent_num += 1
                        neighbor_num = 0
                        for neighbor in agent.get_neighbors():
                                neighbor_num += 1
                                
                                #print the agents position
                                print("agent " + str(agent_num) + " is playing agent " + str(neighbor_num))
                                
                                turn.duel(agent, neighbor)
                                # pygame.time.wait(5000)
                                pygame.display.flip()
                # display the world

                                
                
            
if __name__ == "__main__":
    main()

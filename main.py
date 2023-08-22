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

def main():
        """
        The main method runs the game.
        """
        size = 2
        # create the world
        game_world = world.World(size=size)
        # create the agents
        game_agents = game_world.get_agents()
        # create the visual
        game_display = visual.Visual(game_world, game_agents)
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
                turn = game.Game(game_world, game_agents)
                # I want to add a loop that allows for me to see each individual game between two agents
                agent_num = 0
                for agent in game_agents:
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

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
        iteration = 0
        # create the agents
        for i in range(size*size):
                if (random.randint(0, 1) == 1):
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

                if iteration % 3 == 0:
                        for agent in agents:
                                agent.forget()
                # update the neighbors
                game_world.update_neighbors()
                # play the game
                turn = game.Game(game_world, agents)
                iteration += 1
                print("Iteration: " + str(iteration))
                turn.play()
                game_display.draw_agents(game_display.screen)
                pygame.display.flip()
                pygame.time.wait(1000)



                                
                
            
if __name__ == "__main__":
    main()

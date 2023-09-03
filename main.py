import sys
import random
import time
import pygame

import selfless_agent
import selfish_agent
import titfortat_agent
import game
import world
import agent



def main():
    agents = []
    size = 600
    rounds = 10 # max: 65,536
    
    # create the agents
    for i in range(20):
        agent_type = random.randint(1, 3)
        if agent_type == 1:
                agents.append(selfless_agent.Selfless(name=i))
        elif agent_type == 2:
                agents.append(selfish_agent.Selfish(name=i))
        elif agent_type == 3:
                agents.append(titfortat_agent.Titfortat(name=i))

    # create the world
    game_world = world.World(agents=agents, world_size=size)

    # draw the world
    game_world.draw_background(game_world.screen)
    game_world.draw_agents(game_world.screen)

    # start the game
    game_instance = game.Game(world=game_world, agents=agents, rounds=rounds)

    # play the game
    # print("Playing game...")
    while True:
        # update positions
        # print("moving agents")
        game_world.move_agents()
        # check for collisions
        # print("checking for collisions")
        game_world.collision_detection(game_instance)
        # draw the world
        # print("drawing world")
        game_world.draw_background(game_world.screen)
        # print("drawing agents")
        game_world.draw_agents(game_world.screen)
        # flip the screen
        # print("flipping screen")
        game_world.flip()
        time.sleep(0.1)




        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


if __name__ == "__main__":
    main()
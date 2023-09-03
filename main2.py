import sys
import random
import time

import selfless_agent
import selfish_agent
import titfortat_agent
import game
import world
import agent



def main():
    agents = []
    size = 10 # max: 16
    rounds = 1000 # max: 65,536
    
    # create the agents
    print("Creating agents...")
    timer = time.time()
    for i in range(size*size):
        agent_type = random.randint(1, 3)
        if agent_type == 1:
                agents.append(selfless_agent.Selfless(name=i))
        elif agent_type == 2:
                agents.append(selfish_agent.Selfish(name=i))
        elif agent_type == 3:
                agents.append(titfortat_agent.Titfortat(name=i))
    print("Done. Time elapsed: " + str(time.time() - timer) + " seconds.")

    # create the world
    print("Creating world...")
    timer = time.time()
    game_world = world.World(size=size, agents=agents)
    print("Done. Time elapsed: " + str(time.time() - timer) + " seconds.")

    # update the neighbors
    print("Updating neighbors...")
    timer = time.time()
    game_world.update_neighbors()
    print("Done. Time elapsed: " + str(time.time() - timer) + " seconds.")

    # start the game
    print("Starting game...")
    timer = time.time()
    game_instance = game.Game(world=game_world, agents=agents, rounds=rounds)
    print("Done. Time elapsed: " + str(time.time() - timer) + " seconds.")

    # play the game
    print("Playing game...")
    timer = time.time()
    game_instance.play()
    print("Done. Time elapsed: " + str(time.time() - timer) + " seconds.")
    print("Each round took " + str((time.time() - timer) / rounds) + " seconds.")

    # print the scores
    print("Printing scores in a grid for human readability...")
    timer = time.time()
    for i in range(size):
        for j in range(size):
            print(game_world.get_grid()[i][j].get_score(), end="\t")
        print()
    print("Done. Time elapsed: " + str(time.time() - timer) + " seconds.")


if __name__ == "__main__":
    main()
import sys
import random
import time
import pygame


import game
import world
import agents_list



def main():
    #TODO: add command args
    agents = []
    size = 600
    rounds = 10000


    # create the game instance
    game_instance = game.Game(rounds=rounds)
    
    # create the agents
    for i in range(20):
        
        #agents.append(agents_list.selfish_agent.Selfish(name=i))
        
        agent_type = random.randint(1, 3)
        if agent_type == 1:
                agents.append(agents_list.selfless_runner_agent.Selfless_Runner(name=i, game_instance=game_instance))
        elif agent_type == 2:
                agents.append(agents_list.selfish_chaser_agent.Selfish_Chaser(name=i, game_instance=game_instance))
        elif agent_type == 3:
                agents.append(agents_list.titfortat_agent.Titfortat(name=i, game_instance=game_instance))

    # create the world, using the game rules and the agents
    game_world = world.World(agents=agents, world_size=size, game=game_instance)
    while rounds > game_world.game.get_round():

        game_world.update()
        time.sleep(0.05)


    print("Game Over")
    for agent in agents:
        print(agent.get_score())
    pygame.quit()
    results = data.Data(self.game, "results.csv")
    results.write_to_file()

    

if __name__ == "__main__":
    main()
import sys
import random
import time
import pygame


import game
import world
import agents_list
import data



def main():
    #TODO: add command args
    agents = []
    size = 600
    rounds = 250


    # create the game instance
    game_instance = game.Game(rounds=rounds)
    
    # create the agents
    for i in range(25):
        
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
    pygame.quit()
    results = data.Data(game_instance, agents)
    results.fill_data()
    # print(results.get_data_summary())
    # print(results.get_data())
    results.score_line_chart()

    

if __name__ == "__main__":
    main()
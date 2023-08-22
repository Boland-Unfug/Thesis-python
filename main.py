import sys
import agent
import titfortat_agent
import selfish_agent
import selfless_agent
import world
import game

def main():
        """
        The main method runs the game.
        """
        # create the world
        stage = world.World()
        #print(stage.get_grid())
        #print(stage.get_size())
        #print(stage.get_agents())
        # create the agents
        agents = stage.get_agents()
        # play the game
        stage.update_neighbors()
        # print(agents)
        # print(len(agents))
        # for i in range(len(agents)):
        #         print("Agent",i,":", agents[i])
        #         print(len(agents[i].get_neighbors()))
        #         for j in range(len(agents[i].get_neighbors())):
        #                 print("Neighbor",j,":",agents[i].get_neighbors()[j])

        board = game.Game(stage, agents)
        board.play()
        for agent in agents:
                print(agent, "", agent.get_score())
        




        


                


if __name__ == "__main__":
    main()

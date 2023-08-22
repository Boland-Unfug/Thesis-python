import sys
import agent
import titfortat_agent
import selfish_agent
import selfless_agent
import world

# rules
# C - C = 3, 3
# C - D = 0, 5
# D - C = 5, 0
# D - D = 1, 1

def main():
        """
        The main method runs the game.
        """
        # create the world
        stage = world.World()
        print(stage.get_grid())
        print(stage.get_size())
        print(stage.get_agents())
        # create the agents
        agents = stage.get_agents()
        # play the game
        




        


                


if __name__ == "__main__":
    main()

import sys
import agent
import titfortat_agent
import selfish_agent
import selfless_agent
import world
import game
import visual

def main():
        """
        The main method runs the game.
        """
        # create the world
        game_world = world.World()
        # create the agents
        game_agents = game_world.get_agents()
        # create the visual
        game_display = visual.Visual(game_world, game_agents)
        # display the world
        
        # update the neighbors
        game_world.update_neighbors()
        # play the game
        turn = game.Game(game_world, game_agents)
        turn.play()

        




        


                


if __name__ == "__main__":
    main()

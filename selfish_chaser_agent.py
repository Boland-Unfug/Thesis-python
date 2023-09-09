# This file stores a variation of the selfish agent that will chase the last agent it collided with
import selfish_agent
import game
import random
class Selfish_Chaser (selfish_agent.Selfish):
    """
    The selfish chaser class is a subclass of the selfish class.
    It always defects, but will chase the last agent it collided with.
    """

    def __init__(self, name, game_instance):
        """
        The constructor for the selfish chaser class.
        It sets the score of the agent to 0.
        """
        self.name = name
        self.game_instance = game_instance

    

    def move (self):
        # check the recent game instances for a match for the earliest collision
        # if there is a match, set the direction to the direction of the opponent
        # if there is no match, move randomly

        # get the most recent game instance
        recent_game = self.game_instance.get_specific_recent_history(self.name)
        # get the collision point
        
        if recent_game == None:
            # no collision
            self.set_direction([random.randint(-10, 10), random.randint(-10, 10)])
        else:
            collision_point = recent_game[1]
            # move towards the collision point
            self.set_direction([collision_point[0] - self.get_position()[0], collision_point[1] - self.get_position()[1]])
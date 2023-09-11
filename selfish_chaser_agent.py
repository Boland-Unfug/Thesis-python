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
        self.chase_direction = [0, 0]
        
    def move_strategy (self):
        # check the recent game instances for a match for the earliest collision
        # if there is a match, set the direction to the direction of the opponent
        # if there is no match, move randomly

        # get the most recent game instance
        recent_game = self.game_instance.get_specific_recent_history(self.name)
        # if there are no games yet, move randomly
        # if the last collision is more than 100 rounds ago, move randomly
        if recent_game == None or self.game_instance.get_round() - recent_game[2] > 20: # forget target after 20 rounds
            self.set_direction([random.randint(-10, 10), random.randint(-10, 10)])
        
        elif self.game_instance.get_round() - recent_game[2] > 1: # chase for 19 rounds
            # move randomly
            self.set_direction([self.chase_direction[0], self.chase_direction[1]])

        # else, update the chase point
        else:
            # get the collision point
            self.collision_point = recent_game[1]
            # given the collision point, set the direction to the direction of the opponent
            # calculate the force by subtracting the collision point from the current position
            force = [self.collision_point[0] - self.get_position()[0], self.collision_point[1] - self.get_position()[1]]
            # add the force to the chase direction
            self.chase_direction = [self.direction[0] + force[0], self.direction[1] + force[1]]
            # set the direction to the force
            self.set_direction([self.direction[0] + force[0], self.direction[1] + force[1]])

    def __str__(self):
        return super().__str__() + " Chaser"

    def get_strategy(self):
        return "Selfish"

    def get_movement_strategy(self):
        return "Chaser"
            
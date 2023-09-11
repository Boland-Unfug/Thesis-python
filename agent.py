# Description: This file contains the Agent class and its subclasses.
# The Agent class is the parent class for all agents. it contains the score.

import random
class Agent():
    """
    The Agent class functions as an interface for the actual agent subclasses.
    It contains the helper functions of the Agent class.
    This class is not designed to be used directly, but rather to be inherited by subclasses.
    """

    score = 0 # default score is 0
    name = -1 # start at -1 so that we can tell if there is an error
    current_position = [0,0] # needed as the default value for the position
    previous_position = [0,0] # needed as the default value for the position
    direction = [0, 0] # needed as the default value for the direction
    
    
    def __init__(self, name):
        """
        Initializes an Agent object with a given name.
        A name is required for each agent, as it functions as their unique identifier.

        Parameters:
        name (int): The name of the agent. Ints are used for the hash function, so the name must be an int.

        Returns:
        None
        """
        pass

    def strategy(self):
        """
        Returns the move of the agent.

        Parameters:
        None by default, inputs can be added for specific strategies.

        Returns:
        list: The move of the agent.
        """
        pass

    def move_strategy(self):
        self.update_direction()

    def update_direction(self):
        """
        Updates the direction of the agent.  Random by default, will change later.

        Parameters:
        None

        Returns:
        None
        """
        self.direction = [self.direction[0] + random.randint(-10,10), self.direction[1] + random.randint(-10,10)]



    def __str__(self):
        """
        Returns the type and name of the agent for print statements.

        Parameters:
        None

        Returns:
        str: The type and name of the agent.
        """
        return ("None")

    def update_position(self):
        """
        Updates the position of the agent.

        Parameters:
        None

        Returns:
        None
        """
        self.previous_position = self.current_position
        self.current_position = [self.current_position[0] + self.direction[0], self.current_position[1] + self.direction[1]]

    # setters
    def set_score(self, score):
        """
        Sets the score of the agent to a given value.

        Parameters:
        score (int): The value to set the score to.

        Returns:
        None
        """
        self.score = score

    def set_direction(self, direction):
        """
        Sets the direction of the agent to a given value.

        Parameters:
        direction (list): The value to set the direction to.

        Returns:
        None
        """
        self.direction = direction


    def set_direction_x(self, direction_x):
        """
        Sets the direction of the agent to a given x value.
        
        Parameters:
        direction_x (int): The x component of the direction.

        Returns:
        None
        """

        self.direction[0] = direction_x

    def set_direction_y(self, direction_y):
        """
        Sets the direction of the agent to a given y value.
        
        Parameters:
        direction_y (int): The y component of the direction.

        Returns:
        None
        """

        self.direction[1] = direction_y

    def set_position(self, position):
        """
        Sets the position of the agent to given x and y coordinates.

        Parameters:
        position (list): The x and y coordinates to set the position to.

        Returns:
        None
        """
        self.current_position = position

    
    def set_position_x(self, position_x):
        """
        Sets the position of the agent to a given x value.
        
        Parameters:
        position_x (int): The x component of the position.

        Returns:
        None
        """

        self.current_position[0] = position_x

    def set_position_y(self, position_y):
        """
        Sets the position of the agent to a given y value.
        
        Parameters:
        position_y (int): The y component of the position.

        Returns:
        None
        """

        self.current_position[1] = position_y

    # getters
    
    def get_name(self):
        #TODO: make it so the name can be a string?
        """
        Returns the name of the agent.

        Parameters:
        None

        Returns:
        int: The name of the agent. Ints are used for the hash function, so the name must be an int.
        """
        return self.name

    def get_score(self):
        """
        Returns the score of the agent.

        Parameters:
        None

        Returns:
        int: The score of the agent.
        """
        return self.score

    def get_direction(self):
        """
        Returns the direction of the agent.

        Parameters:
        None

        Returns:
        list: The direction of the agent.
        """
        return self.direction

    def get_position(self):
        """
        Returns the position of the agent.

        Parameters:
        None

        Returns:
        list: The position of the agent.
        """
        return self.current_position

    def get_previous_position(self):
        """
        Returns the previous position of the agent.

        Parameters:
        None

        Returns:
        list: The previous position of the agent.
        """
        return self.previous_position

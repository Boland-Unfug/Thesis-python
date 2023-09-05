# Description: This file contains the Agent class and its subclasses.
# The Agent class is the parent class for all agents. it contains the score.

import random
class Agent():
    """
    The Agent class is the parent class for all agents. 
    it contains the score, the memory of the agent, and the memory of the opponent, but cannot be instantiated.
    it also includes several methods:
    set_score() sets the score of the agent
    get_score() returns the score of the agent
    strategy() returns the move of the agent
    add_neighbor() adds a neighbor to the agent
    set_neighbors() sets the neighbors of the agent
    get_neighbors() returns the neighbors of the agent
    set_xy() sets the x and y coordinates of the agent
    get_xy() returns the x and y coordinates of the agent
    get_name() returns the name of the agent
    create_hash() creates a hash of the game
    __str__() returns the type and name of the agent
    """

    score = 0
    name = -1
    position = []
    direction = [0,0]
    
    def __init__(self, name):
        pass
    
    def change_score(self, score):
        self.score += score

    def set_score(self, score):
        self.score = score

    def get_score(self):
        return self.score

    def strategy(self):
        pass

    def move_strategy(self):
        self.direction = [self.direction[0] + random.randint(-3, 3), self.direction[1] + random.randint(-3, 3)]
        return self.direction

    def get_direction(self):
        return self.direction

    def set_direction(self, direction):
        self.direction = direction

    def set_position(self, x, y):
        self.position = [x, y]

    def get_position(self):
        return self.position

    def get_name(self):
        return self.name

    def create_hash(self, round_number, agent1, agent2):
        """
        The create_hash method creates a hash of the game.
        It takes in the round number and the names of the two agents, which are sorted by name.
        It returns the hash of the game.
        The bit shifts are to make sure that the hash is unique
        # 24 bits for rounds, max:16,777,216 (1 round for movement, 9 rounds for drifting)
        # 20 bits for agent1, max:1,048,576
        # 20 bits for agent2
        """
        return (round_number << 40) + (agent1 << 20) + agent2

    def __str__(self):
        return ("None")
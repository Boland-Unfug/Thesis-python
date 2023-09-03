# Description: This file contains the Agent class and its subclasses.
import abc
# The Agent class is the parent class for all agents. it contains the score.


class Agent():
    """
    The Agent class is the parent class for all agents. 
    it contains the score, the memory of the agent, and the memory of the opponent, but cannot be instantiated.
    it also includes several methods:
    get_score() returns the score of the agent
    change_score() changes the score of the agent
    set_score() sets the score of the agent
    play() returns the move of the agent
    memorize() adds the move of the agent to the memory
    memorize_opponent() adds the move of the opponent to the memory
    forget_move() removes the last move of the agent from the memory
    forget_opponent_move() removes the last move of the opponent from the memory
    forget() resets the memory of the agent
    get_memory() returns the memory of the agent
    get_opponent_memory() returns the memory of the opponent
    get_neighbors() returns the neighbors of the agent
    set_neighbors() sets the neighbors of the agent
    """

    score = 0
    name = ""
    position = []
    memory = []
    neighbors = []

    
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

    def memorize(self, state):
        self.memory.append(state)

    def forget_move(self):
        if self.memory != []:
            self.memory.pop()

    def forget(self):
        self.memory = []

    def get_memory(self):
        return self.memory

    def add_neighbor(self, neighbor):
        self.neighbors.append(neighbor)

    def set_neighbors(self, neighbors):
        self.neighbors = neighbors

    def get_neighbors(self):
        return self.neighbors

    def set_xy(self, x, y):
        self.position = [x, y]

    def get_xy(self):
        return self.position

    def get_name(self):
        return self.name

    def __str__(self):
        return "None"
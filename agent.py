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
    """

    score = 0
    self_memory = []
    opponent_memory = []

    
    def __init__(self):
        pass

    def get_score(self):
        return self.score

    def change_score(self, score):
        self.score += score

    def set_score(self, score):
        self.score = score

    def play(self):
        pass

    def memorize(self, state):
        self.self_memory.append(state)

    def memorize_opponent(self, move):
        self.opponent_memory.append(move)

    def forget_move(self):
        self.self_memory.pop()

    def forget_opponent_move(self):
        self.opponent_memory.pop()

    def forget(self):
        self_memory = []
        self.opponent_memory = []

    def get_memory(self):
        return self.self_memory

    def get_opponent_memory(self):
        return self.opponent_memory
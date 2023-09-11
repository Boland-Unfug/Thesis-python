import numpy as np
import pandas as pd
import os

class Data():
    def __init__(self,game, name= "results.csv"): # so far its fair to say every data needs to analyze a game
        self.game = game
        self.name = name
        self.delete_file(name)
        self.make_file(name)
        # general data, stores agent names, their strategy, and their movement strategy, and their final score
        self.data_summary = pd.DataFrame(columns=['Agent', 'Strategy', 'Movement Strategy', 'Score'])
        # round data, stores the round number, the state, the actions of the agents, and the score of the agents
        self.data = pd.DataFrame(columns=['Round', 'State', 'Player 1 Action', 'Player 2 Action', 'Player 1 Reward', 'Player 2 Reward', 'Player 1 Score', 'Player 2 Score', 'Collision Point'])


    def make_file(self, name="results.csv"):
        if not os.path.exists(name):
            # create a file
            file = open(name, "w")
            file.close()
    
    def delete_file(self, name = "results.csv"):
        if os.path.exists(name):
            # delete a file
            os.remove(name)
        else:
            print("The file does not exist")

    def fill_data(self):
        # fill in the data summary
        for agent in self.game.get_agents():
            self.add_agent_to_data_summary(agent)
        # fill in the round data
        for hashcode in self.game.get_history():
            self.add_round_to_data(hashcode)
        # write to the file
        self.write_to_file()

    def add_agent_to_data_summary(self, agent):
        self.data_summary = self.data_summary.append({'Agent': agent.get_name(), 'Strategy': agent.get_strategy(), 'Movement Strategy': agent.get_movement_strategy(), 'Score': agent.get_score()}, ignore_index=True)

    def add_round_to_data(self, hash):

        state, collision_point, score1, score2 = self.game.get_specific_history(hash)
        # get the game state, agents, and round from the hash
        round_number, agent1, agent2 = self.decode(hash)

        # get the actions and scores of the agents from the game state
        action_1, action_2, reward_1, reward_2 = self.get_actions_and_outcomes(state)

        # add to the table
        self.data = self.data.append({'Round': round_number, 'State': state,
                                     'Player 1 Action': action_1, 'Player 2 Action': action_2,
                                     'Player 1 Reward': reward_1, 'Player 2 Reward': reward_2,
                                     'Player 1 Score': score1, 'Player 2 Score': score2, 
                                     'Collision Point': collision_point}, ignore_index=True)
        

    # def add_data_summary(self):
    #     self.data_summary = self.data_summary.append({'Agent': agent, 'Strategy': strategy, 'Movement Strategy': movement_strategy, 'Score': score}, ignore_index=True)

    # def write_to_file(self, name = self.name):
    #     self.data.to_csv(name, index=False)

    # def read_from_file(self, name = self.name):
    #     self.data = pd.read_csv(name)

    # def add_round(self, round_number, state, score_1, score_2):
    #     self.data = self.data.append({'Round': round_number, 'State': state, 'Player 1 score': score_1, 'Player 2 score': score_2}, ignore_index=True)

    def decode(self, hash): # must do this first to get payoffs
        """
        retreives the round, agent1, and agent2 and state from the hash.
        Parameters:
        hash (int): The hash of the game.
        Returns:
        tuple: The round, agent1, agent2, and state.
        """
        round_number = hash >> 40
        agent1 = (hash >> 20) & 0xFFFFF
        agent2 = hash & 0xFFFFF
        state = self.game.get_state(agent1, agent2)
        return (round_number, agent1, agent2, state)

    def get_actions_and_outcomes (self, state):
        """
        Gets the actions and outcomes for the two agents.
        Parameters:
        hash (int): The hash of the game.
        Returns:
        tuple: The actions and outcomes for the two agents.
        """
        action_1, action_2 = self.game.get_actions(state)
        outcome_1, outcome_2 = self.game.get_outcomes(action_1, action_2)
        return (action_1, action_2, outcome_1, outcome_2)
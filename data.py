import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

class Data():
    def __init__(self,game, agents, name= "results.csv", name2 = "summary.csv"): # so far its fair to say every data needs to analyze a game
        self.game = game
        self.name = name
        self.name2 = name2
        self.delete_file(name)
        self.make_file(name)
        self.delete_file(name2)
        self.make_file(name2)
        self.agents = agents
        # general data, stores agent names, their strategy, and their movement strategy, and their final score
        self.data_summary = pd.DataFrame(columns=['Agent', 'Strategy', 'Movement Strategy', 'Score'])
        # round data, stores the round number, the state, the actions of the agents, and the score of the agents
        self.data = pd.DataFrame(columns=['Round','Agent', 'Opponent', 'State', 'Player 1 Action', 'Player 2 Action', 'Player 1 Reward', 'Player 2 Reward', 'Player 1 Score', 'Player 2 Score', 'Collision Point'])


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

    def write_to_file(self):
        self.data_summary.to_csv(self.name2, mode='a', header=True)
        self.data.to_csv(self.name, mode='a', header=True)

    def fill_data(self):
        # fill in the summary data
        for agent in self.agents:
            self.add_agent_to_data_summary(agent)
        # fill in the round data
        for hashcode in self.game.get_history():
            self.add_round_to_data(hashcode)
        # write to the file
        self.write_to_file()

    def add_agent_to_data_summary(self, agent):
        self.data_summary = self.data_summary._append({'Agent': agent.get_name(), 'Strategy': agent.get_strategy(), 'Movement Strategy': agent.get_movement_strategy(), 'Score': agent.get_score()}, ignore_index=True)

    def add_round_to_data(self, hash):

        state, collision_point, score1, score2 = self.game.get_specific_history(hash)
        # get the game state, agents, and round from the hash
        round_number, agent1, agent2 = self.decode(hash)

        # get the actions and scores of the agents from the game state
        action_1, action_2, reward_1, reward_2 = self.get_actions_and_outcomes(state)

        # add to the table
        self.data = self.data._append({'Round': round_number, 'State': state,
                                     'Agent': agent1, 'Opponent': agent2,
                                     'Player 1 Action': action_1, 'Player 2 Action': action_2,
                                     'Player 1 Reward': reward_1, 'Player 2 Reward': reward_2,
                                     'Player 1 Score': score1, 'Player 2 Score': score2, 
                                     'Collision Point': collision_point}, ignore_index=True)
        

    
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
        return (round_number, agent1, agent2)

    def get_actions_and_outcomes (self, state):
        """
        Gets the actions and outcomes for the two agents.
        Parameters:
        hash (int): The hash of the game.
        Returns:
        tuple: The actions and outcomes for the two agents.
        """
        action_1, action_2 = self.game.get_actions(state)
        outcome_1, outcome_2 = self.game.get_payoff(action_1, action_2)
        return (action_1, action_2, outcome_1, outcome_2)

    def get_data_summary(self):
        return self.data_summary

    def get_data(self):
        return self.data


    # graphing functions
    def score_line_chart(self):
        # make a plot of rounds where each agent has a score
        # x axis is round number
        # y axis is score
        # each line is an agent

        # get the data
        data = self.data
        # get the scores of both agents and opponents
        rounds = data['Round'].unique()
        print(rounds)
        agents = data['Agent'].unique()
        print(agents)
        opponents = data['Opponent'].unique()
        print(opponents)
        # combine the agents and opponents
        agents = np.concatenate((agents, opponents))
        agents = np.unique(agents)
        print(agents)
        # make a list for each agents score each round, updating it if the agents score changes
        # pretty much just need to fill all the scores for each agent for each round
        #TODO
        
        
        
        # get the scores of the agents and opponents

        


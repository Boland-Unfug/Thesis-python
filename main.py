import sys
import agent
import titfortat_agent
import selfish_agent
import selfless_agent

# rules
# C - C = 3, 3
# C - D = 0, 5
# D - C = 5, 0
# D - D = 1, 1

def main():
        # # get the number of rounds
        rounds = int(10)
        # # get the agents
        # agent_1 = sys.argv[2]
        # agent_2 = sys.argv[3]
        # create the agents
        agent_1 = titfortat_agent.titfortat()
        agent_2 = selfish_agent.selfish()
        # play the game
        for i in range(rounds):
                play_1 = agent_1.play()
                play_2 = agent_2.play()
                # print("play: ", play_1, play_2)
                score_1, score_2 = prisoner_dilemma(play_1, play_2)
                # print("score: ", score_1, score_2)
                agent_1.change_score(score_1)
                agent_2.change_score(score_2)
                # print("agent score: ", agent_1.get_score(), agent_2.get_score())
                agent_1.forget()
                agent_2.forget()
                agent_1.memorize(play_1)
                agent_2.memorize(play_2)
                agent_1.memorize_opponent(play_2)
                agent_2.memorize_opponent(play_1)
        # print the score
        print("agent 1: ", agent_1.get_score())
        print("agent 2: ", agent_2.get_score())

def prisoner_dilemma(play_1, play_2):
        score_1 = 0
        score_2 = 0
        if play_1 == 'C' and play_2 == 'C':
                score_1 = 3
                score_2 = 3
        elif play_1 == 'C' and play_2 == 'D':
                score_1 = 0
                score_2 = 5
        elif play_1 == 'D' and play_2 == 'C':
                score_1 = 5
                score_2 = 0
        elif play_1 == 'D' and play_2 == 'D':
                score_1 = 1
                score_2 = 1
        return score_1, score_2

                


if __name__ == "__main__":
    main()

import sys
import agent

# rules
# C - C = 3, 3
# C - D = 0, 5
# D - C = 5, 0
# D - D = 1, 1

def main():
    player_1 = agent.Agent(strategy='C')
    player_2 = agent.Agent(strategy='D')

    for i in range(1, 10):
        #both players play
        print("Round " + str(i))
        play_1 = player_1.play()
        play_2 = player_2.play()

        #Update memory of each player
        player_1.memorize([player_1, play_1])
        player_1.memorize_opponent([player_2, play_2])
        player_2.memorize([player_2, play_2])
        player_2.memorize_opponent([player_1, play_1])
        

        result_1, result_2 = prisoner_dilemma(player_1.play(), player_2.play())
        player_1.change_score(result_1)
        player_2.change_score(result_2)
        

        print("Player 1 score: " + str(player_1.get_score()))
        print("Player 2 score: " + str(player_2.get_score()))

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

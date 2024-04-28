import game
import graph
import numpy as np
import random
import math

payoff_matrix = np.array([[0.5, 1, 0], [0, 0.5, 1], [1, 0, 0.5]])

def generate_distribution_strategy():
    cdf = (random.random(), random.random())
    pdf = (cdf[0], cdf[1] - cdf[0], 1 - cdf[1])

    return game.DistributionStrategy(pdf)

#if __name__ == '__main__':
N_STRATEGIES = 10
strategies = []
for _ in range(N_STRATEGIES):
    strategy = generate_distribution_strategy()
    strategies.append(strategy)

mg = game.MatrixGame(payoff_matrix)
matrix = mg.play_strategies(strategies)

print(matrix)

normalized = graph.graph_normalize(matrix)
gram = graph.graph_dot(normalized)

distance_matrix = np.sqrt((1 - gram / 10) / 2)

print(distance_matrix)

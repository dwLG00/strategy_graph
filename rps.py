import game
import numpy as np
import random

payoff_matrix = np.array([[0.5, 1, 0], [0, 0.5, 1], [1, 0, 0.5]])

def generate_distribution_strategy():
    cdf = (random.random(), random.random())
    pdf = (cdf[0], cdf[1] - cdf[0], 1 - cdf[1])

    return lambda: np.random.choice([0, 1, 2], p=pdf)

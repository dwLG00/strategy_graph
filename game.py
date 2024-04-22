import numpy as np
import random

class MatrixGame:
    def __init__(self, payout_matrix, winner=):
        self.payout_matrix = payout_matrix

    def play(strategy1, strategy2, n=101, winfunc=bin_more_wins):
        outcomes = []
        for _ in range(n):
            i = strategy1.play()
            j = strategy2.play()
            payout = self.payout_matrix[i, j]
            outcomes.append(payout)
        return winfunc(outcomes)

class MonoStrategy:
    def __init__(self, n):
        # 0 <= n < n_strategies
        self.stragety = n

    def play(self):
        return self.strategy

class DistributionStrategy:
    def __init__(self, distribution):
        self.distribution = distribution

    def play(self):
        rand = random.random()
        for n, p in enumerate(self.distribution):
            if rand < p:
                return n
            rand -= p
        return len(distribution) - 1

def bin_more_wins(l):
    if sum([1 if outcome > 0 else 0]) / 2 > len(l):
        return True
    return False

def average_better_score(l):
    if sum(l) > 0:
        return True
    return False

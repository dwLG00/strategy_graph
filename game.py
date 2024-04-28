import numpy as np
import random

def winrate(l):
    return sum([1 if outcome > 0 else 0 for outcome in l]) / len(l)

def bin_more_wins(l):
    if sum([1 if outcome > 0 else 0 for outcome in l]) / 2 > len(l):
        return True
    return False

def average_better_score(l):
    if sum(l) > 0:
        return True
    return False

class MatrixGame:
    def __init__(self, payout_matrix):
        self.payout_matrix = payout_matrix

    def play(self, strategy1, strategy2, n=101, winfunc=winrate):
        outcomes = []
        for _ in range(n):
            i = strategy1.play()
            j = strategy2.play()
            payout = self.payout_matrix[i, j]
            outcomes.append(payout)
        return winfunc(outcomes)

    def play_strategies(self, strategies, **kwargs):
        matchup_matrix = np.zeros((len(strategies), len(strategies)))
        for i, strategy1 in enumerate(strategies):
            for j, strategy2 in enumerate(strategies):
                if i < j:
                    outcome = self.play(strategy1, strategy2, **kwargs)
                    matchup_matrix[i, j] = outcome
                    matchup_matrix[j, i] = 1 - outcome
                elif i == j:
                    matchup_matrix[i, i] = 0.5
        return matchup_matrix

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


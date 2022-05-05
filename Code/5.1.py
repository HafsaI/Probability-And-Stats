import random
import scipy
import math
import numpy as np
import fishCImport as f
import scipy.stats as st
from scipy.stats import norm
import matplotlib.pyplot as plt


# __________________________________________________________________________5.1___________________________________________________________________________________
''' a function that simulates the behavior of a fair coin'''


def heads_tails(number_of_flips):
    tails_count = 0
    heads_count = 0
    for _ in range(number_of_flips):
        rand = random.choice([1, -1])
        if rand == 1:
            tails_count += 1
        else:
            heads_count += 1
    # print(' Total tails:', tails_count, ' Total heads:', heads_count)
    return heads_count


'''function that uses the above function to simulate 10 coin tosses multiple times and finds the expected number of times the null hypothesis is rejected even though it is true.'''


def simulate_multiple(x):
    averagelst = []
    for _ in range(x):
        lst = []
        for _ in range(x):
            expected = 0
            for _ in range(x):
                heads_count = heads_tails(10)
                if heads_count >= 9:         # critical value when threshold = 0.05
                    expected += 1
                elif heads_count <= 1:
                    expected += 1
            lst.append(expected)
        averagelst.append(sum(lst)/x)
    return averagelst


#noOfExps = 100
# expected = simulate_multiple(noOfExps)
# print("Expected values are:", expected)
# print("Expected probability that we will reject the null hypothesis even though it is true:",
#       round((sum(expected)/noOfExps)/noOfExps, 3))

# ---------------HISTOGRAM------------------- for simulate_multiple()
# plt.figure(figsize=(8, 5))
# plt.style.use('seaborn-whitegrid')
# np.random.seed(1)
# x = expected
# n, bins, patches = plt.hist(
#     x, bins=15, facecolor='#0e8c9b', edgecolor='#e0e0e0', linewidth=1.0)
# n = n.astype('int')
# plt.title("Histogram", fontsize=11)
# plt.xlabel('Expected Number Of Times Null Hypothesis is Rejected', fontsize=10)
# plt.ylabel('Frequency', fontsize=10)
# plt.show()
# ---------------------xxx-------------------------

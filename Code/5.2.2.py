import random
import scipy
import math
import numpy as np
import fishCImport as f
import scipy.stats as st
from scipy.stats import norm
import matplotlib.pyplot as plt


def mean_variance(sampleno):
    lengths = []
    sums = 0
    mean = 0
    variance = 0
    for _ in range(sampleno):
        length = f.fish()
        lengths.append(length)

    variance = np.var(lengths)
    mean = np.mean(lengths)
    return (mean, variance)

# __________________________________________________________5.2.2___________________________________________________________________


def hypothesis_testing4(n, popmean):
    rejected = []
    expectedvalues = []
    exps = 100
    k = 100
    j = 10
    for _ in range(exps):
        rejected = []
        for _ in range(j):
            rejects = 0
            for _ in range(k):
                samplemean, variance = mean_variance(n)
                a = abs(samplemean - popmean)
                # P( S >= u0 + a)
                x = 1 - norm(loc=popmean, scale=(math.sqrt(variance)) /
                             math.sqrt(n)).cdf(popmean + a)

                # P( S <= u0 - a)
                y = norm(loc=popmean, scale=(math.sqrt(variance)) /
                         math.sqrt(n)).cdf(popmean - a)

                ans = x + y
                if (ans < 0.05):
                    rejects += 1
            rejected.append(rejects)
        expectedvalues.append(sum(rejected)/j)
    return expectedvalues


n = 70
mean = 23
#expectation = hypothesis_testing4(n, mean)

# ---------------HISTOGRAM------------------- for hypothesis_testing4(n, popmean) ^
# plt.figure(figsize=(8, 5))
# plt.style.use('seaborn-whitegrid')
# np.random.seed(1)
# x = expectation

# n, bins, patches = plt.hist(
#     x, bins=15, facecolor='#0e8c9b', edgecolor='#e0e0e0', linewidth=1.0)


# n = n.astype('int')

# plt.title("Histogram", fontsize=11)
# plt.xlabel('Expected Number Of Times Null Hypothesis is Rejected', fontsize=10)
# plt.ylabel('Frequency', fontsize=10)
# plt.show()

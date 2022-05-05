import random
import scipy
import math
import numpy as np
import fishCImport as f
import scipy.stats as st
from scipy.stats import norm
import matplotlib.pyplot as plt


# __________________________________________________________5.2.3___________________________________________________________________
''' ran several times with different values of n to get the least value of n that would ensure null hypothesis is not wrongly rejected more than 10 percent of the time.'''


def samplefish(n):
    lengths = []
    for _ in range(n):
        l = np.random.normal(23, 3)
        lengths.append(l)
    return lengths


def probability(n):
    lengths = samplefish(n)
    std = np.std(lengths)
    samplemean = np.mean(lengths)
    a = abs(samplemean - 23)
    # P( S >= u0 + a)
    x = 1 - norm(loc=23, scale=(std) /
                 math.sqrt(n)).cdf(23 + a)

    # P( S <= u0 - a)
    y = norm(loc=23, scale=(std) /
             math.sqrt(n)).cdf(23 - a)

    probability = x + y
    return probability


def Hypothesis_Testing(n):
    exps = 100
    tests = 100

    expected = []
    for _ in range(exps):
        rejects = 0
        for _ in range(tests):
            p = probability(n)  # of n samples
            if p <= 0.1:
                rejects += 1

        rejected = rejects/tests
        expected.append(rejected)

    return expected


expected = Hypothesis_Testing(46)


# -----------Histogram ---- for function  Hypothesis_Testing()
plt.figure(figsize=(8, 5))
plt.style.use('seaborn-whitegrid')
np.random.seed(1)
x = expected
n, bins, patches = plt.hist(
    x, bins=30, facecolor='#0e8c9b', edgecolor='#e0e0e0', linewidth=1.0, density=True)
x.sort()
mu, sigma = scipy.stats.norm.fit(x)
best_fit_line = scipy.stats.norm.pdf(x, mu, sigma)
plt.plot(x, best_fit_line)
n = n.astype('int')
plt.title("Histogram", fontsize=11)
plt.xlabel(
    'Expected Number Of Times Null Hypothesis is Rejected', fontsize=10)
plt.ylabel('Frequency', fontsize=10)
plt.show()

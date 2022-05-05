import random
import scipy
import math
import numpy as np
import fishCImport as f
import scipy.stats as st
from scipy.stats import norm
import matplotlib.pyplot as plt

# ___________________________________________________________5.2.1____________________________________________________________________________


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


# SUB TASK 1
''' Finds expected number of times the null hypothesis is rejected using pvalue'''


def hypothesis_testing1(n, popmean):
    lengths = []
    rejects = 0
    length = 0
    rejectedtimes = []
    k = 100
    exps = 100
    expectedvalues = []

    for _ in range(exps):
        rejectedtimes = []
        for _ in range(k):
            rejects = 0
            for _ in range(k):

                for _ in range(n):
                    length = f.fish()
                    lengths.append(length)

                tset, pval = st.ttest_1samp(lengths, popmean)  # gets p-value

                if pval < 0.05:    # threshold value is 0.05
                    rejects += 1

                lengths = []
            rejectedtimes.append(rejects)
        expectedvalues.append(sum(rejectedtimes)/k)
    return expectedvalues


#rejectlst = hypothesis_testing1(30, 23)

# ---------------HISTOGRAM------------------- for hypothesis_testing1(n, popmean) ^
# plt.figure(figsize=(8, 5))
# plt.style.use('seaborn-whitegrid')
# np.random.seed(1)
# x = rejectlst
# n, bins, patches = plt.hist(
#     x, bins=15, facecolor='#0e8c9b', edgecolor='#e0e0e0', linewidth=1.0)
# n = n.astype('int')
# plt.title("Histogram", fontsize=11)
# plt.xlabel('Expected Number Of Times Null Hypothesis is Rejected', fontsize=10)
# plt.ylabel('Frequency', fontsize=10)
# plt.show()

# -------------------xxx--------------------------------------------------


# SUB TASK 2
'''a function that takes in u0 and n, and conducts a ''single hypothesis test'' and returns probability P ( |S - u_{o}| >= a) where a = u - u0'''


def hypothesis_testing2(n, popmean):
    samplemean, variance = mean_variance(30)
    a = abs(samplemean - popmean)
    # P( S >= u0 + a)
    phi1 = norm(loc=popmean, scale=(math.sqrt(variance)) /
                math.sqrt(n)).cdf(popmean + a)
    x = 1 - phi1
    # # P( S <= u0 - a)
    phi2 = norm(loc=popmean, scale=(math.sqrt(variance)) /
                math.sqrt(n)).cdf(popmean - a)
    y = phi2

    ans = x + y
    if (ans < 0.05):
        print(" Null hypothesis Rejected")
    else:
        print("Null Hypothesis Accepted")
    return ans


#prob = hypothesis_testing2(30, 23)
# print("Probability of  P ( |S - u_o| >= a) for a single sample:", prob)


# SUB TASK 3
def hypothesis_testing3(n, popmean):
    rejected = []
    expectedvalues = []
    exps = 100
    tests = 100
    j = 10
    for _ in range(exps):
        rejected = []
        for _ in range(j):
            rejects = 0
            for _ in range(tests):
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


n = 30
mean = 23
#expectation = hypothesis_testing3(n, mean)

# ---------------HISTOGRAM------------------- for hypothesis_testing3(n, popmean) ^
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

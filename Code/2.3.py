import random
import numpy as np
import math
from matplotlib import pyplot as plt


# _______________________________________________________________2.3____________________________________________________

# picked x and found corresponding values of y
def random_var():
    randomvar = 0
    x = np.random.random()
    randomvar = math.sqrt(-1 / (2 * (x-1)))
    return randomvar

# Histogram _ 1

# y = []
# for i in range(100000):
#     x = random_var()
#     y.append(x)
# y.sort()
# ind = (np.array(y) > 5).tolist().index(1)
# y = y[: ind]
# bins = 100
# binWidth = (max(y) - min(y)) / bins
# plt.hist(y, bins=bins, weights=np.ones(len(y)) / (len(y) * binWidth))
# values = np.linspace(min(y), max(y), 50)
# plt.plot(values, (1 / values ** 3))
# plt.show()

# Expected Value Function that calculates expected values


def expected_values(exps):
    y = []
    expected = []
    sums = 0
    for _ in range(exps):
        for _ in range(100000):
            x = random_var()
            y.append(x)
        sums = (sum(y) / 100000)
        y = []
        expected.append(sums)
    return expected


expected = expected_values(100)

# Histogram _ 2
# ------Plotting of Expected Values

plt.figure(figsize=(8, 4))
plt.style.use('seaborn-whitegrid')
x = expected

n, bins, patches = plt.hist(
    x, bins=10, facecolor='#1f77b4', edgecolor='#e0e0e0', linewidth=1.0)

n = n.astype('int')

plt.title("Histogram", fontsize=11)
plt.xlabel('Expected Values', fontsize=10)
plt.ylabel('Frequency', fontsize=10)
plt.show()

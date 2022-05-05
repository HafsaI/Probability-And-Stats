import matplotlib.pyplot as plt
import numpy as np
import random

# ____________________________________________________________#1.1#___________________________________________________________


def calc_Expectation_1(n, p):
    expectedvalues = []
    finalpos = 0
    exps = 1000
    k = 100
    lst = []

    for _ in range(exps):
        for _ in range(k):
            for i in range(0, n):
                randomNo = np.random.random()
                if randomNo > p:
                    finalpos -= 1
                if randomNo < p:
                    finalpos += 1

            lst.append(finalpos)
            finalpos = 0
        expected = sum(lst)/k
        lst = []
        expectedvalues.append(expected)
    return expectedvalues


n = 10
p = 0.5
expect = calc_Expectation_1(n, p)
print('1.1__Final Positions:', expect, "\n")


# ---------------HISTOGRAM------------------- for calc_Expectation_1(n, p)^

plt.figure(figsize=(6, 4))
plt.style.use('seaborn-whitegrid')
np.random.seed(1)
x = expect

n, bins, patches = plt.hist(
    x, bins=15, facecolor='#2ab0ff', edgecolor='#e0e0e0', linewidth=1.0)

n = n.astype('int')

for i in range(len(patches)):
    patches[i].set_facecolor(plt.cm.viridis(n[i]/max(n)))

plt.title("Histogram", fontsize=11)
plt.xlabel('Expected Values', fontsize=10)
plt.ylabel('Frequency', fontsize=10)
plt.show()

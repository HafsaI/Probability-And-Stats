import matplotlib.pyplot as plt
import numpy as np
import random
# ____________________________________________________________#1.2#___________________________________________________________


def calc_Expectation_2(n, p):
    expected = []
    exps = 1000
    k = 100
    for _ in range(exps):
        positions = []
        for _ in range(k):
            finalpos = 0
            for i in range(n):
                # if at zero, can only move to right
                if (finalpos == 0):
                    finalpos += 1
                else:
                    randomNo = np.random.random()
                    if randomNo > p:
                        finalpos -= 1
                    elif randomNo < p:
                        finalpos += 1
            positions.append(finalpos)
        expected.append(sum(positions)/k)
    return expected


n = 100
p = 0.5
expect2 = calc_Expectation_2(n, p)
print('1.2__FinalPositions:', expect2, '\n')

# ---------------HISTOGRAM-------------------  for calc_Expectation_2(n, p) ^

plt.figure(figsize=(8, 4))  # Plot size
plt.style.use('seaborn-whitegrid')  # Style
np.random.seed(1)
x = expect2

n, bins, patches = plt.hist(
    x, bins=20, facecolor='#2ab0ff', edgecolor='#e0e0e0', linewidth=1.0)

n = n.astype('int')

for i in range(len(patches)):
    patches[i].set_facecolor(plt.cm.viridis(n[i]/max(n)))


plt.title("Histogram", fontsize=11)
plt.xlabel('Expected Values', fontsize=10)
plt.ylabel('Frequency', fontsize=10)
plt.show()

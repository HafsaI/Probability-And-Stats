import matplotlib.pyplot as plt
import numpy as np
import random

# ____________________________________________________________#1.3#___________________________________________________________
''' finds expected no of steps taken for two objects to meet when there is even distance between them '''


def meetingsteps(startpos1, startpos2, p1, p2):
    exps = 100
    k = 100
    pos1 = startpos1
    pos2 = startpos2
    expectedsteps = []
    for _ in range(exps):
        steps = []
        for _ in range(k):
            noofSteps = 0
            while pos1 != pos2:
                randomNo = np.random.random()
                if randomNo > p1:
                    pos1 -= 1
                elif randomNo < p1:
                    pos1 += 1
                randomNo = np.random.random()
                if randomNo > p2:
                    pos2 -= 1
                elif randomNo < p2:
                    pos2 += 1
                noofSteps += 2

            steps.append(noofSteps)
            pos1 = startpos1
            pos2 = startpos2
        expectedsteps.append(sum(steps)/k)

    return expectedsteps


startpos1 = 2
startpos2 = -2
p1 = 0.5
p2 = 0.5
expectedsteps = meetingsteps(startpos1, startpos2, p1, p2)
print('Expected Number of Steps Taken to Meet :', expectedsteps, '\n')


# ---------------HISTOGRAM-------------------
plt.figure(figsize=(12, 4))
plt.style.use('seaborn-whitegrid')
np.random.seed(1)
x = expectedsteps


n, bins, patches = plt.hist(
    x, bins=[0, 100, 500, 1000, 2000, 5000], facecolor='#0e8c9b', edgecolor='#e0e0e0', linewidth=1.0)


plt.xticks([0, 100, 500, 1000, 2000, 5000], fontsize=8)
n = n.astype('int')

plt.title("Histogram", fontsize=11)
plt.xlabel('Expected Steps To Meet', fontsize=10)
plt.ylabel('Frequency', fontsize=10)
plt.show()

# ...................

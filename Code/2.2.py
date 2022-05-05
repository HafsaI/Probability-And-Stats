import random
import numpy as np
import math
from matplotlib import pyplot as plt


y = []

for i in range(100000):
    x = np.random.random()
    y.append(1 / (1 - x))

y.sort()
ind = (np.array(y) > 30).tolist().index(1)
y = y[: ind]
bins = 100
binWidth = (max(y) - min(y)) / bins
plt.hist(y, bins=bins, weights=np.ones(len(y)) / (len(y) * binWidth))
values = np.linspace(min(y), max(y), 50)
plt.plot(values, (1 / values ** 2))
plt.show()

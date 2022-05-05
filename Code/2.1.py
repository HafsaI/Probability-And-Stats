

import random
import numpy as np
import math
from matplotlib import pyplot as plt

y = []

for i in range(100000):
    x = np.random.random()
    y.append(- np.log(1 - x))

bins = 20
binWidth = (max(y) - min(y)) / bins
plt.hist(y, bins=bins, weights=np.ones(len(y)) / (len(y) * binWidth))
values = np.linspace(min(y), max(y), 50)
plt.plot(values, np.exp(- values))
plt.show()

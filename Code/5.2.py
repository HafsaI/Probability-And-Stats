import random
import scipy
import math
import numpy as np
import fishCImport as f
import scipy.stats as st
from scipy.stats import norm
import matplotlib.pyplot as plt


# __________________________________________________________5.2___________________________________________________________________
''' calculates mean and variance of a sample of fish lengths'''


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


# mean, variance = mean_variance(30)
# print("Mean of sample: ", round(mean,2), " Variance of sample: ", round(variance,2))

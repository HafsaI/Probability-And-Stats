import random
import matplotlib.pyplot as plt
import numpy as np

def generateRandomXY(R):
    '''
    Generates random x and y values.
    args: R - radius
    returns: x and y list. 
    '''
    x, y = [], []
    for i in range(1000):
        ax = (random.randint(-R, R))
        wy = (random.randint(-R, R))
        if np.sqrt(ax**2 + wy**2) < R:
            x.append(ax)
            y.append(wy)
    return x, y

def plot(R, x, y):
    '''
    Plots circle and random points.
    args: Radius (R), x and y value list for random points
    '''

    # plotting circle
    t = np.linspace(0, 2*np.pi, 150)
    a = R * np.cos(t)
    b = R * np.sin(t)
    fig, ax = plt.subplots(1)
    ax.plot(a, b)
    ax.set_aspect(1)
    # plotting points
    plt.scatter(x, y, marker='.')
    plt.show()

def main():
    R = 1000
    x, y = generateRandomXY(R)
    
    # calculating variance in radius and theta
    print("Variance in theta values: ", np.var(x))
    print("Variance in R values: ", np.var(y))

    plot(R, x, y)

main()
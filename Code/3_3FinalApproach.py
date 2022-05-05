import random
import matplotlib.pyplot as plt
import numpy as np

def convertToXY(r, theta):
    '''
    Converts radius and theta values to xy values for plotting.
    args: radius list (r), theta list (theta)
    returns: x and y lists.
    '''

    x = []
    y = []
    for i in range(1000):
        x.append(r[i] * np.cos(theta[i]))
        y.append(r[i] * np.sin(theta[i]))
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
    plt.scatter(x, y, marker='.', color='red')
    plt.show()

def generateRandom(R):
    '''
    - Generates random values of radius and theta. 
    - Calculates variance.
    args: Radius - integer
    returns: theta and radius list
    '''
    theta = []
    radius = []
    # Generating 1000 random radius and theta values.
    for i in range(1000):
        radius.append(R*np.sqrt(random.random()))
        theta.append(random.randint(1,360))
    
    return radius, theta
    

def main():
    R = 1000
    radius, theta = generateRandom(R)
    
    x , y = convertToXY(radius, theta)
    
    # calculating variance in radius and theta
    print("Variance in x values: ", np.var(x))
    print("Variance in y values: ", np.var(y))

    plot(R, x, y)

main()
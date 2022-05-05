# method 1
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
    for i in range(len(r)):
        x.append(r[i] * np.cos(theta[i]))
        y.append(r[i] * np.sin(theta[i]))
    return x, y

def plot(R1, R2, x, y):
    '''
    Plots circle and random points.
    args: Radius (R), x and y value list for random points
    '''

    # plotting circle
    t = np.linspace(0, 2*np.pi, 150)
    a1 = R1 * np.cos(t)
    b1 = R1 * np.sin(t)
    a2 = R2 * np.cos(t)
    b2 = R2 * np.sin(t)

    fig, ax = plt.subplots(1)
    ax.plot(a1, b1)
    ax.plot(a2, b2)
    ax.set_aspect(1)
    # plotting points
    plt.scatter(x, y, marker='.', color='red')
    plt.show()

def generateRandom(R1, R2):
    '''
    - Generates random values of radius and theta. 
    - keeps count of points generated
    args: R1 (large circle), R2 (smaller circle) - integer
    returns: theta and radius list, count of R1 and R2
    '''
    theta = []
    radius = []
    countR1 = 0
    countR2 = 0
    # Generating 1000 random radius and theta values.
    for i in range(1000):
        r = random.randint(1,R1)
        t = random.randint(1,360)
        # if (r not in radius) and (t not in theta):
        radius.append(r)
        theta.append(t)
        if (r <= R2):
            countR2+=1
        countR1+=1
    return radius, theta, countR1, countR2
    

def main():
    R1 = 1000
    R2 = R1//2
    radius, theta, countR1, countR2 = generateRandom(R1, R2)
    
    x , y = convertToXY(radius, theta)

    
    # calculating variance in radius and theta
    print("Variance in x1 values: ", np.var(x))
    print("Variance in y1 values: ", np.var(y))
    print("Number of points in R2: ", countR2)
    print("Number of points in R1: ", countR1)


    plot(R1, R2, x, y)

main()
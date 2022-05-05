import math
import matplotlib.pyplot as plt
import numpy as np

# For all parts, we will assume radius r = 10 cm
r = 10
chordLengthList = []


# Function to uniformly select 2 angles theta1 and theta2, between 0, and 2pi. 
def selectAngles():
    thetaListA = []
    thetaListB = []
    i = 0
    while len(thetaListA) < 100: 
        theta1 = (np.random.uniform(0, 360)) # thetas are uniformly selected
        thetaListA.append(theta1)
    while len(thetaListB) < 100:
        theta2 = (np.random.uniform(0, 360))
        while theta2 < thetaListA[i]: # Our function is such that theta2 will always be greater than theta1 to avoid negative values
            theta2 = (np.random.uniform(0, 360))
        thetaListB.append(theta2)
        i += 1
    return thetaListA, thetaListB


# Function to claculate length of chord formed by theta1 and theta2
# Formula = 2*r*sin*(c/2)
# Where r is radius and centralAngle is angle between theta1 and theta2 
def calculateChordLength():
    global chordLengthList # global variable so that it can be accessed outside function to plot histogram
    i = 0
    while len(chordLengthList) < 100:
        thetas = selectAngles() # thetas contains two lists, one containing theta1 and other containing theta2 respectively
        centralAngle = thetas[1][i] - thetas[0][i] 
        chordLength = 2*r*(math.sin(math.radians(centralAngle/2))) # formula to calculate chord length is implemented here
        chordLengthList.append(chordLength) # a list of chord lengths is collected to plot histogram
        if i < 99:
            i += 1
    return chordLengthList
calculateChordLength()


# Function to plot histogram
def plotHistogram():
    n, bins, patches = plt.hist(chordLengthList, weights=np.ones_like(chordLengthList) / len(chordLengthList),
                            color='#0A4614', alpha=0.5, edgecolor = 'black')

    plt.xlabel('Chord Length/cm', fontsize = 13)
    plt.ylabel('Probability', fontsize = 13)
    plt.title('Probability Of Chord Lengths', fontsize = 15)
    # plt.ylim([0, 0.5])
    plt.grid()
    plt.show()
(plotHistogram())


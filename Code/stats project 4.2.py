import math
import matplotlib.pyplot as plt
import numpy as np

# For all parts, we will assume radius r = 10 cm
r = 10
chordLengthList = []


# Function to randomly select an angle theta between 0 and 2pi. 
def selectAngle():
    thetaList = []
    i = 0
    while len(thetaList) < 100: 
        theta = np.random.uniform(0, 360) # thetas are uniformly selected
        thetaList.append(theta)
    return thetaList

def pointOfBisection():
    angles = selectAngle()
    bisectionList = []
    for i in angles:
        x = r*(math.sin(math.radians(i))) # x and y coordinates found of the line formed by angle from center of circle to boundary
        y = r*(math.sin(math.radians(i)))
        xRand = np.random.uniform(0, x) # xRand and yRand are random bisection point coordinates
        yRand = np.random.uniform(0, y)
        tup = (xRand, yRand) # cooridantes stored in tuple
        bisectionList.append(tup) # list of bisection points corresponding to different randomly selected angles
    return bisectionList

def lengthOfChord():
    global chordLengthList
    bisection = pointOfBisection()
    for i in bisection:
        triangleSideLength = math.sqrt((i[0]**2 + i[1]**2)) # length of one side of triangle: √(x2 − x1)^2 + (y2 − y1)^2
        chordLength = 2*(math.sqrt(abs(r**2 - triangleSideLength**2))) # r^2 = a^2 + c^2 = c^2 = |r^2 - b^2|, 2*√c
        chordLengthList.append(chordLength) # chord lengths stored in list
    return chordLengthList
print(lengthOfChord())

# Function to plot histogram
def plotHistogram():
    n, bins, patches = plt.hist(chordLengthList, weights=np.ones_like(chordLengthList) / len(chordLengthList),
                            color='#22827A', alpha=0.5, edgecolor = 'black')
    plt.xlabel('Chord Length/cm', fontsize = 13)
    plt.ylabel('Probability', fontsize = 13)
    plt.title('Probability Of Chord Lengths', fontsize = 15)
    
    plt.grid()
    plt.show()
(plotHistogram())
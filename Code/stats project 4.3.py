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

def chordMidpoint():
    angles = selectAngle()
    chordMidPointList = []
    for i in angles:
        x = r*(math.sin(math.radians(i))) # x and y coordinates found of the line formed by angle from center of circle to boundary
        y = r*(math.sin(math.radians(i)))
        xRand = np.random.uniform(r, -r) # xRand and yRand are midpoint of random chord
        yRand = np.random.uniform(r, -r)
        tup = (xRand, yRand) # cooridantes stored in tuple
        chordMidPointList.append(tup) # list of bisection points corresponding to different randomly selected angles
    return chordMidPointList

def lengthOfChord():
    global chordLengthList
    midpoint = chordMidpoint()
    for i in midpoint:
        triangleSideLength = math.sqrt((i[0]**2 + i[1]**2)) # length of one side of triangle: √(x2 − x1)^2 + (y2 − y1)^2
        chordLength = 2*(math.sqrt(abs(r**2 - triangleSideLength**2))) # r^2 = a^2 + c^2 = c^2 = |r^2 - b^2|, 2*√c
        chordLengthList.append(chordLength) # chord lengths stored in list
    return chordLengthList
print(lengthOfChord())

# Function to plot histogram
def plotHistogram():
    n, bins, patches = plt.hist(chordLengthList, weights=np.ones_like(chordLengthList) / len(chordLengthList),
                            color='#EE5E5E', alpha=0.5, edgecolor = 'white')
    plt.xlabel('Chord Length/cm', fontsize = 13)
    plt.ylabel('Probability', fontsize = 13)
    plt.title('Probability Of Chord Lengths', fontsize = 15)
    # plt.ylim([0, 0.50])
    plt.grid()
    plt.show()
(plotHistogram())
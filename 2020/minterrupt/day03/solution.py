import io
import os
from functools import reduce

os.chdir(os.path.dirname(__file__))

firstSlop = 3
firstLog = []
slopes = []
slopeIds = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
logsJammed = 0

def collect():
    global slopes
    with open("input.txt", "r") as inputFillet:
        for line in inputFillet:
            slopes.append(list(line))

def traverseSlopes(slide, skipper=1, results=[]):
    global slopes
    totes = 0
    modelo = len(slopes[0]) - 1
    bottomText = len(slopes)
    existanceOffset = 0
    descentAngle = slide
    for i in range(0, bottomText, skipper):
        trueSpace = existanceOffset % modelo
        print(existanceOffset)
        print(trueSpace)
        if slopes[i][trueSpace] == "#":
            totes += 1
        existanceOffset += descentAngle
    results.append(totes)

def checkAllSlopes(slopeIds):
    global logsJammed
    cosmicLebowski = []
    for id in slopeIds:
        traverseSlopes(id[0], id[1], cosmicLebowski)
    logsJammed = reduce((lambda x, y: x * y), cosmicLebowski)
    
collect()
traverseSlopes(firstSlop, results=firstLog)
checkAllSlopes(slopeIds)
# print("slopes: " + str(slopes))
print("logs jammed: " + str(logsJammed))
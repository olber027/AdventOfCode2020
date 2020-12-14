'''
Your ferry made decent progress toward the island, but the storm came in faster than anyone expected. The ferry needs to take evasive actions!

Unfortunately, the ship's navigation computer seems to be malfunctioning; rather than giving a route directly to safety, it produced extremely circuitous instructions. When the captain uses the PA system to ask if anyone can help, you quickly volunteer.

The navigation instructions (your puzzle input) consists of a sequence of single-character actions paired with integer input values. After staring at them for a few minutes, you work out what they probably mean:

Action N means to move north by the given value.
Action S means to move south by the given value.
Action E means to move east by the given value.
Action W means to move west by the given value.
Action L means to turn left the given number of degrees.
Action R means to turn right the given number of degrees.
Action F means to move forward by the given value in the direction the ship is currently facing.
The ship starts by facing east. Only the L and R actions change the direction the ship is facing. (That is, if the ship is facing east and the next instruction is N10, the ship would move north 10 units, but would still move east if the following action were F.)

For example:

F10
N3
F7
R90
F11
These instructions would be handled as follows:

F10 would move the ship 10 units east (because the ship starts by facing east) to east 10, north 0.
N3 would move the ship 3 units north to east 10, north 3.
F7 would move the ship another 7 units east (because the ship is still facing east) to east 17, north 3.
R90 would cause the ship to turn right by 90 degrees and face south; it remains at east 17, north 3.
F11 would move the ship 11 units south to east 17, south 8.
At the end of these instructions, the ship's Manhattan distance (sum of the absolute values of its east/west position and its north/south position) from its starting position is 17 + 8 = 25.

Figure out where the navigation instructions lead. What is the Manhattan distance between that location and the ship's starting position?
'''
import re
import math

def addTuple(first, second):
    firstList = list(first)
    secondList = list(second)
    firstIndex = 0
    secondIndex = 0
    resultList = []
    while firstIndex < len(firstList) and secondIndex < len(secondList):
        resultList.append(firstList[firstIndex] + secondList[secondIndex])
        firstIndex += 1
        secondIndex += 1
    return tuple(resultList)

def multiplyTuple(tup, scale):
    result = []
    for num in tup:
        result.append(num * scale)
    return tuple(result)

def degreesToRadians(degrees):
    return (degrees * math.pi) / 180.0

def convertAngleToVector(angle):
    return (math.cos(degreesToRadians(angle)), math.sin(degreesToRadians(angle)))

def convertCardinalDirectionToAngle(direction):
    dirMap = {"N":90, "E":0, "S":270, "W":180}
    return dirMap[direction]

class Ship:
    def __init__(self):
        self.coords = (0,0)
        self.orientation = 0

    def moveForward(self, distance):
        moveVector = multiplyTuple(convertAngleToVector(self.orientation), distance)
        self.coords = addTuple(self.coords, moveVector)

    def move(self, direction, distance):
        moveVector = multiplyTuple(convertAngleToVector(direction), distance)
        self.coords = addTuple(self.coords, moveVector)

    def rotate(self, angle):
        self.orientation += angle

    def __repr__(self):
        return "{} -> {}".format(self.coords, self.orientation)

ship = Ship()
inputRegex = re.compile("(?P<Direction>\w)(?P<Amount>\d+)")

with open("Data\input.txt", "r") as inputFile:
    for line in inputFile:
        line = line.strip()
        command = inputRegex.match(line).groupdict()
        if command["Direction"] == "F":
            ship.moveForward(int(command["Amount"]))
        elif command["Direction"] == "R":
            ship.rotate(-1*int(command["Amount"]))
        elif command["Direction"] == "L":
            ship.rotate(int(command["Amount"]))
        else:
            ship.move(convertCardinalDirectionToAngle(command["Direction"]), int(command["Amount"]))

print(abs(ship.coords[0]) + abs(ship.coords[1]))


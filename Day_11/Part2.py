'''
As soon as people start to arrive, you realize your mistake. People don't just care about adjacent seats - they care about the first seat they can see in each of those eight directions!

Now, instead of considering just the eight immediately adjacent seats, consider the first seat in each of those eight directions. For example, the empty seat below would see eight occupied seats:

.......#.
...#.....
.#.......
.........
..#L....#
....#....
.........
#........
...#.....
The leftmost empty seat below would only see one empty seat, but cannot see any of the occupied ones:

.............
.L.L.#.#.#.#.
.............
The empty seat below would see no occupied seats:

.##.##.
#.#.#.#
##...##
...L...
##...##
#.#.#.#
.##.##.
Also, people seem to be more tolerant than you expected: it now takes five or more visible occupied seats for an occupied seat to become empty (rather than four or more from the previous rules). The other rules still apply: empty seats that see no occupied seats become occupied, seats matching no rule don't change, and floor never changes.

Given the same starting layout as above, these new rules cause the seating area to shift around as follows:

L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL
#.##.##.##
#######.##
#.#.#..#..
####.##.##
#.##.##.##
#.#####.##
..#.#.....
##########
#.######.#
#.#####.##
#.LL.LL.L#
#LLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLL#
#.LLLLLL.L
#.LLLLL.L#
#.L#.##.L#
#L#####.LL
L.#.#..#..
##L#.##.##
#.##.#L.##
#.#####.#L
..#.#.....
LLL####LL#
#.L#####.L
#.L####.L#
#.L#.L#.L#
#LLLLLL.LL
L.L.L..#..
##LL.LL.L#
L.LL.LL.L#
#.LLLLL.LL
..L.L.....
LLLLLLLLL#
#.LLLLL#.L
#.L#LL#.L#
#.L#.L#.L#
#LLLLLL.LL
L.L.L..#..
##L#.#L.L#
L.L#.#L.L#
#.L####.LL
..#.#.....
LLL###LLL#
#.LLLLL#.L
#.L#LL#.L#
#.L#.L#.L#
#LLLLLL.LL
L.L.L..#..
##L#.#L.L#
L.L#.LL.L#
#.LLLL#.LL
..#.L.....
LLL###LLL#
#.LLLLL#.L
#.L#LL#.L#
Again, at this point, people stop shifting around and the seating area reaches equilibrium. Once this occurs, you count 26 occupied seats.

Given the new visibility method and the rule change for occupied seats becoming empty, once equilibrium is reached, how many seats end up occupied?
'''

import copy

def isInBounds(layout, coords):
    if coords[0] < 0 or coords[0] >= len(layout):
        return False
    if coords[1] < 0 or coords[1] >= len(layout[coords[0]]):
        return False
    return True

def update(currentCoords, directionVector):
    return (currentCoords[0] + directionVector[0], currentCoords[1] + directionVector[1])

def checkDirection(layout, rowIndex, columnIndex, directionVector):
    currentPosition = update((rowIndex, columnIndex), directionVector)
    while isInBounds(layout, currentPosition):
        currentCharacter = layout[currentPosition[0]][currentPosition[1]]
        currentPosition = update(currentPosition, directionVector)
        if currentCharacter == ".":
            continue
        if currentCharacter == "L":
            return 0
        if currentCharacter == "#":
            return 1
    return 0

def isOccupied(layout, rowIndex, columnIndex):
    if not isInBounds(layout, (rowIndex, columnIndex)):
        return 0
    if layout[rowIndex][columnIndex] == "#":
        return 1
    return 0

def getNumOccupiedSeatsInSightLines(layout, rowIndex, columnIndex):
    totalOccupiedSeats = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            totalOccupiedSeats += checkDirection(layout, rowIndex, columnIndex, (i, j))
    return totalOccupiedSeats

seatLayout = []

with open("Data\input.txt", "r") as inputFile:
    for line in inputFile:
        seatLayout.append([])
        for character in line.strip():
            seatLayout[-1].append(character)

previousLayout = []
while previousLayout != seatLayout:
    newLayout = copy.deepcopy(seatLayout)
    previousLayout = copy.deepcopy(seatLayout)
    for i in range(len(seatLayout)):
        for j in range(len(seatLayout[i])):
            if seatLayout[i][j] == ".":
                continue
            if not isOccupied(seatLayout, i, j) and getNumOccupiedSeatsInSightLines(seatLayout, i, j) == 0:
                newLayout[i][j] = "#"
            elif isOccupied(seatLayout, i, j) and getNumOccupiedSeatsInSightLines(seatLayout, i, j) >= 5:
                newLayout[i][j] = "L"
    seatLayout = copy.deepcopy(newLayout)


totalOccupiedSeats = 0
for i in range(len(seatLayout)):
    for j in range(len(seatLayout[i])):
        totalOccupiedSeats += isOccupied(seatLayout, i, j)
print(totalOccupiedSeats)
'''
Your plane lands with plenty of time to spare. The final leg of your journey is a ferry that goes directly to the tropical island where you can finally start your vacation. As you reach the waiting area to board the ferry, you realize you're so early, nobody else has even arrived yet!

By modeling the process people use to choose (or abandon) their seat in the waiting area, you're pretty sure you can predict the best place to sit. You make a quick map of the seat layout (your puzzle input).

The seat layout fits neatly on a grid. Each position is either floor (.), an empty seat (L), or an occupied seat (#). For example, the initial seat layout might look like this:

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
Now, you just need to model the people who will be arriving shortly. Fortunately, people are entirely predictable and always follow a simple set of rules. All decisions are based on the number of occupied seats adjacent to a given seat (one of the eight positions immediately up, down, left, right, or diagonal from the seat). The following rules are applied to every seat simultaneously:

If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
If a seat is occupied (#) and four or more seats adjacent to it are also occupied, the seat becomes empty.
Otherwise, the seat's state does not change.
Floor (.) never changes; seats don't move, and nobody sits on the floor.

After one round of these rules, every seat in the example layout becomes occupied:

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
After a second round, the seats with four or more occupied adjacent seats become empty again:

#.LL.L#.##
#LLLLLL.L#
L.L.L..L..
#LLL.LL.L#
#.LL.LL.LL
#.LLLL#.##
..L.L.....
#LLLLLLLL#
#.LLLLLL.L
#.#LLLL.##
This process continues for three more rounds:

#.##.L#.##
#L###LL.L#
L.#.#..#..
#L##.##.L#
#.##.LL.LL
#.###L#.##
..#.#.....
#L######L#
#.LL###L.L
#.#L###.##
#.#L.L#.##
#LLL#LL.L#
L.L.L..#..
#LLL.##.L#
#.LL.LL.LL
#.LL#L#.##
..L.L.....
#L#LLLL#L#
#.LLLLLL.L
#.#L#L#.##
#.#L.L#.##
#LLL#LL.L#
L.#.L..#..
#L##.##.L#
#.#L.LL.LL
#.#L#L#.##
..L.L.....
#L#L##L#L#
#.LLLLLL.L
#.#L#L#.##
At this point, something interesting happens: the chaos stabilizes and further applications of these rules cause no seats to change state! Once people stop moving around, you count 37 occupied seats.

Simulate your seating area by applying the seating rules repeatedly until no seats change state. How many seats end up occupied?
'''
import copy

def isOccupied(layout, rowIndex, columnIndex):
    if rowIndex < 0 or rowIndex >= len(layout):
        return 0
    if columnIndex < 0 or columnIndex >= len(layout[rowIndex]):
        return 0
    if layout[rowIndex][columnIndex] == "#":
        return 1
    return 0

def getNumOccupiedAdjacentSeats(layout, rowIndex, columnIndex):
    totalOccupiedSeats = 0
    for i in range(rowIndex - 1, rowIndex + 2):
        for j in range(columnIndex - 1, columnIndex + 2):
            if i == rowIndex and j == columnIndex:
                continue
            totalOccupiedSeats += isOccupied(layout, i, j)
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
            if not isOccupied(seatLayout, i, j) and getNumOccupiedAdjacentSeats(seatLayout, i, j) == 0:
                newLayout[i][j] = "#"
            elif isOccupied(seatLayout, i, j) and getNumOccupiedAdjacentSeats(seatLayout, i, j) >= 4:
                newLayout[i][j] = "L"
    seatLayout = copy.deepcopy(newLayout)


totalOccupiedSeats = 0
for i in range(len(seatLayout)):
    for j in range(len(seatLayout[i])):
        totalOccupiedSeats += isOccupied(seatLayout, i, j)
print(totalOccupiedSeats)
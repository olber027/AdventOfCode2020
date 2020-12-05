'''
Ding! The "fasten seat belt" signs have turned on. Time to find your seat.

It's a completely full flight, so your seat should be the only missing boarding pass in your list. However, there's a catch: some of the seats at the very front and back of the plane don't exist on this aircraft, so they'll be missing from your list as well.

Your seat wasn't at the very front or back, though; the seats with IDs +1 and -1 from yours will be in your list.

What is the ID of your seat?
'''

numRows = 128
numColumns = 8

ticketIDs = []

with open("Data\input.txt", "r") as inputFile:
    for line in inputFile:
        rowRange = range(numRows)
        columnRange = range(numColumns)
        line = line.strip()

        rowSpecifiers = line[:7]
        columnSpecifiers = line[-3:]

        for spec in rowSpecifiers:
            if spec == "F":
                rowRange = rowRange[:int(len(rowRange)/2)]
            else:
                rowRange = rowRange[int(len(rowRange)/2):]

        for spec in columnSpecifiers:
            if spec == "L":
                columnRange = columnRange[:int(len(columnRange)/2)]
            else:
                columnRange = columnRange[int(len(columnRange)/2):]

        ticketIDs.append(rowRange[0]*8 + columnRange[0])

ticketIDs = sorted(ticketIDs)
for index in range(len(ticketIDs) - 1):
    if ticketIDs[index + 1] != (ticketIDs[index] + 1):
        print(ticketIDs[index] + 1)
        break
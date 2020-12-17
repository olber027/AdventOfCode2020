'''
Now that you've identified which tickets contain invalid values, discard those tickets entirely. Use the remaining valid tickets to determine which field is which.

Using the valid ranges for each field, determine what order the fields appear on the tickets. The order is consistent between all tickets: if seat is the third field, it is the third field on every ticket, including your ticket.

For example, suppose you have the following notes:

class: 0-1 or 4-19
row: 0-5 or 8-19
seat: 0-13 or 16-19

your ticket:
11,12,13

nearby tickets:
3,9,18
15,1,5
5,14,9
Based on the nearby tickets in the above example, the first position must be row, the second position must be class, and the third position must be seat; you can conclude that in your ticket, class is 12, row is 11, and seat is 13.

Once you work out which field is which, look for the six fields on your ticket that start with the word departure. What do you get if you multiply those six values together?
'''

def findValidRules(num, ruleDict):
    results = []
    for ruleName in ruleDict:
        for validRange in ruleDict[ruleName]:
            if num >= validRange[0] and num <= validRange[1]:
                results.append(ruleName)
                break
    return results

ticketRules = {}
myTicket = []
otherTickets = []
inputSections = []

with open("Data\input.txt", "r") as inputFile:
    inputSections = inputFile.read().split("\n\n")

for rule in inputSections[0].splitlines():
    ruleName, ranges = rule.split(":")
    ticketRules[ruleName] = []
    ranges = [x.strip() for x in ranges.split("or")]
    for r in ranges:
        parsedRange = [int(x) for x in r.split("-")]
        ticketRules[ruleName].append(tuple(parsedRange))

myTicket = [int(x) for x in inputSections[1].splitlines()[1].split(",")]

for line in inputSections[2].splitlines():
    if "," in line:
        otherTickets.append([int(x) for x in line.split(",")])

validTickets = []
possibleFields = [set(ticketRules.keys()) for _ in range(len(myTicket))]

for ticket in otherTickets:
    isValid = True
    for field in ticket:
        if len(findValidRules(field, ticketRules)) == 0:
            isValid = False
            break
    if isValid:
        validTickets.append(ticket)

for ticket in validTickets:
    for index in range(len(ticket)):
        possibleRules = findValidRules(ticket[index], ticketRules)
        possibleFields[index].intersection_update(set(possibleRules))

certainFields = [(x[0], str(list(x[1])[0])) for x in enumerate(possibleFields) if len(x[1]) == 1]

while len(certainFields) < len(possibleFields):
    for field in certainFields:
        for fields in possibleFields:
            if field[1] in fields:
                fields.remove(field[1])
    for index in range(len(possibleFields)):
        if len(possibleFields[index]) == 1:
            certainFields.append((index, list(possibleFields[index])[0]))

total = 1
for field in certainFields:
    if "departure" in field[1]:
        total *= myTicket[field[0]]
print(total)

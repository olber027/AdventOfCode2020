'''
As you finish the last group's customs declaration, you notice that you misread one word in the instructions:

You don't need to identify the questions to which anyone answered "yes"; you need to identify the questions to which everyone answered "yes"!

Using the same example as above:

abc

a
b
c

ab
ac

a
a
a
a

b
This list represents answers from five groups:

In the first group, everyone (all 1 person) answered "yes" to 3 questions: a, b, and c.
In the second group, there is no question to which everyone answered "yes".
In the third group, everyone answered yes to only 1 question, a. Since some people did not answer "yes" to b or c, they don't count.
In the fourth group, everyone answered yes to only 1 question, a.
In the fifth group, everyone (all 1 person) answered "yes" to 1 question, b.
In this example, the sum of these counts is 3 + 0 + 1 + 1 + 1 = 6.

For each group, count the number of questions to which everyone answered "yes". What is the sum of those counts?
'''
def calculateGroupIntersection(groupList):
    if len(groupList) == 0:
        return set()
    if len(groupList) == 1:
        return groupList[0]
    result = groupList[0]
    for person in groupList[1:]:
        result.intersection_update(person)
    return result

total = 0

with open("Data\input.txt", "r") as inputFile:
    currentGroup = []
    for line in [l.strip() for l in inputFile]:
        if len(line) == 0:
            total += len(calculateGroupIntersection(currentGroup))
            currentGroup = []
        else:
            currentGroup.append(set(list(line)))
    if len(currentGroup) > 0:
        total += len(calculateGroupIntersection(currentGroup))
print(total)
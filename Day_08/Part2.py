'''
After some careful analysis, you believe that exactly one instruction is corrupted.

Somewhere in the program, either a jmp is supposed to be a nop, or a nop is supposed to be a jmp. (No acc instructions were harmed in the corruption of this boot code.)

The program is supposed to terminate by attempting to execute an instruction immediately after the last instruction in the file. By changing exactly one jmp or nop, you can repair the boot code and make it terminate correctly.

For example, consider the same program from above:

nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6
If you change the first instruction from nop +0 to jmp +0, it would create a single-instruction infinite loop, never leaving that instruction. If you change almost any of the jmp instructions, the program will still eventually find another jmp instruction and loop forever.

However, if you change the second-to-last instruction (from jmp -4 to nop -4), the program terminates! The instructions are visited in this order:

nop +0  | 1
acc +1  | 2
jmp +4  | 3
acc +3  |
jmp -3  |
acc -99 |
acc +1  | 4
nop -4  | 5
acc +6  | 6
After the last instruction (acc +6), the program terminates by attempting to run the instruction below the last instruction in the file. With this change, after the program terminates, the accumulator contains the value 8 (acc +1, acc +1, acc +6).

Fix the program so that it terminates normally by changing exactly one jmp (to nop) or nop (to jmp). What is the value of the accumulator after the program terminates?
'''

originalOperationList = []

with open("Data\input.txt", "r") as inputFile:
    for line in inputFile:
        operation, number = line.split()
        number = int(number)
        originalOperationList.append((operation, number))

possibleOperationLists = []

for i in range(len(originalOperationList)):
    if originalOperationList[i][0] == "nop":
        tmp = originalOperationList.copy()
        tmp[i] = "jmp"
        possibleOperationLists.append(tmp.copy())
    elif originalOperationList[i][0] == "jmp":
        tmp = originalOperationList.copy()
        tmp[i] = "nop"
        possibleOperationLists.append(tmp.copy())

for operationList in possibleOperationLists:
    accumulatedTotal = 0
    currentIndex = 0
    executionList = [0] * len(operationList)
    while currentIndex < len(executionList) and executionList[currentIndex] == 0:
        executionList[currentIndex] += 1
        currentOperation = operationList[currentIndex][0]
        if currentOperation == "jmp":
            currentIndex += operationList[currentIndex][1]
            continue
        if currentOperation == "acc":
            accumulatedTotal += operationList[currentIndex][1]
        currentIndex += 1
    if currentIndex == len(operationList):
        print(accumulatedTotal)
        break
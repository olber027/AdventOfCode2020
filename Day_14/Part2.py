'''
For some reason, the sea port's computer system still can't communicate with your ferry's docking program. It must be using version 2 of the decoder chip!

A version 2 decoder chip doesn't modify the values being written at all. Instead, it acts as a memory address decoder. Immediately before a value is written to memory, each bit in the bitmask modifies the corresponding bit of the destination memory address in the following way:

If the bitmask bit is 0, the corresponding memory address bit is unchanged.
If the bitmask bit is 1, the corresponding memory address bit is overwritten with 1.
If the bitmask bit is X, the corresponding memory address bit is floating.
A floating bit is not connected to anything and instead fluctuates unpredictably. In practice, this means the floating bits will take on all possible values, potentially causing many memory addresses to be written all at once!

For example, consider the following program:

mask = 000000000000000000000000000000X1001X
mem[42] = 100
mask = 00000000000000000000000000000000X0XX
mem[26] = 1
When this program goes to write to memory address 42, it first applies the bitmask:

address: 000000000000000000000000000000101010  (decimal 42)
mask:    000000000000000000000000000000X1001X
result:  000000000000000000000000000000X1101X
After applying the mask, four bits are overwritten, three of which are different, and two of which are floating. Floating bits take on every possible combination of values; with two floating bits, four actual memory addresses are written:

000000000000000000000000000000011010  (decimal 26)
000000000000000000000000000000011011  (decimal 27)
000000000000000000000000000000111010  (decimal 58)
000000000000000000000000000000111011  (decimal 59)
Next, the program is about to write to memory address 26 with a different bitmask:

address: 000000000000000000000000000000011010  (decimal 26)
mask:    00000000000000000000000000000000X0XX
result:  00000000000000000000000000000001X0XX
This results in an address with three floating bits, causing writes to eight memory addresses:

000000000000000000000000000000010000  (decimal 16)
000000000000000000000000000000010001  (decimal 17)
000000000000000000000000000000010010  (decimal 18)
000000000000000000000000000000010011  (decimal 19)
000000000000000000000000000000011000  (decimal 24)
000000000000000000000000000000011001  (decimal 25)
000000000000000000000000000000011010  (decimal 26)
000000000000000000000000000000011011  (decimal 27)
The entire 36-bit address space still begins initialized to the value 0 at every address, and you still need the sum of all values left in memory at the end of the program. In this example, the sum is 208.

Execute the initialization program using an emulator for a version 2 decoder chip. What is the sum of all values left in memory after it completes?
'''
import re
import copy

def toBitList(num, numBits):
    if num >= pow(2, numBits):
        return []
    result = [0] * numBits
    for currentBit in reversed(range(numBits)):
        if pow(2, currentBit) <= num:
            result[numBits - currentBit - 1] = 1
            num -= pow(2, currentBit)
    return result

def fromBitList(bitList):
    result = 0
    littleEndianList = list(reversed(bitList))
    for bit in  range(len(bitList)):
        result += pow(2, bit) * littleEndianList[bit]
    return result

def isDigit(character):
    return character in "1234567890"

class ModifiedMask:
    def __init__(self, size):
        self.mask = ["X"] * size

    def update(self, newMask):
        self.mask = []
        for character in newMask:
            if isDigit(character):
                self.mask.append(int(character))
            else:
                self.mask.append(character)

    def __resolveFloatingBits(self, bitListWithFloatingBits):
        WIPStack = [bitListWithFloatingBits]
        resolvedBitLists = []
        while len(WIPStack) > 0:
            current = WIPStack.pop(0)
            if "X" not in current:
                resolvedBitLists.append(copy.deepcopy(current))
                continue
            xIndex = current.index("X")
            current[xIndex] = 1
            WIPStack.append(copy.deepcopy(current))
            current[xIndex] = 0
            WIPStack.append(copy.deepcopy(current))
        return resolvedBitLists

    def doMask(self, number):
        bitwiseNumber = toBitList(number, len(self.mask))
        for index in range(len(self.mask)):
            if self.mask[index] == "X" or self.mask[index] == 1:
                bitwiseNumber[index] = self.mask[index]
        resolvedBitwiseNumbers = self.__resolveFloatingBits(bitwiseNumber)
        return [fromBitList(num) for num in resolvedBitwiseNumbers]

maskRegex = re.compile("mask = (?P<mask>[X10]{36})")
valueRegex = re.compile("mem\[(?P<address>\d+)\] = (?P<value>\d+)")

memoryLocations = {}
modifiedMask = ModifiedMask(36)

with open("Data\input.txt", "r") as inputFile:
    for line in inputFile:
        maskResult = maskRegex.match(line)
        if maskResult is not None:
            modifiedMask.update(maskResult.group("mask"))
            continue
        valueResult = valueRegex.match(line)
        memAddress = int(valueResult.group("address"))
        value = int(valueResult.group("value"))
        maskedAddresses = modifiedMask.doMask(memAddress)
        for address in maskedAddresses:
            memoryLocations[address] = value

print(sum(memoryLocations.values()))
'''
The final step in breaking the XMAS encryption relies on the invalid number you just found: you must find a contiguous set of at least two numbers in your list which sum to the invalid number from step 1.

Again consider the above example:

35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576
In this list, adding up all of the numbers from 15 through 40 produces the invalid number from step 1, 127. (Of course, the contiguous set of numbers in your actual list might be much longer.)

To find the encryption weakness, add together the smallest and largest number in this contiguous range; in this example, these are 15 and 47, producing 62.

What is the encryption weakness in your XMAS-encrypted list of numbers?
'''

# answer from example 1
target = 18272118

data = []
with open("Data\input.txt", "r") as inputFile:
    data = [int(line) for line in inputFile]

for currentStart in range(len(data) - 1):
    print(currentStart)
    currentEnd = currentStart + 1
    testBlock = data[currentStart:currentEnd]
    while sum(testBlock) < target:
        currentEnd += 1
        testBlock = data[currentStart:currentEnd]
    if sum(testBlock) == target:
        print(max(testBlock) + min(testBlock))
        break
    currentStart += 1

'''
The Elves in accounting are thankful for your help; one of them even offers you a starfish coin they had left over from a past vacation. They offer you a second one if you can find three numbers in your expense report that meet the same criteria.

Using the above example again, the three entries that sum to 2020 are 979, 366, and 675. Multiplying them together produces the answer, 241861950.

In your expense report, what is the product of the three entries that sum to 2020?
'''

def extractTuple(targetList, index1, index2, index3):
    return targetList[index1], targetList[index2], targetList[index3]

inputData = []

with open("Data\input.txt", "r") as inFile:
    for num in inFile:
        inputData.append(int(num))

inputData = sorted(inputData)

target = 2020

for smallIndex in range(len(inputData) - 2):
    middleIndex = smallIndex + 1
    bigIndex = len(inputData) - 1
    while middleIndex < bigIndex:
        small, middle, big = extractTuple(inputData, smallIndex, middleIndex, bigIndex)
        total = small + middle + big
        if total == target:
            print(small * middle * big)
            exit()
        elif total > target:
            bigIndex -= 1
        else:
            middleIndex += 1



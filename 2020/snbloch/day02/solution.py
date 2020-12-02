import io

def part1():
    values = []
    with open('input.txt', 'r') as inputfile:
        for line in inputfile:
            line = line.split(' ')
            minOccur = int(line[0].split('-')[0])
            maxOccur = int(line[0].split('-')[1])
            repeatedChar = line[1].split(':')[0]
            password = line[2].strip()
            values.append([minOccur, maxOccur, repeatedChar, password])
    validCount = 0
    i = 0
    while i < len(values):
        if (values[i][3].count(values[i][2]) >= values[i][0] and values[i][3].count(values[i][2]) <= values[i][1]):
            validCount += 1
        i += 1
    print(validCount)

def part2():
    values = []
    with open('input.txt', 'r') as inputfile:
        for line in inputfile:
            line = line.split(' ')
            firstPos = int(line[0].split('-')[0])
            secondPos = int(line[0].split('-')[1])
            evalChar = line[1].split(':')[0]
            password = line[2].strip()
            values.append([firstPos, secondPos, evalChar, password])
    validCount = 0
    i = 0
    while i < len(values):
        if (values[i][3][values[i][0] - 1] == values[i][2] and not values[i][3][values[i][1] - 1] == values[i][2]):
            validCount += 1
        elif (values[i][3][values[i][1] - 1] == values[i][2] and not values[i][3][values[i][0] - 1] == values[i][2]):
            validCount += 1
        i += 1
    print(validCount)

if __name__ == '__main__':
    part1()
    part2()


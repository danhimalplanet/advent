import io

def part1():
    curX = 0
    curY = 0
    treeCount = 0
    incrX = 3
    incrY = 1
    values = []
    with open('input.txt', 'r') as inputfile:
        for line in inputfile:
            values.append(line.strip())
    lineWidth = len(values[0])
    while curY < len(values):
        if (values[curY][curX % lineWidth] == '#'):
            treeCount += 1
        curX += incrX
        curY += incrY
    print(treeCount)

def part2():
    slopes = [(1,1), (3,1), (5,1), (7,1), (1,2)]
    totalTrees = 0
    for i in slopes:
        curX = 0
        curY = 0
        treeCount = 0
        incrX = i[0]
        incrY = i[1]
        values = []
        with open('input.txt', 'r') as inputfile:
            for line in inputfile:
                values.append(line.strip())
        lineWidth = len(values[0])
        while curY < len(values):
            if (values[curY][curX % lineWidth] == '#'):
                treeCount += 1
            curX += incrX
            curY += incrY
        if not totalTrees:
            totalTrees = treeCount
        else:
            totalTrees *= treeCount
    print(totalTrees)

if __name__ == '__main__':
    part1()
    part2()
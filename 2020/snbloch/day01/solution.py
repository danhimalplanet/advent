import io

def part1():
    values = []
    with open('input.txt', 'r') as inputfile:
        for line in inputfile:
           values.append(int(line))
    i = 0
    while i < len(values):
        j = i + 1
        while j < len(values):
            if (values[i] + values[j]) == 2020:
                print(values[i] * values[j])
                break
            j += 1
        i += 1

def part2():
    values = []
    with open('input.txt', 'r') as inputfile:
        for line in inputfile:
           values.append(int(line))
    i = 0
    while i < len(values):
        j = i + 1
        while j < len(values):
            k = j + 1
            while k < len(values):
                if (values[i] + values[j] + values[k]) == 2020:
                    print(values[i] * values[j] * values[k])
                    break
                k += 1
            j += 1
        i += 1

if __name__ == '__main__':
    part1()
    part2()


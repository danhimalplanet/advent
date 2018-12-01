import io

def frequency_change(curr, change):
    if change[0] == '+':
        curr += int(change[1:])
    elif change[0] == '-':
        curr -= int(change[1:])
    return curr

def part1():
    current_frequency = 0
    inputfile = open('part1.txt', 'r')
    for line in inputfile:
        current_frequency = frequency_change(current_frequency, line)
    print 'Part 1, Final Frequency: ' + str(current_frequency)
    inputfile.close()
    return

def part2():
    current_frequency = 0
    repeated_frequency = None
    seen = set([])
    seen.add(current_frequency)
    while repeated_frequency == None:
        inputfile = open('part2.txt', 'r')
        for line in inputfile:
            current_frequency = frequency_change(current_frequency, line)
            if current_frequency in seen:
                repeated_frequency = current_frequency
                print 'Part 2, First Repeated Frequency: ' + str(repeated_frequency)
                return
            else:
                seen.add(current_frequency)
        inputfile.close()

if __name__ == '__main__':
    part1()
    part2()

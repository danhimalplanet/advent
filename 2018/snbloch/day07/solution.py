import io

def part1():
    steps = {}
    final_output = ''
    with open('input.txt', 'r') as inputfile:
        for line in inputfile:
            line = line.strip().split()
            if steps.get(line[1]) is None:
                steps[line[1]] = []
            if steps.get(line[7]) is None:
                steps[line[7]] = []
    with open('input.txt', 'r') as inputfile:
        for line in inputfile:
            line = line.strip().split()
            steps[line[7]].append(line[1])
    while len(steps) > 0:
        changed = False
        round_output = ''
        for i in steps.keys():
            if len(steps[i]) == 0 and changed == False:
                round_output += i
                for j in steps.keys():
                    if i in steps[j]:
                        steps[j].remove(i)
                del steps[i]
                changed = True
            else:
                for j in steps[i]:
                    if j in final_output:
                        steps[i].remove(j)
                        changed = True
        for i in sorted(round_output):
            final_output += i
    print 'Part 1:',final_output



if __name__ == '__main__':
    part1()

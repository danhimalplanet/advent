def part1():
    values = []
    group_answers = []
    with open('input.txt', 'r') as inputfile:
        for line in inputfile.read().split('\n\n'):
            values.append(line.strip().replace('\n', ''))
    for v in values:
        ga = set()
        for i in v:
            ga.add(i)
        group_answers.append(ga)
    total = 0
    for ga in group_answers:
        total += len(ga)
    print(total)

def part2():
    values = []
    group_answers = []
    with open('input.txt', 'r') as inputfile:
        for line in inputfile.read().split('\n\n'):
            group_size = len(line.strip().split('\n'))
            values.append((line.strip().replace('\n', ''), group_size))
    for v in values:
        ga = set()
        for i in v[0]:
            if v[0].count(i) == v[1]:
                ga.add(i)
        group_answers.append(ga)
    total = 0
    for ga in group_answers:
        total += len(ga)
    print(total)

if __name__ == '__main__':
    part1()
    part2()
    
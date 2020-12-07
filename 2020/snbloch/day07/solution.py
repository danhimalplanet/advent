def part1():
    values = dict()
    with open('input.txt', 'r') as inputfile:
        for line in inputfile:
            line = line.split('bags contain')
            container = line[0].strip()
            contained = line[1].split(',')
            for i in range(len(contained)):
                contained[i] = contained[i].replace('.', '').replace('bags', '').replace('bag', '').strip()
            values[container] = contained
    contains_shiny_gold = set()
    for v in values:
        for i in values[v]:
            if 'shiny gold' in i:
                contains_shiny_gold.add(v)
    finished = False
    while finished == False:
        found_count = 0
        csg_iter = contains_shiny_gold.copy()
        for csg in csg_iter:
            for v in values:
                for i in values[v]:
                    if ' '.join(i.split()[1:]) ==  csg and v not in contains_shiny_gold:
                        contains_shiny_gold.add(v)
                        found_count += 1
        if found_count == 0:
            finished = True
    print(len(contains_shiny_gold))

def part2():
    values = dict()
    with open('input.txt', 'r') as inputfile:
        for line in inputfile:
            line = line.split('bags contain')
            container = line[0].strip()
            contained = line[1].split(',')
            for i in range(len(contained)):
                contained[i] = contained[i].replace('.', '').replace('bags', '').replace('bag', '').strip()
            values[container] = contained
    counter = 0
    finished = False
    next_depth = []
    for i in values['shiny gold']:
        for j in range(int((i.split()[0]))):
            counter += 1
            next_depth.append(' '.join(i.split()[1:]))
    while finished != True:
        if len(next_depth) == 0:
            finished = True
            continue
        else:
            nd = next_depth.copy()
            next_depth = []
            for i in nd:
                for v in values[i]:
                    if v.split()[0] == 'no':
                        continue
                    for j in range(int((v.split()[0]))):
                        counter += 1
                        next_depth.append(' '.join(v.split()[1:]))
    print(counter)

if __name__ == '__main__':
    part1()
    part2()
    
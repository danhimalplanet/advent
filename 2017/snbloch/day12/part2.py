import io
file = open('input.txt', 'r')

input = {}

for line in file:
    comms = []
    id = int(line.split('<->')[0].strip())
    for i in line.split('<->')[1].split(', '):
        comms.append(int(i.strip()))
    input[id] = comms

def calculate_group(num):
    output = []
    for i in input[num]:
        output.append(i)

    for id, comms in input.iteritems():
        if num in comms:
            for i in comms:
                output.append(i)

    start_count = len(set(output))
    end_count = 0

    while start_count != end_count:
        start_count = len(set(output))
        for i in set(output):
            for id, comms in input.iteritems():
                if id == i:
                    for j in comms:
                        output.append(j)
        end_count = len(set(output))
    return set(output)

iterator = 0
groups = {}
while iterator < len(input):
    group = calculate_group(iterator)
    if group not in groups.itervalues():
        groups[iterator] = group
    iterator += 1
    print groups

print len(groups)

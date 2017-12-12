import io
file = open('input.txt', 'r')

input = {}

for line in file:
    comms = []
    id = int(line.split('<->')[0].strip())
    for i in line.split('<->')[1].split(', '):
        comms.append(int(i.strip()))
    input[id] = comms

output = []

for i in input[0]:
    output.append(i)

for id, comms in input.iteritems():
    if 0 in comms:
        for i in comms:
            output.append(i)

start_count = len(set(output))
end_count = 0
iterator = 0

while start_count != end_count:
    start_count = len(set(output))
    for i in set(output):
        for id, comms in input.iteritems():
            if id == i:
                for j in comms:
                    output.append(j)
    end_count = len(set(output))

print set(output)
print len(set(output))

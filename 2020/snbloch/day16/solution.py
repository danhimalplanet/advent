from collections import defaultdict, Counter

def part1():
    filename = 'input.txt'
    valid = set()
    with open(filename, 'r') as inputfile:
        for line in inputfile:
            if len(line.strip().split(': ')) > 1:
                line = line.strip().split(': ')[1]
                for i in line.split(' or '):
                    for j in range(int(i.split('-')[0]), int(i.split('-')[1]) + 1):
                        valid.add(j)
    error_rate = 0
    with open(filename, 'r') as inputfile:
        for line in inputfile:
            if 'nearby tickets:' not in line:
                continue
            else:
                break
        for line in inputfile:
            for i in line.strip().split(','):
                if int(i) not in valid:
                    error_rate += int(i)
    print(error_rate)

def part2():
    field_order = {}
    filename = 'input.txt'
    fields = {}
    my_ticket = []
    nearby_tickets = []
    valid = set()
    with open(filename, 'r') as inputfile:
        for line in inputfile:
            if len(line.strip().split(': ')) > 1:
                line = line.strip().split(': ')[1]
                for i in line.split(' or '):
                    for j in range(int(i.split('-')[0]), int(i.split('-')[1]) + 1):
                        valid.add(j)
    with open(filename, 'r') as inputfile:
        for line in inputfile:
            if len(line.strip().split(': ')) > 1:
                fields[line.strip().split(': ')[0]] = []
                valid_in_line = line.strip().split(': ')[1]
                for i in valid_in_line.split(' or '):
                    for j in range(int(i.split('-')[0]), int(i.split('-')[1]) + 1):
                        fields[line.strip().split(': ')[0]].append(j) 
    with open(filename, 'r') as inputfile:
        for line in inputfile:
            if 'your ticket:' not in line:
                continue
            else:
                break
        for line in inputfile:
            if len(line.strip().split(',')) > 1:
                for i in line.strip().split(','):
                    my_ticket.append(int(i))
            else:
                break
    with open(filename, 'r') as inputfile:
        for line in inputfile:
            if 'nearby tickets:' not in line:
                continue
            else:
                break
        for line in inputfile:
            if len(line.strip().split(',')) > 1:
                ticket = []
                for i in line.strip().split(','):
                    ticket.append(int(i))
                nearby_tickets.append(ticket)
            else:
                break
    valid_tickets = []
    for ticket in nearby_tickets:
        valid_tickets.append(ticket)
        for column in ticket:
            if column not in valid:
                del valid_tickets[valid_tickets.index(ticket)]
    positions = defaultdict(list)
    for ticket in valid_tickets:
        counter = 0
        for column in ticket:
            for field in fields:
                if column in fields[field]:
                    positions[counter].append(field)
            counter += 1
    for i in positions:
        positions[i] = Counter(positions[i])
    for i in positions:
        for j in positions[i]:
            if positions[i][j] != len(valid_tickets):
                positions[i][j] = 0
    seen = set()
    while len(field_order) < len(my_ticket):
        for i in positions:
            curr = []
            for j in positions[i]:
                if j in seen:
                    continue
                else:
                    if positions[i][j] > 0:
                        curr.append(j)
            if len(curr) == 1:
                field_order[i] = curr[0]
                seen.add(curr[0])
    total = 1
    for i in field_order:
        if 'departure ' in field_order[i]:
            total *= my_ticket[i]
    print(total)



if __name__ == '__main__':
    part1()
    part2()
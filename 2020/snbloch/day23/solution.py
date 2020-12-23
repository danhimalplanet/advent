def part1():
    cups = []
    input = '364297581'
    for i in input:
        cups.append(int(i))
    curr = cups[0]
    for _ in range(100):
        moved = []
        destination = None
        for _ in range(3):
            cup = cups[(cups.index(curr) + 1) % len(cups)]
            moved.append(cups.pop(cups.index(cup)))
        if curr == min(cups):
            destination = cups.index(max(cups))
        else:
            dest_try = curr - 1
            while destination is None:
                if dest_try in cups:
                    destination = cups.index(dest_try)
                else:
                    if dest_try < min(cups):
                        destination = cups.index(max(cups))
                        continue
                    dest_try -= 1
        for m in moved:
            cups.insert(destination + 1, m)
            destination += 1
        if cups.index(curr) == len(cups) - 1:
            curr = cups[0]
        else:
            curr = cups[cups.index(curr) + 1]
    output = ''
    idx = cups.index(1) + 1
    while len(cups) > 1:
        if idx == len(cups):
            idx = 0
            output += str(cups.pop(idx))
        else:
            output += str(cups.pop(idx))
    print(output)

def part2():
    cups = []
    input = '364297581'
    for i in input:
        cups.append(int(i))
    cups += list(range(10,1000001))
    curr = cups[0]
    cups = dict(zip(cups, cups[1:] + cups[:1]))
    for _ in range(10000000):
        moved = [cups[curr], cups[cups[curr]], cups[cups[cups[curr]]]]
        destination = curr
        while destination == curr or destination in moved:
            destination = ((destination - 2) % len(cups)) + 1
        cups[curr] = cups[moved[-1]]
        cups[moved[-1]] = cups[destination]
        cups[destination] = moved[0]
        curr = cups[curr]
    print(cups[1] * cups[cups[1]])

if __name__ == '__main__':
    part1()
    part2()
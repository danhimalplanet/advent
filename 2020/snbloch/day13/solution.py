class buses:
    def __init__(self):
        with open('input.txt', 'r') as inputfile:
            self.departure = int(inputfile.readline().strip())
            self.routes = []
            for i in inputfile.readline().strip().split(','):
                if i != 'x':
                    self.routes.append(int(i))
                else:
                    self.routes.append(i)

def part1():
    simulation = buses()
    nearest_departure = (-1,-1)
    for i in simulation.routes:
        if i != 'x':
            departure_time = 0
            while departure_time < simulation.departure:
                departure_time += i
            if nearest_departure[0] == -1 or departure_time - simulation.departure < nearest_departure[1]:
                nearest_departure = (i, departure_time - simulation.departure)
    print(nearest_departure[0] * nearest_departure[1])

def part2_iterative():
    simulation = buses()
    timestamp = 0
    diffs = {}
    for i in simulation.routes:
        if i != 'x':
            if simulation.routes.index(i) == 0:
                incr = i
            diffs[i] = simulation.routes.index(i)
    found = False
    while found != True:
        count = 0
        for i in simulation.routes:
            if i != 'x':
                if (timestamp + diffs[i]) % i == 0:
                    count += 1
                else:
                    continue
        if count == len(diffs):
            print(timestamp)
            found = True
        else:
            timestamp += incr

def part2_math():
    simulation = buses()
    timestamp = 0
    step = 1
    for i in simulation.routes:
        if i != 'x':
            while (timestamp + simulation.routes.index(i)) % i != 0:
                timestamp += step
            step *= i
    print(timestamp)

if __name__ == '__main__':
    part1()
    part2_math()
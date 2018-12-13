def part1():
    initial_state = '.##.##...#.###..#.#..##..###..##...####.#...#.##....##.#.#...#...###.........##...###.....##.##.##'
    starting_position = 0
    transforms = {}
    with open('input.txt', 'r') as inputfile:
        for line in inputfile:
            line = line.strip().split(' => ')
            transforms[line[0]] = line[1]
    generation_count = 0
    while generation_count <  20:
        initial_state = '..' + initial_state + '..'
        starting_position -= 2
        counter = 2
        new_generation = '..'
        while counter < len(initial_state) - 2:
            if transforms.get(initial_state[counter - 2:counter + 3]) is not None:
                if transforms.get(initial_state[counter - 2:counter + 3]) == '#':
                    new_generation += '#'
                else:
                    new_generation += '.'
            else:
                new_generation += '.'
            counter += 1
        new_generation += '..'
        initial_state = new_generation
        generation_count += 1
    counter = 0
    sum = 0
    position = starting_position
    while counter < len(initial_state):
        if initial_state[counter] == '#':
            sum += position
        position += 1
        counter += 1
    print 'Part 1: Sum of all pots containing a plant is',sum

def part2():
    print 'Part 2: Sum after 50000000000 generations is',((50000000000 - 101) * 5) + 724

if __name__ == '__main__':
    part1()
    part2()

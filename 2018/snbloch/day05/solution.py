import io

def should_destroy(chars):
    if chars[0].upper() == chars[1].upper():
        if (chars[0].isupper() and chars[1].islower()) or (chars[0].islower() and chars[1].isupper()):
            return True
    return False

def part1():
    polymer = []
    with open('input.txt', 'r') as inputfile:
        for line in inputfile:
            line = line.strip()
            for i in line:
                polymer.append(i)
    print 'Initial polymer length:',len(polymer)
    iterations = 0
    position = 0
    finished = False
    change_detected = False
    while finished == False:
        if position >= len(polymer) - 1 and change_detected == False:
            finished = True
        elif position >= len(polymer) - 1 and change_detected == True:
            position = 0
            change_detected = False
            iterations += 1
            if iterations % 100 == 0:
                print 'Iteration',iterations,', Polymer length',len(polymer)
        elif should_destroy(polymer[position] + polymer[position + 1]) == True:
            polymer.__delitem__(position)
            polymer.__delitem__(position)
            change_detected = True
            position += 1
        else:
            position += 1
    print 'Part 1: Polymer has',len(polymer),'units remaining.'

def part2():
    polymer = []
    min_length = None
    with open('input.txt', 'r') as inputfile:
        for line in inputfile:
            line = line.strip()
            for i in line:
                polymer.append(i)
    for i in 'abcdefghijklmnopqrstuvwxyz':
        print 'Starting with all',i,'and',i.upper(),'chars removed'
        updated_polymer = polymer[:]
        sanitize_position = 0
        while sanitize_position < len(updated_polymer):
            if updated_polymer[sanitize_position] == i or updated_polymer[sanitize_position] == i.upper():
                updated_polymer.__delitem__(sanitize_position)
                continue
            sanitize_position += 1
        iterations = 0
        position = 0
        finished = False
        change_detected = False
        while finished == False:
            if position >= len(updated_polymer) - 1 and change_detected == False:
                finished = True
                if min_length is None:
                    min_length = len(updated_polymer)
                elif len(updated_polymer) < min_length:
                    min_length = len(updated_polymer)
                print 'Finished processing with all',i,'and',i.upper(),'chars removed'
                print 'Minimum length is now',min_length
            elif position >= len(updated_polymer) - 1 and change_detected == True:
                position = 0
                change_detected = False
                iterations += 1
                if iterations % 100 == 0:
                    print 'Iteration',iterations,', Polymer length',len(updated_polymer)
            elif should_destroy(updated_polymer[position] + updated_polymer[position + 1]) == True:
                updated_polymer.__delitem__(position)
                updated_polymer.__delitem__(position)
                change_detected = True
                position += 1
            else:
                position += 1
    print 'Part 2: Polymer minimum length is',min_length

if __name__ == '__main__':
    part1()
    part2()

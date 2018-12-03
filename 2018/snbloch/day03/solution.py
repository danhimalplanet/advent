import io
import numpy as np

def part1():
    grid = np.zeros((1000, 1000))
    with open('input.txt', 'r') as inputfile:
        for line in inputfile:
            splitline = line.strip().split(' ')
            start_x = int(splitline[2].split(',')[0])
            start_y = int(splitline[2].split(',')[1].replace(':', ''))
            width = int(splitline[3].split('x')[0])
            height = int(splitline[3].split('x')[1])
            cur_y = start_y
            while cur_y < start_y + height:
                cur_x = start_x
                while cur_x < start_x + width:
                    grid[cur_y][cur_x] += 1
                    cur_x += 1
                cur_y += 1
    multiple_claims = 0
    cur_y = 0
    while cur_y < 1000:
        cur_x = 0
        while cur_x < 1000:
            if grid[cur_y][cur_x] > 1:
                multiple_claims += 1
            cur_x += 1
        cur_y += 1
    print 'Part 1: ', multiple_claims, ' tiles have multiple claims'

def part2():
    grid = np.zeros((1000, 1000))
    with open('input.txt', 'r') as inputfile:
        for line in inputfile:
            splitline = line.strip().split(' ')
            start_x = int(splitline[2].split(',')[0])
            start_y = int(splitline[2].split(',')[1].replace(':', ''))
            width = int(splitline[3].split('x')[0])
            height = int(splitline[3].split('x')[1])
            cur_y = start_y
            while cur_y < start_y + height:
                cur_x = start_x
                while cur_x < start_x + width:
                    grid[cur_y][cur_x] += 1
                    cur_x += 1
                cur_y += 1
    with open('input.txt', 'r') as inputfile:
        for line in inputfile:
            splitline = line.strip().split(' ')
            start_x = int(splitline[2].split(',')[0])
            start_y = int(splitline[2].split(',')[1].replace(':', ''))
            width = int(splitline[3].split('x')[0])
            height = int(splitline[3].split('x')[1])
            line_id = int(splitline[0].replace('#', ''))
            cur_y = start_y
            is_intact = True
            while cur_y < start_y + height and is_intact is True:
                cur_x = start_x
                while cur_x < start_x + width:
                    if grid[cur_y][cur_x] > 1:
                        is_intact = False
                        break
                    cur_x += 1
                cur_y += 1
            if is_intact is True:
                print 'Part 2: Found intact square with id ', line_id
                return

if __name__ == '__main__':
    part1()
    part2()

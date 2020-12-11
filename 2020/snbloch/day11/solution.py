from itertools import product
from copy import deepcopy

class airplane:
    def __init__(self):
        self.seats = []
        self.changed = -1
        with open('input.txt', 'r') as inputfile:
            for line in inputfile:
                row = [i for i in line.strip()]
                self.seats.append(row)
        self.row_width = len(self.seats[0])
        self.num_rows = len(self.seats)
    def eval_adjacent_seats(self, x, y):
        if x == 0:
            adjacent_x = (x, x+1) 
        elif x == self.row_width - 1:
            adjacent_x = (x-1, x)
        else:
            adjacent_x = (x-1, x, x+1)
        if y == 0:
            adjacent_y = (y, y+1)
        elif y == self.num_rows - 1:
            adjacent_y = (y-1, y)
        else:
            adjacent_y = (y-1, y, y+1)
        adjacent = list(product(adjacent_x, adjacent_y))
        if self.current_seats[y][x] == 'L':
            occupied_count = 0
            for i in adjacent:
                if i == (x,y):
                    continue
                elif self.current_seats[i[1]][i[0]] == '#':
                    occupied_count += 1
            if occupied_count == 0:
                self.seats[y][x] = '#'
                self.changed += 1
        elif self.current_seats[y][x] == '#':
            occupied_count = 0
            for i in adjacent:
                if i == (x,y):
                    continue
                elif self.current_seats[i[1]][i[0]] == '#':
                    occupied_count += 1
            if occupied_count >= 4:
                self.seats[y][x] = 'L'
                self.changed += 1
    def eval_visible_seats(self, x, y):
        look_west = None
        look_east = None
        look_north = None
        look_south = None
        look_northwest = None
        look_northeast = None
        look_southwest = None
        look_southeast = None
        for visible_x in range(x - 1, -1, -1):
            if x == 0:
                break
            if self.current_seats[y][visible_x] != '.':
                if visible_x != x:
                    look_west = (visible_x, y)
                    break
        for visible_x in range(x + 1, self.row_width, 1):
            if x == self.row_width - 1:
                break
            if self.current_seats[y][visible_x] != '.':
                if visible_x != x:
                    look_east = (visible_x, y)
                    break
        for visible_y in range(y - 1, -1, -1):
            if y == 0:
                break
            if self.current_seats[visible_y][x] != '.':
                if visible_y != y:
                    look_north = (x, visible_y)
                    break
        for visible_y in range(y + 1, self.num_rows, 1):
            if y == self.num_rows - 1:
                break
            if self.current_seats[visible_y][x] != '.':
                if visible_y != y:
                    look_south = (x, visible_y)
                    break
        visible_x = x - 1
        for visible_y in range(y - 1, -1, -1):
            if visible_x < 0 or visible_y < 0:
                break
            if self.current_seats[visible_y][visible_x] != '.':
                look_northwest = (visible_x, visible_y)
                break
            visible_x -= 1
        visible_x = x + 1
        for visible_y in range(y - 1, -1, -1):
            if visible_x > self.row_width - 1 or visible_y < 0:
                break
            if self.current_seats[visible_y][visible_x] != '.':
                look_northeast = (visible_x, visible_y)
                break
            visible_x += 1
        visible_x = x - 1
        for visible_y in range(y + 1, self.num_rows, 1):
            if visible_x < 0 or visible_y == self.num_rows:
                break
            if self.current_seats[visible_y][visible_x] != '.':
                look_southwest = (visible_x, visible_y)
                break
            visible_x -= 1
        visible_x = x + 1
        for visible_y in range(y + 1, self.num_rows, 1):
            if visible_x > self.row_width - 1 or visible_y == self.num_rows:
                break
            if self.current_seats[visible_y][visible_x] != '.':
                look_southeast = (visible_x, visible_y)
                break
            visible_x += 1
        if self.current_seats[y][x] == 'L':
            occupied_count = 0
            for i in [look_west, look_east, look_north, look_south, look_northwest, look_northeast, look_southwest, look_southeast]:
                if i != None:
                    if self.current_seats[i[1]][i[0]] == 'L':
                        continue
                    elif self.current_seats[i[1]][i[0]] == '#':
                        occupied_count += 1
            if occupied_count == 0:
                self.seats[y][x] = '#'
                self.changed += 1
        elif self.current_seats[y][x] == '#':
            occupied_count = 0
            for i in [look_west, look_east, look_north, look_south, look_northwest, look_northeast, look_southwest, look_southeast]:
                if i != None:
                    if self.current_seats[i[1]][i[0]] == 'L':
                        continue
                    elif self.current_seats[i[1]][i[0]] == '#':
                        occupied_count += 1
            if occupied_count >= 5:
                self.seats[y][x] = 'L'
                self.changed += 1

def part1():
    flight = airplane()
    while flight.changed != 0:
        flight.current_seats = deepcopy(flight.seats)
        flight.changed = 0
        for y in range(flight.num_rows):
            for x in range(flight.row_width):
                flight.eval_adjacent_seats(x, y)
    total_occupied = 0
    for y in range(flight.num_rows):
        total_occupied += flight.seats[y].count('#')
    print(total_occupied)

def part2():
    flight = airplane()
    while flight.changed != 0:
        flight.current_seats = deepcopy(flight.seats)
        flight.changed = 0
        for y in range(flight.num_rows):
            for x in range(flight.row_width):
                flight.eval_visible_seats(x, y)
    total_occupied = 0
    for y in range(flight.num_rows):
        total_occupied += flight.seats[y].count('#')
    print(total_occupied)

if __name__ == '__main__':
    part1()
    part2()
            
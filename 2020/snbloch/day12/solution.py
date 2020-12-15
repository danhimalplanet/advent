class ferry:
    def __init__(self):
        self.direction = 'E'
        self.pos_x = 0
        self.pos_y = 0
        self.waypoint_x = 10
        self.waypoint_y = -1
        self.dirs = 'NESW'
        self.values = []
        with open('input.txt', 'r') as inputfile:
            for line in inputfile:
                direction = line[0]
                distance = int(line[1:])
                self.values.append((direction, distance))
    def rotate(self, rot_dir, degrees, is_waypoint):
        if is_waypoint == False:
            current_dir = self.dirs.index(self.direction)
            num_rotations = degrees * 4 / 360
            for _ in range(num_rotations):
                if rot_dir == 'L':
                    if current_dir - 1 < 0:
                        current_dir = len(self.dirs) - 1
                    else:
                        current_dir -= 1
                elif rot_dir == 'R':
                    if current_dir + 1 == len(self.dirs):
                        current_dir = 0
                    else:
                        current_dir += 1
            self.direction = self.dirs[current_dir]
        else:
            num_rotations = degrees * 4 / 360
            for _ in range(num_rotations):
                if rot_dir == 'L':
                    if self.waypoint_x > self.pos_x and self.waypoint_y <= self.pos_y:
                        diff_x = self.waypoint_x - self.pos_x
                        diff_y = self.pos_y - self.waypoint_y
                        self.waypoint_y = self.pos_y - diff_x
                        self.waypoint_x = self.pos_x - diff_y
                    elif self.waypoint_x > self.pos_x and self.waypoint_y > self.pos_y:
                        diff_x = self.waypoint_x - self.pos_x
                        diff_y = self.waypoint_y - self.pos_y
                        self.waypoint_y = self.pos_y - diff_x
                        self.waypoint_x = self.pos_x + diff_y
                    elif self.waypoint_x <= self.pos_x and self.waypoint_y > self.pos_y:
                        diff_x = self.pos_x - self.waypoint_x
                        diff_y = self.waypoint_y - self.pos_y
                        self.waypoint_y = self.pos_y + diff_x
                        self.waypoint_x = self.pos_x + diff_y
                    elif self.waypoint_x <= self.pos_x and self.waypoint_y <= self.pos_y:
                        diff_x = self.pos_x - self.waypoint_x
                        diff_y = self.pos_y - self.waypoint_y
                        self.waypoint_y = self.pos_y + diff_x
                        self.waypoint_x = self.pos_x - diff_y
                elif rot_dir == 'R':
                    if self.waypoint_x > self.pos_x and self.waypoint_y <= self.pos_y:
                        diff_x = self.waypoint_x - self.pos_x
                        diff_y = self.pos_y - self.waypoint_y
                        self.waypoint_y = self.pos_y + diff_x
                        self.waypoint_x = self.pos_x + diff_y
                    elif self.waypoint_x > self.pos_x and self.waypoint_y > self.pos_y:
                        diff_x = self.waypoint_x - self.pos_x
                        diff_y = self.waypoint_y - self.pos_y
                        self.waypoint_y = self.pos_y + diff_x
                        self.waypoint_x = self.pos_x - diff_y
                    elif self.waypoint_x <= self.pos_x and self.waypoint_y > self.pos_y:
                        diff_x = self.pos_x - self.waypoint_x
                        diff_y = self.waypoint_y - self.pos_y
                        self.waypoint_y = self.pos_y - diff_x
                        self.waypoint_x = self.pos_x - diff_y
                    elif self.waypoint_x <= self.pos_x and self.waypoint_y <= self.pos_y:
                        diff_x = self.pos_x - self.waypoint_x
                        diff_y = self.pos_y - self.waypoint_y
                        self.waypoint_y = self.pos_y - diff_x
                        self.waypoint_x = self.pos_x + diff_y

    def move(self, move_dir, move_dist, is_waypoint):
        if is_waypoint == False:
            if move_dir == 'F':
                if self.direction == 'N':
                    self.pos_y -= move_dist
                elif self.direction == 'E':
                    self.pos_x += move_dist
                elif self.direction == 'S':
                    self.pos_y += move_dist
                elif self.direction == 'W':
                    self.pos_x -= move_dist
            elif move_dir == 'N':
                self.pos_y -= move_dist
            elif move_dir == 'E':
                self.pos_x += move_dist
            elif move_dir == 'S':
                self.pos_y += move_dist
            elif move_dir == 'W':
                self.pos_x -= move_dist
        else:
            if move_dir == 'F':
                diff_x = self.waypoint_x - self.pos_x
                diff_y = self.waypoint_y - self.pos_y
                for _ in range(move_dist):
                    self.pos_x += diff_x
                    self.pos_y += diff_y
                self.waypoint_x = self.pos_x + diff_x
                self.waypoint_y = self.pos_y + diff_y
            elif move_dir == 'N':
                self.waypoint_y -= move_dist
            elif move_dir == 'E':
                self.waypoint_x += move_dist
            elif move_dir == 'S':
                self.waypoint_y += move_dist
            elif move_dir == 'W':
                self.waypoint_x -= move_dist
    def move_or_rot(self, direction, distance, is_waypoint):
        if direction in 'LR':
            self.rotate(direction, distance, is_waypoint)
        else:
            self.move(direction, distance, is_waypoint)

def part1():
    boat = ferry()
    for instruction in boat.values:
        boat.move_or_rot(instruction[0], instruction[1], False)
    print(abs(boat.pos_x) + abs(boat.pos_y))

def part2():
    boat = ferry()
    for instruction in boat.values:
        boat.move_or_rot(instruction[0], instruction[1], True)
    print(abs(boat.pos_x) + abs(boat.pos_y))

if __name__ == '__main__':
    part1()
    part2()
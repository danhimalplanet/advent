import math

class Moon:
    def __init__(self, x, y, z):
        self.pos_x = x
        self.pos_y = y
        self.pos_z = z
        self.vel_x = 0
        self.vel_y = 0
        self.vel_z = 0

def setup():
    moons = []
    with open('input.txt', 'r') as inputfile:
        for line in inputfile:
            line = line.strip().replace('<', '').replace('>', '')
            line = line.split(', ')
            for i in line:
                if 'x=' in i:
                    x = int(i.split('x=')[1])
                elif 'y=' in i:
                    y = int(i.split('y=')[1])
                elif 'z=' in i:
                    z = int(i.split('z=')[1])
            moons.append(Moon(x, y, z))
    return moons

def move(moons):
    compared = set()
    new_moons = moons[:]
    for m1 in moons:
        for m2 in moons:
            if m1 == m2 or (m1, m2) in compared or (m2, m1) in compared:
                continue
            else:
                if m1.pos_x > m2.pos_x:
                    new_moons[new_moons.index(m1)].vel_x -= 1
                    new_moons[new_moons.index(m2)].vel_x += 1
                elif m2.pos_x > m1.pos_x:
                    new_moons[new_moons.index(m1)].vel_x += 1
                    new_moons[new_moons.index(m2)].vel_x -= 1
                if m1.pos_y > m2.pos_y:
                    new_moons[new_moons.index(m1)].vel_y -= 1
                    new_moons[new_moons.index(m2)].vel_y += 1
                elif m2.pos_y > m1.pos_y:
                    new_moons[new_moons.index(m1)].vel_y += 1
                    new_moons[new_moons.index(m2)].vel_y -= 1
                if m1.pos_z > m2.pos_z:
                    new_moons[new_moons.index(m1)].vel_z -= 1
                    new_moons[new_moons.index(m2)].vel_z += 1
                elif m2.pos_z > m1.pos_z:
                    new_moons[new_moons.index(m1)].vel_z += 1
                    new_moons[new_moons.index(m2)].vel_z -= 1
                compared.add((m1, m2))
    for m1 in new_moons:
        new_moons[new_moons.index(m1)].pos_x += m1.vel_x
        new_moons[new_moons.index(m1)].pos_y += m1.vel_y
        new_moons[new_moons.index(m1)].pos_z += m1.vel_z
    return new_moons
    
def part1():
    moons = setup()
    for _ in range(1000):
        moons = move(moons)
    total = 0
    for m in moons:
        total += (abs(m.pos_x) + abs(m.pos_y) + abs(m.pos_z)) * (abs(m.vel_x) + abs(m.vel_y) + abs(m.vel_z))
    print(total)

def part2():
    moons = setup()
    original_state = moons[:]
    cycle = {}
    axes = ['x', 'y', 'z']
    x_seen = set()
    y_seen = set()
    z_seen = set()
    for i in range(3):
        moons = original_state[:]
        step_count = 1
        if axes[i] == 'x':
            x_seen.add(str([(m, m.pos_x, m.vel_x) for m in moons]))
        elif axes[i] == 'y':
            y_seen.add(str([(m, m.pos_y, m.vel_y) for m in moons]))
        elif axes[i] == 'z':
            z_seen.add(str([(m, m.pos_z, m.vel_z) for m in moons]))
        while True:
            moons = move(moons)
            if axes[i] == 'x':
                if str([(m, m.pos_x, m.vel_x) for m in moons]) in x_seen:
                    cycle[axes[i]] = step_count
                    break
                else:
                    x_seen.add(str([(m, m.pos_x, m.vel_x) for m in moons]))
            elif axes[i] == 'y':
                if str([(m, m.pos_y, m.vel_y) for m in moons]) in y_seen:
                    cycle[axes[i]] = step_count
                    break
                else:
                    y_seen.add(str([(m, m.pos_y, m.vel_y) for m in moons]))
            elif axes[i] == 'z':
                if str([(m, m.pos_z, m.vel_z) for m in moons]) in z_seen:
                    cycle[axes[i]] = step_count
                    break
                else:
                    z_seen.add(str([(m, m.pos_z, m.vel_z) for m in moons]))
            step_count += 1
    print(math.lcm(cycle['x'], cycle['y'], cycle['z']))

if __name__ == '__main__':
    part1()
    part2()
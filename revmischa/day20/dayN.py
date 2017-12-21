import os
import sys
PWD = os.path.abspath(os.path.join(os.path.dirname(__file__)))
PROJ_ROOT = os.path.abspath(os.path.join(PWD, '..', '..'))
if PROJ_ROOT not in sys.path:
    sys.path.insert(0, PROJ_ROOT)

from revmischa import Computer, main
from pprint import pprint
from typing import Tuple, List

# array indexes
X = 0
Y = 1
Z = 2


class Particle:
    def __init__(self, id_, pos, vel, acc):
        self.id_ = id_
        self.pos = pos
        self.vel = vel
        self.acc = acc

    def __repr__(self):
        return f"p=<{self.pos}>, v=<{self.vel}>, a=<{self.acc}>"

    def update(self):
        self.vel[X] += self.acc[X]
        self.vel[Y] += self.acc[Y]
        self.vel[Z] += self.acc[Z]
        self.pos[X] += self.vel[X]
        self.pos[Y] += self.vel[Y]
        self.pos[Z] += self.vel[Z]

    def distance(self):
        return abs(self.pos[X]) + abs(self.pos[Y]) + abs(self.pos[Z])

class DayN(Computer):
    pwd = PWD

    def __init__(self, structure):
        """Construct solver with puzzle input."""
        super().__init__(structure)
        self.diverging_bound = 1000000000
        self.plist: List[Particle] = structure

    @classmethod
    def parse_vec(cls, vec: str) -> List[int]:
        # p=< 3,0,0>
        _, inner = vec.split('<')
        inner, _ = inner.split('>')
        #print(f"parsed {vec} to {inner}")
        x, y, z = inner.split(',')
        #print(f"x: {x}  y {y}  z{z}")
        return [int(x), int(y), int(z)]
                 

    @classmethod
    def parse_input(cls, input_str: str):
        plist: List[Particle] = list()
        id_ = 0
        for line in input_str.split('\n'):
            p, v, a = line.split(', ')
            pos = cls.parse_vec(p)
            vel = cls.parse_vec(v)
            acc = cls.parse_vec(a)
            particle = Particle(id_, pos, vel, acc)
            plist.append(particle)
            id_ += 1
        return plist
        

    def run_part1(self):
        i = 0
        plist = self.plist
        for i in range(self.diverging_bound):
        # while len(plist) > self.diverging_bound:
            # order particles by distance
            distance_ordered = []
            to_remove = []  # part 1
            for p in plist:
                p.update()

                # part I
                # cull particles we believe are diverging
                # dist = p.distance()
                # if dist > self.diverging_bound:
                    # to_remove.append(p)
                    # continue

            distance_ordered = sorted(plist, key=lambda p: p.distance())
            # search for collisions
            p_last = None
            collided = 0
            for p in distance_ordered:
                if p_last:
                    if p_last and p_last.pos[X] == p.pos[X] and p_last.pos[Y] == p.pos[Y] and p_last.pos[Z] == p.pos[Z]:  # collision
                        collided += 1
                        to_remove.append(p_last)
                        to_remove.append(p)
                p_last = p

            # remove culled
            [plist.remove(p) for p in to_remove if p in plist]
            if collided:
                print(f"{collided} collided - {len(plist)} remaining")
            i += 1
            self.diverging_bound -= 1

            if self.diverging_bound < 1:
                # failed
                print(f"Failed, diverging bound went to zero after {i} iterations")

        # part I
        # if len(plist) > 1:
            # print(f"Failed, {len(self.plist)} > 1")
        return len(plist)
        # return self.plist[0].id_

    def run_part2(self):
        return 0

if __name__ == '__main__':
    main(DayN)

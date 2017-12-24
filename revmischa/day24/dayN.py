import os
import sys
PWD = os.path.abspath(os.path.join(os.path.dirname(__file__)))
PROJ_ROOT = os.path.abspath(os.path.join(PWD, '..', '..'))
if PROJ_ROOT not in sys.path:
    sys.path.insert(0, PROJ_ROOT)

from revmischa import Computer, main
from pprint import pprint
from typing import List, Dict, Tuple

Port = Tuple[int, int]  # 2-ple of port strengths
PortList = List[Port]

LEFT = 0
RIGHT = 1

class DayN(Computer):
    pwd = PWD

    def __init__(self, structure, **kwargs):
        """Construct solver with puzzle input."""
        super().__init__(structure, **kwargs)
        self.ports: PortList = structure
        self.best = 0

    @classmethod
    def parse_input(cls, input_str: str) -> PortList:
        pl: PortList = list()
        for line in input_str.split('\n'):
            parts = line.split('/')
            left = int(parts[LEFT])
            right = int(parts[RIGHT])
            pl.append((left, right))
        return pl

    def run_part1(self):
        self.find_best(self.ports)
        return self.best

    def find_best(self, ports: PortList):
        def search(cur_bridge: PortList, available: PortList):
            self.update_best(cur_bridge)
            for i in range(len(available)):
                port = available[i][:]
                # can we use this port?
                last_bridge_port_strength: int = 0
                if cur_bridge:
                    last_bridge_port: Port = cur_bridge[-1]  # last bridge port
                    last_bridge_port_strength = last_bridge_port[RIGHT]  # right side
                    # currently testing this port to see if it fits
                    if last_bridge_port_strength not in port:
                        # can't connect it
                        continue
                else:
                    # first port must be type 0
                    if last_bridge_port_strength not in port:
                        continue

                # (flip if needed)
                if port[LEFT] != last_bridge_port_strength and port[RIGHT] == last_bridge_port_strength:
                    # flip
                    port = (port[RIGHT], port[LEFT])

                # remove this available from list and stick it on cur_bridge
                new_avail: PortList = available[:]
                del new_avail[i]
                # append to new current
                new_cur: PortList = cur_bridge[:]
                new_cur.append(port)
                # check current strength
                # pprint(new_cur)
                search(new_cur, new_avail)
        search([], self.ports)

    def update_best(self, ports: PortList):
        sum_ = 0
        for port in ports:
            sum_ += sum(port)
        if sum_ > self.best:
            self.best = sum_
            print(f"New best for {ports}: {sum_}")

    def run_part2(self):
        return 0


if __name__ == '__main__':
    print(DayN.part1_result(debug=True))
    print(DayN.part2_result(debug=False))

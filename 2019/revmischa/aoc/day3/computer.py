import os
import sys
from typing import List


PWD = os.path.abspath(os.path.join(os.path.dirname(__file__)))
PROJ_ROOT = os.path.abspath(os.path.join(PWD, "..", ".."))
if PROJ_ROOT not in sys.path:
    sys.path.insert(0, PROJ_ROOT)

from aoc.computer import Computer
from pprint import pprint  # noqa: F401
from shapely.geometry import Point, LineString
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from geoalchemy2 import Geometry, func
from geoalchemy2.shape import to_shape
from sqlalchemy import Column, Integer
from sqlalchemy.orm import sessionmaker


engine = create_engine("postgresql:///aoc", echo=False)
conn = engine.connect()
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()


class Wire(Base):
    __tablename__ = "wire"
    id = Column(Integer, primary_key=True)
    geom = Column(Geometry("LINESTRING"))


Wire.__table__.drop(engine)
Wire.__table__.create(engine)

def prg(geom):
    print(session.scalar(func.ST_AsText(geom)))

class Day3(Computer):
    pwd: str = PWD

    def __init__(self, structure, **kwargs):
        """Construct solver with puzzle input."""
        super().__init__(structure, **kwargs)
        self.w1: List[str] = structure[0]
        self.w2: List[str] = structure[1]

    @classmethod
    def parse_input(cls, input_str: str):
        (w1s, w2s) = input_str.split("\n")
        return w1s.split(","), w2s.split(",")

    def run_part1(self):
        w1 = self.make_geom(self.w1)
        w2 = self.make_geom(self.w2)
        prg(w1.geom)
        prg(w2.geom)
        intersection = session.scalar((w1.geom.ST_Intersection(w2.geom)))
        intshape = to_shape(intersection)
        prg(intersection)
        min_dist = 1000000000
        for point in intshape:
            print(point)
            dist = self.manhattan_dist(point.x, point.y)
            if dist < min_dist:
                min_dist = dist
        print(min_dist)
        return min_dist


    def make_geom(self, ws: List[str]):
        x = 0
        y = 0
        points = []
        for wd in ws:
            # get coords of next wire segment
            direction, magnitude = wd[0], int(wd[1:])
            if direction == "U":
                y += magnitude
            elif direction == "D":
                y -= magnitude
            elif direction == "R":
                x += magnitude
            elif direction == "L":
                x -= magnitude
            points.append(Point(x, y))

        geom = LineString(points)
        wire = Wire(geom=str(geom))
        session.add(wire)
        session.commit()
        return wire

    def manhattan_dist(self, x: int, y: int):
        # distance from origin
        return abs(x) + abs(y)

    def run_part2(self):
        return 0


if __name__ == "__main__":
    print(Day3.part1_result(debug=False))
    print(Day3.part2_result(debug=False))

#!/usr/bin/env python3

import sys

steps=int(sys.argv[1])

f = open("maze.txt", "r")

class Diagram(object):
    def __init__(self, rows):
        self.rows = rows

    def __str__(self):
        print("Num of rows in diagram:", len(rows))
        print("Len of row  in diagram:", len(rows[0]))
        rev = []
        for row in self.rows:
            rev.insert(0, row)
        return '\n'.join([' '.join(row) for row in rev])

    def val(self, x, y):
        val = self.rows[y][x]
        return val

    def height(self):
        return len(self.rows)

    def width(self):
        width = 0
        for row in self.rows:
            if len(row) > width:
                width = len(row)
        return width

    def row(self, x):
        return self.rows[x]
    
    def col(self, y):
        val = []
        for row in self.rows:
            val.insert(0, (row[y]))
        return '\n'.join([' '.join(char) for char in val])

    def cardinal(self, x, y):
        cardinal = {}
        height = self.height()
        width = self.width()
        if y-1>= 0:
            try:
                if not self.val(x,y-1).isspace():
                    cardinal['south'] = (x,y-1)
            except IndexError:
                pass
        if x-1>=0:
            try:
                if not self.val(x-1,y).isspace():
                    cardinal['west'] = (x-1,y)
            except IndexError:
                pass
        if y+1 <= height - 1:
            try:
                if not self.val(x,y+1).isspace():
                    cardinal['north'] = (x,y+1)
            except IndexError:
                pass
        if x+1<= width -1:
            try:
                if not self.val(x+1,y).isspace():
                    cardinal['east'] = (x+1,y)
            except IndexError:
                pass
        return cardinal

rows = []

for _ in f:
    row = [ char for char in str(_.strip("\n")) ]
    rows.insert(0, row)

#    if len(row) != 0:
#        rows.insert(0, row)

d = Diagram(rows)

starting_cell=(1,200)

def move(diagram, x, y, prev_x, prev_y):
    next_x = None
    next_y = None
    start = False
    letter = False
    next_direction = None
    prev_direction = None
    opposites = { 'north': 'south', 'west': 'east', 'south': 'north', 'east': 'west' }

    if diagram.val(x,y) in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        letter = True

    height = diagram.height()
    width = diagram.width()

    if x == 1 and y == 200:
        start = True

    if start:
        if len(diagram.cardinal(x,y).keys()) == 1:
            next_x = x
            next_y = y - 1
            cardinal = diagram.cardinal(x,y)
            for k,v in cardinal.items():
                next_direction = k

    if not start:
        val = diagram.val(x,y)
        cardinal = diagram.cardinal(x,y)
        print(cardinal)

        if prev_x == None:
            print("prev_x is unknown")
        if prev_x == None:
            print("prev_y is unknown")
        if prev_x != None and prev_y != None:
            prev = (prev_x, prev_y)
            print("prev: ", prev)
            for k, v in cardinal.items():
                if v == prev:
                    prev_direction = k
            print("prev_direction: ", prev_direction)

        if prev != None:
            if len(cardinal) == 1:
                print("FINISHED")
            if len(cardinal) == 4:
                opposite=opposites[prev_direction]
                next_direction = opposite
                next = cardinal[next_direction]
                next_direction = opposite
                next_x = next[0]
                next_y = next[1]
            elif val == "|" or val == "-":
                for k,v in cardinal.items():
                    if v == prev:
                        opposite = opposites[k]
                next = cardinal[opposite]
                next_direction = opposite       
                next_x = next[0]
                next_y = next[1]
            else:
                next_direction = ""
                naughty = []
                for k,v in cardinal.items():
                    print(k, v)
                    if v == prev:
                        naughty.append(k)
                for n in naughty:
                    cardinal.pop(n, 0)
                for k, v in cardinal.items():
                    next = v
                    next_direction = k
                    next_x = next[0]
                    next_y = next[1]

    if x == None:
        print("x is unknown")
    if y == None:
        print("y is unknown")
    if x != None and y != None:
        print("current: ", diagram.val(x,y), x, y)
        print("cardinal:", diagram.cardinal(x,y))

    if next_x == None:
        print("next_x is unknown")
    if next_y == None:
        print("next_y is unknown")
    if next_x != None and next_y != None:
        print("next: ", diagram.val(next_x, next_y), next_x, next_y)
        print("next_direction: ", next_direction)
    print("--------")

    return (next_x, next_y)

def run_simulation(moves):
  cell = ()
  j = 0
  letter_path = ""
  while j < moves:
    if cell == ():
      cell = starting_cell
      prev_x = None
      prev_y = None 
    x = cell[0]
    y = cell[1]
    next_cell = move(d, x, y, prev_x, prev_y)
    prev_x = x
    prev_y = y
    if d.val(x,y) in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        letter_path = letter_path + d.val(x,y)
    print("LETTER_PATH", letter_path)
    cell = next_cell
    j = j + 1

run_simulation(steps)

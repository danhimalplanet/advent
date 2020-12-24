class tile:
    def __init__(self):
        self.color = 'white'

class floor:
    def __init__(self):
        self.tiles = {}
        for x in range(300):
            for y in range(300):
                t = tile()
                t.color = 'white'
                self.tiles[(x,y)] = t
        with open('input.txt', 'r') as filename:
            for line in filename:
                self.move(line.strip())
    def move(self, dirs):
        pos = 0
        x, y = 150, 150
        while pos < len(dirs):
            if dirs[pos] in ['n', 's']:
                d = dirs[pos:pos+2]
            else:
                d = dirs[pos]
            if d == 'ne':
                x += 1
                y += 1
            elif d == 'nw':
                x -= 1
                y += 1
            elif d == 'se':
                x += 1
                y -= 1
            elif d == 'sw':
                x -= 1
                y -= 1
            elif d == 'w':
                x -= 2
            elif d == 'e':
                x += 2
            pos += len(d)
        if self.tiles[(x,y)].color == 'white':
            self.tiles[(x,y)].color = 'black'
        else:
            self.tiles[(x,y)].color = 'white'

def part1():
    lobby = floor()
    total = 0
    for t in lobby.tiles:
        if lobby.tiles[t].color == 'black':
            total += 1
    print(total)

def part2():
    lobby = floor()
    for _ in range(100):
        for t1 in lobby.tiles:
            adj_black = 0
            for move in [(1, 1), (1, -1), (-1, 1), (-1, -1), (2, 0), (-2, 0)]:
                x,y = t1[0] + move[0], t1[1] + move[1]
                if (x,y) not in lobby.tiles:
                    continue
                if lobby.tiles[(x,y)].color == 'black' or lobby.tiles[(x,y)].color == 'black_flipping_white':
                    adj_black += 1
            if lobby.tiles[t1].color == 'black' and (adj_black == 0 or adj_black > 2):
                lobby.tiles[t1].color = 'black_flipping_white'
            elif lobby.tiles[t1].color == 'white' and adj_black == 2:
                lobby.tiles[t1].color = 'white_flipping_black'
        for t1 in lobby.tiles:
            if lobby.tiles[t1].color == 'white_flipping_black':
                lobby.tiles[t1].color = 'black'
            elif lobby.tiles[t1].color == 'black_flipping_white':
                lobby.tiles[t1].color = 'white'
    total = 0
    for t in lobby.tiles:
        if lobby.tiles[t].color == 'black':
            total += 1
    print(total)

if __name__ == '__main__':
    part1()
    part2()
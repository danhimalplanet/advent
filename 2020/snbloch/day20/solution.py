import math
from collections import defaultdict

class tile:
    def __init__(self):
        self.id = None
        self.edges = {}
        self.tile_grid = None

def rotate(grid):
    return [''.join(row) for row in zip(*reversed(grid))]

def flip_vertical(grid):
    return grid[::-1]

def flip_horizontal(grid):
    for row in grid:
        grid[grid.index(row)] = ''.join(list(reversed(row)))
    return grid

def find_edge(game_tiles, layout, x, y, corners, edges, inside, found):
    rotation_directions = ['north','east','south','west']
    to_search = corners + edges
    if layout[y - 1][x] and y > 0:
        tile_id = layout[y - 1][x]
        match_edge = game_tiles[layout[y - 1][x]].edges['south']
    elif layout[y][x - 1] and x > 0:
        tile_id = layout[y][x - 1]
        match_edge = game_tiles[layout[y][x - 1]].edges['east']
    elif layout[y + 1][x] and y < len(layout):
        tile_id = layout[y + 1][x]
        match_edge = game_tiles[layout[y + 1][x]].edges['north']
    elif layout[y][x + 1] and x < len(layout[y]):
        tile_id = layout[y][x + 1]
        match_edge = game_tiles[layout[y][x + 1]].edges['west']
    for t1 in to_search:
        if t1 == tile_id or t1 in found:
            continue
        else:
            if match_edge in game_tiles[t1].edges.values() or match_edge[::-1] in game_tiles[t1].edges.values():
                found.add(t1)
                for edge in game_tiles[tile_id].edges:
                    if game_tiles[tile_id].edges[edge] == match_edge or game_tiles[tile_id].edges[edge] == match_edge[::-1]:
                        direction = edge
                desired = rotation_directions[(rotation_directions.index(direction) + 2) % len(rotation_directions)]
                while game_tiles[t1].edges[desired] != match_edge:
                    if game_tiles[t1].edges[desired] == match_edge[::-1]:
                        if desired == 'north' or desired == 'south':
                            game_tiles[t1].tile_grid = flip_horizontal(game_tiles[t1].tile_grid)
                        elif desired == 'east' or desired == 'west':
                            game_tiles[t1].tile_grid = flip_vertical(game_tiles[t1].tile_grid)
                    else:
                        game_tiles[t1].tile_grid = rotate(game_tiles[t1].tile_grid)
                    game_tiles[t1].edges['north'] = game_tiles[t1].tile_grid[0]
                    game_tiles[t1].edges['south'] = game_tiles[t1].tile_grid[len(game_tiles[t1].tile_grid) - 1]
                    game_tiles[t1].edges['west'] = ''.join([row[0] for row in game_tiles[t1].tile_grid])
                    game_tiles[t1].edges['east'] = ''.join([row[len(row) - 1] for row in game_tiles[t1].tile_grid])
                return game_tiles, t1, found

def find_inside(game_tiles, layout, x, y, corners, edges, inside, found):
    rotation_directions = ['north','east','south','west']
    to_search = inside
    look_north = layout[y - 1][x]
    look_west = layout[y][x - 1]
    
    for t1 in to_search:
        if t1 == look_north or t1 == look_west or t1 in found:
            continue
        else:
            for n in game_tiles[look_north].edges.values():
                for w in game_tiles[look_west].edges.values():
                    if (n in game_tiles[t1].edges.values() or n[::-1] in game_tiles[t1].edges.values()) and (w in game_tiles[t1].edges.values() or w[::-1] in game_tiles[t1].edges.values()):
                        found.add(t1)
                        for edge in game_tiles[look_west].edges:
                            if game_tiles[look_west].edges[edge] == w or game_tiles[look_west].edges[edge] == w[::-1]:
                                direction = edge
                        desired = rotation_directions[(rotation_directions.index(direction) + 2) % len(rotation_directions)]
                        while game_tiles[t1].edges[desired] != w:
                            if game_tiles[t1].edges[desired] == w[::-1]:
                                if desired == 'north' or desired == 'south':
                                    game_tiles[t1].tile_grid = flip_horizontal(game_tiles[t1].tile_grid)
                                elif desired == 'east' or desired == 'west':
                                    game_tiles[t1].tile_grid = flip_vertical(game_tiles[t1].tile_grid)
                            else:
                                game_tiles[t1].tile_grid = rotate(game_tiles[t1].tile_grid)
                            game_tiles[t1].edges['north'] = game_tiles[t1].tile_grid[0]
                            game_tiles[t1].edges['south'] = game_tiles[t1].tile_grid[len(game_tiles[t1].tile_grid) - 1]
                            game_tiles[t1].edges['west'] = ''.join([row[0] for row in game_tiles[t1].tile_grid])
                            game_tiles[t1].edges['east'] = ''.join([row[len(row) - 1] for row in game_tiles[t1].tile_grid])
                        return game_tiles, t1, found
    return game_tiles, None, found


def part1():
    game_tiles = {}
    tile_count = defaultdict(int)
    corners = []
    edges = []
    inside = []

    with open('input.txt', 'r') as inputfile:
        tiles = inputfile.read().split('\n\n')
        for t in tiles:
            curr_tile = tile()
            id = int(t.split(':')[0].split('Tile ')[1])
            tile_grid = []
            for line in t.split(':')[1].strip().split('\n'):
                tile_grid.append(line)
            curr_tile.tile_grid = tile_grid
            curr_tile.edges['north'] = tile_grid[0]
            curr_tile.edges['south'] = tile_grid[len(tile_grid) - 1]
            curr_tile.edges['west'] = ''.join([row[0] for row in tile_grid])
            curr_tile.edges['east'] = ''.join([row[len(row) - 1] for row in tile_grid])
            game_tiles[id] = curr_tile

    for t1 in game_tiles:
        for t2 in game_tiles:
            if t1 == t2:
                continue
            else:
                for e in game_tiles[t1].edges.values():
                    if e in game_tiles[t2].edges.values() or e[::-1] in game_tiles[t2].edges.values():
                        tile_count[t1] += 1
    for t in tile_count:
        if tile_count[t] == 2:
            corners.append(t)
        elif tile_count[t] == 3:
            edges.append(t)
        elif tile_count[t] == 4:
            inside.append(t)
    total = 1
    for i in corners:
        total *= i
    print(total)

def part2():
    game_tiles = {}
    tile_count = defaultdict(int)
    corners = []
    edges = []
    inside = []
    found = set()

    with open('input.txt', 'r') as inputfile:
        tiles = inputfile.read().split('\n\n')
        for t in tiles:
            curr_tile = tile()
            id = int(t.split(':')[0].split('Tile ')[1])
            tile_grid = []
            for line in t.split(':')[1].strip().split('\n'):
                tile_grid.append(line)
            curr_tile.tile_grid = tile_grid
            curr_tile.edges['north'] = tile_grid[0]
            curr_tile.edges['south'] = tile_grid[len(tile_grid) - 1]
            curr_tile.edges['west'] = ''.join([row[0] for row in tile_grid])
            curr_tile.edges['east'] = ''.join([row[len(row) - 1] for row in tile_grid])
            game_tiles[id] = curr_tile
    
    for t1 in game_tiles:
        for t2 in game_tiles:
            if t1 == t2:
                continue
            else:
                for e in game_tiles[t1].edges.values():
                    if e in game_tiles[t2].edges.values() or e[::-1] in game_tiles[t2].edges.values():
                        tile_count[t1] += 1
    for t in tile_count:
        if tile_count[t] == 2:
            corners.append(t)
        elif tile_count[t] == 3:
            edges.append(t)
        elif tile_count[t] == 4:
            inside.append(t)

    layout = []
    width = int(math.sqrt(len(game_tiles)))
    length = width
    for y in range(length):
        row = []
        for x in range(width):
            row.append(None)
        layout.append(row)

    while len(found) == 0:
        for i in corners:
            found_n = False
            found_w = False
            edge_n = game_tiles[i].edges['north']
            edge_w = game_tiles[i].edges['west']
            for t1 in edges:
                if edge_n in game_tiles[t1].edges.values() or edge_n[::-1] in game_tiles[t1].edges.values():
                    found_n = True
                if edge_w in game_tiles[t1].edges.values() or edge_w[::-1] in game_tiles[t1].edges.values():
                    found_w = True
            if found_n == False and found_w == False:
                layout[0][0] = i
                found.add(i)
            else:
                game_tiles[i].tile_grid = rotate(game_tiles[i].tile_grid)
                game_tiles[i].edges['north'] = game_tiles[i].tile_grid[0]
                game_tiles[i].edges['south'] = game_tiles[i].tile_grid[len(game_tiles[i].tile_grid) - 1]
                game_tiles[i].edges['west'] = ''.join([row[0] for row in game_tiles[i].tile_grid])
                game_tiles[i].edges['east'] = ''.join([row[len(row) - 1] for row in game_tiles[i].tile_grid])
    
    #find edges first
    #travel south along the west edge:
    y = 1
    x = 0
    while y < len(layout):
        game_tiles, t1, found = find_edge(game_tiles, layout, x, y, corners, edges, inside, found)
        layout[y][x] = t1
        y += 1
    #next travel east along the south edge:
    y = len(layout) - 1
    x = 1
    while x < len(layout[y]):
        game_tiles, t1, found = find_edge(game_tiles, layout, x, y, corners, edges, inside, found)
        layout[y][x] = t1
        x += 1
    #next travel north along the east edge:
    y = len(layout) - 2
    x = len(layout[y]) - 1
    while y >= 0:
        game_tiles, t1, found = find_edge(game_tiles, layout, x, y, corners, edges, inside, found)
        layout[y][x] = t1
        y -= 1
    #finally travel west along the north edge:
    y = 0
    x = len(layout[y]) - 2
    while x > 0:
        game_tiles, t1, found = find_edge(game_tiles, layout, x, y, corners, edges, inside, found)
        layout[y][x] = t1
        x -= 1
    #now fill in the rest of the inside
    y = 1
    while y < len(layout) - 1:
        x = 1
        while x < len(layout[y]) - 1:
            if layout[y][x]:
                continue
            else:
                game_tiles, t1, found = find_inside(game_tiles, layout, x, y, corners, edges, inside, found)
                layout[y][x] = t1
            x += 1
        y += 1

    big_picture = []
    for x in range(len(layout[0])):
        row_count = 0
        if len(big_picture) == 0:
            for y in range(len(layout[x])):
                for line in game_tiles[layout[y][x]].tile_grid[1:-1]:
                    big_picture.append(''.join(line[1:-1]))
                    row_count += 1
        else:
            for y in range(len(layout[y])):
                for line in game_tiles[layout[y][x]].tile_grid[1:-1]:
                    big_picture[row_count] += ''.join(line[1:-1])
                    row_count += 1
    
    sea_monster = [(18,0),(0,1),(5,1),(6,1),(11,1),(12,1),(17,1),(18,1),(19,1),(1,2),(4,2),(7,2),(10,2),(13,2),(16,2)]
 
    sea_monster_count = 0
    while sea_monster_count == 0:
        for y in range(len(big_picture) - 2):
            for x in range(len(big_picture[y]) - 19):
                points = 0
                for point in sea_monster:
                    if big_picture[y + point[1]][x + point[0]] == '#':
                        points += 1
                if points == len(sea_monster):
                    sea_monster_count += 1
                    for point in sea_monster:
                        big_picture[y + point[1]] = big_picture[y + point[1]][:x + point[0]] + '.' + big_picture[y + point[1]][x + point[0] + 1:]
        if sea_monster_count == 0:
            big_picture = flip_horizontal(big_picture)
            big_picture = flip_vertical(big_picture)
            big_picture = rotate(big_picture)
        else:
            roughness = 0
            for y in range(len(big_picture)):
                for x in range(len(big_picture[y])):
                    if big_picture[y][x] == '#':
                        roughness += 1
            print(roughness)
    

if __name__ == '__main__':
    part1()
    part2()
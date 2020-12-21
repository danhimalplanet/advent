from collections import defaultdict

game_tiles = {}
tile_count = defaultdict(int)
edge_count = defaultdict(int)

class tile:
    def __init__(self):
        self.id = None
        self.edges = {}
        self.tile_grid = None

with open('test.txt', 'r') as inputfile:
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

def rotate(grid):
    return [''.join(row) for row in zip(*reversed(grid))]

def flip_vertical(grid):
    return grid[::-1]

def flip_horizontal(grid):
    for row in grid:
        grid[grid.index(row)] = ''.join(list(reversed(row)))
    return grid

def find_neighbor(tile_id, edge, direction):
    global game_tiles
    rotation_directions = ['north','east','south','west']
    for t1 in game_tiles:
        if t1 == tile_id:
            continue
        else:
            for k, v in game_tiles[t1].edges.items():
                if v == edge:
                    #print('found match in tile:')
                    #for row in game_tiles[t1].tile_grid:
                    #    print(row)
                    #print
                    if k == direction:
                        #print('found: ', direction, t1)                        
                        return t1
                    else:
                        desired_dir_index = rotation_directions.index(direction)
                        curr_dir_index = rotation_directions.index(k)
                        while curr_dir_index != desired_dir_index:
                            #print('rotating')
                            #print('grid before rotate:')
                            #for row in game_tiles[t1].tile_grid:
                            #    print(row)
                            #print
                            game_tiles[t1].tile_grid = rotate(game_tiles[t1].tile_grid)
                            #print('grid after rotate:')
                            #for row in game_tiles[t1].tile_grid:
                            #    print(row)
                            #print
                            game_tiles[t1].edges['north'] = game_tiles[t1].tile_grid[0]
                            game_tiles[t1].edges['south'] = game_tiles[t1].tile_grid[len(tile_grid) - 1]
                            game_tiles[t1].edges['west'] = ''.join([row[0] for row in game_tiles[t1].tile_grid])
                            game_tiles[t1].edges['east'] = ''.join([row[len(row) - 1] for row in game_tiles[t1].tile_grid])
                            if curr_dir_index == len(rotation_directions) - 1:
                                curr_dir_index = 0
                            else:
                                curr_dir_index += 1
                        #print('found: ', direction, t1)
                        return t1
                elif v == edge[::-1]:
                    #print('found match in tile:')
                    #for row in game_tiles[t1].tile_grid:
                    #    print(row)
                    #print
                    #print('found: ', direction, t1)
                    if k == direction:
                        if k == 'north' or k == 'south':
                            #print('flipping horizontal')
                            #print('grid before flip:')
                            #for row in game_tiles[t1].tile_grid:
                            #    print(row)
                            #print
                            game_tiles[t1].tile_grid = flip_horizontal(game_tiles[t1].tile_grid)
                            #print('grid after flip:')
                            #for row in game_tiles[t1].tile_grid:
                            #    print(row)
                            #print
                            game_tiles[t1].edges['north'] = game_tiles[t1].tile_grid[0]
                            game_tiles[t1].edges['south'] = game_tiles[t1].tile_grid[len(tile_grid) - 1]
                            game_tiles[t1].edges['west'] = ''.join([row[0] for row in game_tiles[t1].tile_grid])
                            game_tiles[t1].edges['east'] = ''.join([row[len(row) - 1] for row in game_tiles[t1].tile_grid])
                        elif k == 'east' or k == 'west':
                            #print('flipping vertical')
                            #print('grid before flip:')
                            #for row in game_tiles[t1].tile_grid:
                            #    print(row)
                            #print
                            game_tiles[t1].tile_grid = flip_vertical(game_tiles[t1].tile_grid)
                            #print('grid after flip:')
                            #for row in game_tiles[t1].tile_grid:
                            #    print(row)
                            #print
                            game_tiles[t1].edges['north'] = game_tiles[t1].tile_grid[0]
                            game_tiles[t1].edges['south'] = game_tiles[t1].tile_grid[len(tile_grid) - 1]
                            game_tiles[t1].edges['west'] = ''.join([row[0] for row in game_tiles[t1].tile_grid])
                            game_tiles[t1].edges['east'] = ''.join([row[len(row) - 1] for row in game_tiles[t1].tile_grid])
                        return t1
                    else:
                        desired_dir_index = rotation_directions.index(direction)
                        curr_dir_index = rotation_directions.index(k)
                        while curr_dir_index != desired_dir_index:
                            #print('rotating')
                            #print('grid before rotate:')
                            #for row in game_tiles[t1].tile_grid:
                            #    print(row)
                            #print
                            game_tiles[t1].tile_grid = rotate(game_tiles[t1].tile_grid)
                            #print('grid after rotate:')
                            #for row in game_tiles[t1].tile_grid:
                            #    print(row)
                            #print
                            game_tiles[t1].edges['north'] = game_tiles[t1].tile_grid[0]
                            game_tiles[t1].edges['south'] = game_tiles[t1].tile_grid[len(tile_grid) - 1]
                            game_tiles[t1].edges['west'] = ''.join([row[0] for row in game_tiles[t1].tile_grid])
                            game_tiles[t1].edges['east'] = ''.join([row[len(row) - 1] for row in game_tiles[t1].tile_grid])
                            if curr_dir_index == len(rotation_directions) - 1:
                                curr_dir_index = 0
                            else:
                                curr_dir_index += 1
                        if game_tiles[t1].edges[direction] == edge:
                            #print('found: ', direction, t1)
                            return t1
                        else:
                            if k == 'north' or k == 'south':
                                #print('flipping horizontal')
                                #print('grid before flip:')
                                #for row in game_tiles[t1].tile_grid:
                                #    print(row)
                                #print
                                game_tiles[t1].tile_grid = flip_horizontal(game_tiles[t1].tile_grid)
                                #print('grid after flip:')
                                #for row in game_tiles[t1].tile_grid:
                                #    print(row)
                                #print
                                game_tiles[t1].edges['north'] = game_tiles[t1].tile_grid[0]
                                game_tiles[t1].edges['south'] = game_tiles[t1].tile_grid[len(tile_grid) - 1]
                                game_tiles[t1].edges['west'] = ''.join([row[0] for row in game_tiles[t1].tile_grid])
                                game_tiles[t1].edges['east'] = ''.join([row[len(row) - 1] for row in game_tiles[t1].tile_grid])
                            elif k == 'east' or k == 'west':
                                #print('flipping vertical')
                                #print('grid before flip:')
                                #for row in game_tiles[t1].tile_grid:
                                #    print(row)
                                #print
                                game_tiles[t1].tile_grid = flip_vertical(game_tiles[t1].tile_grid)
                                #print('grid after flip:')
                                #for row in game_tiles[t1].tile_grid:
                                #    print(row)
                                #print
                                game_tiles[t1].edges['north'] = game_tiles[t1].tile_grid[0]
                                game_tiles[t1].edges['south'] = game_tiles[t1].tile_grid[len(tile_grid) - 1]
                                game_tiles[t1].edges['west'] = ''.join([row[0] for row in game_tiles[t1].tile_grid])
                                game_tiles[t1].edges['east'] = ''.join([row[len(row) - 1] for row in game_tiles[t1].tile_grid])
                            return t1
    return None


def part1():
    for t1 in game_tiles:
        for t2 in game_tiles:
            if t1 == t2:
                continue
            else:
                for e in game_tiles[t1].edges.values():
                    if e in game_tiles[t2].edges.values() or e[::-1] in game_tiles[t2].edges.values():
                        tile_count[t1] += 1
    minval = min(tile_count.values())
    total = 1
    for i in tile_count:
        if tile_count[i] == minval:
            total *= i
    print(total)

def part2():
    layout = []
    found_nw = False
    while found_nw != True:
        for i in game_tiles:
            found_n = False
            found_w = False
            edge_n = game_tiles[i].edges['north']
            edge_w = game_tiles[i].edges['west']
            for t1 in game_tiles:
                if t1 == i:
                    continue
                else:
                    if edge_n in game_tiles[t1].edges.values() or edge_n[::-1] in game_tiles[t1].edges.values():
                        found_n = True
                    if edge_w in game_tiles[t1].edges.values() or edge_w[::-1] in game_tiles[t1].edges.values():
                        found_w = True
            if found_n == False and found_w == False:
                row = [i]
                layout.append(row)
                found_nw = True
    row_count = 0
    col_count = 0
    curr_tile = layout[row_count][col_count]
    neighbor_e = True
    neighbor_s = True
    while neighbor_e or neighbor_s:
        #print('current tile: ', curr_tile)
        #for row in game_tiles[curr_tile].tile_grid:
        #    print(row)
        #print
        neighbor_e = find_neighbor(curr_tile, game_tiles[curr_tile].edges['east'], 'west')
        if neighbor_e:
            layout[row_count].append(neighbor_e)
            col_count += 1
            curr_tile = layout[row_count][col_count]
        else:
            #print('reached the end of row, no east neighbor')
            col_count = 0
            curr_tile = layout[row_count][col_count]
            neighbor_s = find_neighbor(curr_tile, game_tiles[curr_tile].edges['south'], 'north')
            if neighbor_s:
                layout.append([neighbor_s])
                row_count += 1
            curr_tile = layout[row_count][col_count]
            #print('east neighbor: ', neighbor_e)
            #print(game_tiles[neighbor_e].edges)
    
    #for line in layout:
    #    print(line)

    big_picture = []
    for x in range(len(layout[0])):
        row_count = 0
        if len(big_picture) == 0:
            for y in range(len(layout[x])):
                #print(layout[y][x])
                for line in game_tiles[layout[y][x]].tile_grid[1:-1]:
                    big_picture.append(''.join(line[1:-1]))
                    row_count += 1
        
        else:
            for y in range(len(layout[y])):
                #print(layout[y][x])
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
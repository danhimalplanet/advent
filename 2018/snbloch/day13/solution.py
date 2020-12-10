class board:
    cart_counter = 0
    cart_directions = []
    cart_positions = []
    cart_turns = []
    grid = []
    corners = []
    intersections = []
    def turn_at_intersection(self, cart_index):
        if (self.cart_turns[cart_index] + 1) % 3 == 1:
            self.turn_left(cart_index)
            self.cart_turns[cart_index] += 1
        elif (self.cart_turns[cart_index] + 1) % 3 == 2:
            self.cart_turns[cart_index] += 1
        elif (self.cart_turns[cart_index] + 1) % 3 == 0:
            self.turn_right(cart_index)
            self.cart_turns[cart_index] += 1
    def turn_left(self, cart_index):
        if self.cart_directions[cart_index] == '^':
            self.cart_directions[cart_index] = '<'
        elif self.cart_directions[cart_index] == '<':
            self.cart_directions[cart_index] = 'v'
        elif self.cart_directions[cart_index] == 'v':
            self.cart_directions[cart_index] = '>'
        elif self.cart_directions[cart_index] == '>':
            self.cart_directions[cart_index] = '^'
    def turn_right(self, cart_index):
        if self.cart_directions[cart_index] == '^':
            self.cart_directions[cart_index] = '>'
        elif self.cart_directions[cart_index] == '>':
            self.cart_directions[cart_index] = 'v'
        elif self.cart_directions[cart_index] == 'v':
            self.cart_directions[cart_index] = '<'
        elif self.cart_directions[cart_index] == '<':
            self.cart_directions[cart_index] = '^'
    with open('input.txt', 'r') as inputfile:
        y = 0
        for line in inputfile:
            curr_line = []
            x = 0
            for char in line:
                if char == '/':
                    corners.append([(x, y), '/'])
                    curr_line.append(' ')
                elif char == '\\':
                    corners.append([(x, y), '\\'])
                    curr_line.append(' ')
                elif char == '+':
                    intersections.append((x, y))
                    curr_line.append(' ')
                elif char == '^':
                    curr_line.append(cart_counter)
                    cart_directions.append('^')
                    cart_positions.append((x, y))
                    cart_turns.append(0)
                    cart_counter += 1
                elif char == '>':
                    curr_line.append(cart_counter)
                    cart_directions.append('>')
                    cart_positions.append((x, y))
                    cart_turns.append(0)
                    cart_counter += 1
                elif char == 'v':
                    curr_line.append(cart_counter)
                    cart_directions.append('v')
                    cart_positions.append((x, y))
                    cart_turns.append(0)
                    cart_counter += 1
                elif char == '<':
                    curr_line.append(cart_counter)
                    cart_directions.append('<')
                    cart_positions.append((x, y))
                    cart_turns.append(0)
                    cart_counter += 1
                else:
                    curr_line.append(' ')
                x += 1
            grid.append(curr_line)
            y += 1

def move(cart_index, board):
    if board.cart_directions[cart_index] == '^':
        if (board.cart_positions[cart_index][0], board.cart_positions[cart_index][1] - 1) in board.cart_positions:
            collision_x = board.cart_positions[cart_index][0]
            collision_y = board.cart_positions[cart_index][1] - 1
            board.grid[board.cart_positions[cart_index][1]][board.cart_positions[cart_index][0]] = ' '
            board.grid[board.cart_positions[cart_index][1] - 1][board.cart_positions[cart_index][0]] = ' '
            board.cart_positions[board.cart_positions.index((board.cart_positions[cart_index][0], board.cart_positions[cart_index][1] - 1))] = None
            board.cart_positions[cart_index] = None
            board.cart_counter -= 2
            return (collision_x, collision_y)
        board.cart_positions[cart_index] = (board.cart_positions[cart_index][0], board.cart_positions[cart_index][1] - 1)
        if (board.cart_positions[cart_index][0], board.cart_positions[cart_index][1]) in board.intersections:
            board.turn_at_intersection(cart_index)
            return
        for c in board.corners:
            if c[0] == (board.cart_positions[cart_index][0], board.cart_positions[cart_index][1]):
                if c[1] == '\\':
                    board.turn_left(cart_index)
                elif c[1] == '/':
                    board.turn_right(cart_index)
                return
    elif board.cart_directions[cart_index] == '>':
        if (board.cart_positions[cart_index][0] + 1, board.cart_positions[cart_index][1]) in board.cart_positions:
            collision_x = board.cart_positions[cart_index][0] + 1
            collision_y = board.cart_positions[cart_index][1]
            board.grid[board.cart_positions[cart_index][1]][board.cart_positions[cart_index][0]] = ' '
            board.grid[board.cart_positions[cart_index][1]][board.cart_positions[cart_index][0] + 1] = ' '
            board.cart_positions[board.cart_positions.index((board.cart_positions[cart_index][0] + 1, board.cart_positions[cart_index][1]))] = None
            board.cart_positions[cart_index] = None
            board.cart_counter -= 2
            return (collision_x, collision_y)
        board.cart_positions[cart_index] = (board.cart_positions[cart_index][0] + 1, board.cart_positions[cart_index][1])
        if (board.cart_positions[cart_index][0], board.cart_positions[cart_index][1]) in board.intersections:
            board.turn_at_intersection(cart_index)
            return
        for c in board.corners:
            if c[0] == (board.cart_positions[cart_index][0], board.cart_positions[cart_index][1]):
                if c[1] == '\\':
                    board.turn_right(cart_index)
                elif c[1] == '/':
                    board.turn_left(cart_index)
                return
    if board.cart_directions[cart_index] == 'v':
        if (board.cart_positions[cart_index][0], board.cart_positions[cart_index][1] + 1) in board.cart_positions:
            collision_x = board.cart_positions[cart_index][0]
            collision_y = board.cart_positions[cart_index][1] + 1
            board.grid[board.cart_positions[cart_index][1]][board.cart_positions[cart_index][0]] = ' '
            board.grid[board.cart_positions[cart_index][1] + 1][board.cart_positions[cart_index][0]] = ' '
            board.cart_positions[board.cart_positions.index((board.cart_positions[cart_index][0], board.cart_positions[cart_index][1] + 1))] = None
            board.cart_positions[cart_index] = None
            board.cart_counter -= 2
            return (collision_x, collision_y)
        board.cart_positions[cart_index] = (board.cart_positions[cart_index][0], board.cart_positions[cart_index][1] + 1)
        if (board.cart_positions[cart_index][0], board.cart_positions[cart_index][1]) in board.intersections:
            board.turn_at_intersection(cart_index)
            return
        for c in board.corners:
            if c[0] == (board.cart_positions[cart_index][0], board.cart_positions[cart_index][1]):
                if c[1] == '\\':
                    board.turn_left(cart_index)
                elif c[1] == '/':
                    board.turn_right(cart_index)
                return
    if board.cart_directions[cart_index] == '<':
        if (board.cart_positions[cart_index][0] - 1, board.cart_positions[cart_index][1]) in board.cart_positions:
            collision_x = board.cart_positions[cart_index][0] - 1
            collision_y = board.cart_positions[cart_index][1]
            board.grid[board.cart_positions[cart_index][1]][board.cart_positions[cart_index][0]] = ' '
            board.grid[board.cart_positions[cart_index][1]][board.cart_positions[cart_index][0] - 1] = ' '
            board.cart_positions[board.cart_positions.index((board.cart_positions[cart_index][0] - 1, board.cart_positions[cart_index][1]))] = None
            board.cart_positions[cart_index] = None
            board.cart_counter -= 2
            return (collision_x, collision_y)
        board.cart_positions[cart_index] = (board.cart_positions[cart_index][0] - 1, board.cart_positions[cart_index][1])
        if (board.cart_positions[cart_index][0], board.cart_positions[cart_index][1]) in board.intersections:
            board.turn_at_intersection(cart_index)
            return
        for c in board.corners:
            if c[0] == (board.cart_positions[cart_index][0], board.cart_positions[cart_index][1]):
                if c[1] == '\\':
                    board.turn_right(cart_index)
                elif c[1] == '/':
                    board.turn_left(cart_index)
                return
        
def part1():
    game_board = board()

    crashed = False
    while crashed == False:
        moved = set()
        for y in range(len(game_board.grid)):
            for x in range(len(game_board.grid[y])):
                if (x, y) in game_board.cart_positions:
                    if game_board.cart_positions.index((x, y)) not in moved:
                        moved.add(game_board.cart_positions.index((x, y)))
                        m = move(game_board.cart_positions.index((x, y)), game_board)
                        if m != None:
                            print(str(m[0]) + ',' + str(m[1]))
                            crashed = True

def part2():
    game_board = board()

    while game_board.cart_counter > 1:
        moved = set()
        for y in range(len(game_board.grid)):
            for x in range(len(game_board.grid[y])):
                if (x, y) in game_board.cart_positions:
                    if game_board.cart_positions.index((x, y)) not in moved:
                        moved.add(game_board.cart_positions.index((x, y)))
                        move(game_board.cart_positions.index((x, y)), game_board)
    for i in game_board.cart_positions:
        if i is not None:
            print(str(i[0]) + ',' + str(i[1]))

if __name__ == '__main__':
    part1()
    part2()
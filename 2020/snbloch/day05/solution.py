import io, math

def bisect(start, end, dir):
    range_size = math.floor((end - start) / 2)
    if dir == 'F' or dir == 'L':
        return start, start + range_size
    elif dir == 'B' or dir == 'R':
        return end - range_size, end

def part1():
    values = []
    max_id = 0
    with open('input.txt', 'r') as inputfile:
        for line in inputfile:
            values.append(line.strip())
    for v in values:
        row_start, row_end = 0, 127
        col_start, col_end = 0, 7
        for char in v:
            if char == 'F' or char == 'B':
                row_start, row_end = bisect(row_start, row_end, char)
            elif char == 'L' or char == 'R':
                col_start, col_end = bisect(col_start, col_end, char)
        if row_end * 8 + col_end > max_id:
            max_id = row_end * 8 + col_end
    print(max_id)

def part2():
    values = []
    seats = []
    with open('input.txt', 'r') as inputfile:
        for line in inputfile:
            values.append(line.strip())
    for v in values:
        row_start, row_end = 0, 127
        col_start, col_end = 0, 7
        for char in v:
            if char == 'F' or char == 'B':
                row_start, row_end = bisect(row_start, row_end, char)
            elif char == 'L' or char == 'R':
                col_start, col_end = bisect(col_start, col_end, char)
        seats.append(row_end * 8 + col_end)
    for s in sorted(seats):
        if s + 1 not in seats and s + 2 in seats:
            print(s + 1)
            break

if __name__ == '__main__':
    part1()
    part2()

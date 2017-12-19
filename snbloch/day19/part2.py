import io

alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
seen = []
end = False

file = open('input.txt', 'r')
tubes = []
for line in file:
    tubes.append(line.replace('\n', ''))

current_row = 0
current_column = 0
direction = 'down'
step_counter = 0
# Move to starting position
current_column = tubes[current_row].index('|')

while end == False:
    if direction == 'down':
        while tubes[current_row][current_column] != '+' and tubes[current_row][current_column] != ' ':
            current_row += 1
            step_counter += 1
            if tubes[current_row][current_column] in alpha:
                seen.append(tubes[current_row][current_column])
        if tubes[current_row][current_column + 1] == '-':
            direction = 'right'
            current_column += 1
            step_counter += 1
        elif tubes[current_row][current_column - 1] == '-':
            direction = 'left'
            current_column -= 1
            step_counter += 1
        else:
            end = True

    if direction == 'right':
        while tubes[current_row][current_column] != '+' and tubes[current_row][current_column] != ' ':
            current_column += 1
            step_counter += 1
            if tubes[current_row][current_column] in alpha:
                seen.append(tubes[current_row][current_column])
        if tubes[current_row + 1][current_column] == '|':
            direction = 'down'
            current_row += 1
            step_counter += 1
        elif tubes[current_row - 1][current_column] == '|':
            direction = 'up'
            current_row -= 1
            step_counter += 1
        else:
            end = True

    if direction == 'up':
        while tubes[current_row][current_column] != '+' and tubes[current_row][current_column] != ' ':
            current_row -= 1
            step_counter += 1
            if tubes[current_row][current_column] in alpha:
                seen.append(tubes[current_row][current_column])
        if tubes[current_row][current_column + 1] == '-':
            direction = 'right'
            current_column += 1
            step_counter += 1
        elif tubes[current_row][current_column - 1] == '-':
            direction = 'left'
            current_column -= 1
            step_counter += 1
        else:
            end = True

    if direction == 'left':
        while tubes[current_row][current_column] != '+' and tubes[current_row][current_column] != ' ':
            current_column -= 1
            step_counter += 1
            if tubes[current_row][current_column] in alpha:
                seen.append(tubes[current_row][current_column])
        if tubes[current_row - 1][current_column] == '|':
            direction = 'up'
            current_row -= 1
            step_counter += 1
        elif tubes[current_row + 1][current_column] == '|':
            direction = 'down'
            current_row += 1
            step_counter += 1
        else:
            end = True

print step_counter

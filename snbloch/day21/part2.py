import io
import math
import numpy as np
import collections

enhancement_rules = []
transformed_outputs = []
puzzle_input = np.array([['.','#','.'], ['.','.','#'], ['#','#','#']])

file = open('input.txt', 'r')
for line in file:
    rule = []
    output = []
    for i in line.split(' => ')[0].split('/'):
        rule.append(list(i.replace('\n', '')))
    enhancement_rules.append(np.asarray(rule))
    for i in line.split(' => ')[1].split('/'):
        output.append(list(i.replace('\n', '')))
    transformed_outputs.append(np.asarray(output))

def transform(input):
    output_panels = []
    if len(input) % 2 == 0:
        divisor = 2
    else:
        divisor = 3
    width = len(input) / divisor
    height = len(input) / divisor
    counter_x = 0
    while counter_x < width:
        counter_y = 0
        while counter_y < height:
            start_x = counter_x * divisor
            start_y = counter_y * divisor
            match_location = find_match(input[start_x:start_x + divisor, start_y:start_y + divisor])
            output_panels.append(transformed_outputs[match_location])
            counter_y += 1
        counter_x += 1
    square_root = math.sqrt(len(output_panels))
    output_counter = 0
    counter_y = 0
    output_rows = []
    while counter_y < square_root:
        counter_x = 0
        output_rows.append([])
        while counter_x < square_root:
            output_rows[counter_y].append(output_panels[output_counter])
            output_counter += 1
            counter_x += 1
        counter_y += 1

    counter = 0
    while counter < len(output_rows):
        output_rows[counter] = np.concatenate(output_rows[counter], axis = 1)
        counter += 1
    final_output = np.vstack(output_rows.pop(0))
    counter = 0
    while counter < len(output_rows):
        final_output = np.vstack((final_output, output_rows.pop(0)))
    return final_output

def find_match(square):
    rotation_counter = 0
    global enhancement_rules
    matched = False
    while rotation_counter < 4 and matched == False:
        flip_counter = 0
        while flip_counter < 2 and matched == False:
            counter = 0
            while counter < len(enhancement_rules) and matched == False:
                if np.array_equal(square, enhancement_rules[counter]):
                    return counter
                counter += 1
            square = np.flipud(square)
            flip_counter += 1
        square = np.rot90(square)
        rotation_counter += 1
    return False

iter_counter = 0
while iter_counter < 18:
    print 'Starting iteration: ', iter_counter
    puzzle_input = transform(puzzle_input)
    iter_counter += 1

unique, counts = np.unique(puzzle_input, return_counts=True)
used_count = dict(zip(unique, counts))
print used_count['#']

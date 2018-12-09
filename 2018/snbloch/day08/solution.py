import io

def calculate_value(input_array, position):
    child_values = []
    value = 0
    num_children = input_array[position]
    num_metadata = input_array[position + 1]
    if num_children == 0:
        metadata = input_array[position + 2:position + 2 + num_metadata]
        for i in metadata:
            value += i
        #print 'No children for string',input_array[position:position + 2 + num_metadata]
        #print 'Returning value of',value,'and position of',position + 2 + num_metadata
        return value, position + 2 + num_metadata
    else:
        counter = 0
        new_position = position + 2
        while counter < num_children:
            #print 'Calculating value of child beginning at position',new_position
            child_value, new_position = calculate_value(input_array, new_position)
            #print 'Returning value of',child_value,'and position of',new_position
            child_values.append(child_value)
            counter += 1
        metadata = input_array[new_position:new_position + num_metadata]
        for i in metadata:
            if i > len(child_values) or i == 0:
                continue
            else:
                value += child_values[i - 1]
        return value,new_position + num_metadata

def part1():
    input_array = []
    all_metadata = []
    with open('input.txt', 'r') as inputfile:
        for line in inputfile:
            for i in line.strip().split():
                input_array.append(int(i))
    position = 0
    while position < len(input_array):
        if input_array[position] != 0:
            position += 2
        else:
            num_metadata = input_array[position + 1]
            metadata_position = position + 2
            counter = 0
            while counter < num_metadata:
                all_metadata.append(input_array[metadata_position])
                input_array.__delitem__(metadata_position)
                counter += 1
            input_array.__delitem__(position + 1)
            input_array.__delitem__(position)
            if position >= 2:
                input_array[position - 2] -= 1
                position -= 2
    print 'Part 1: sum of all metadata is',sum(all_metadata)

def part2():
    input_array = []
    with open('input.txt', 'r') as inputfile:
        for line in inputfile:
            for i in line.strip().split():
                input_array.append(int(i))
    value, position = calculate_value(input_array, 0)
    print 'Part 2: value of root node is',value

if __name__ == '__main__':
    part1()
    part2()

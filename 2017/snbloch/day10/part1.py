lengths = '94,84,0,79,2,27,81,1,123,93,218,23,103,255,254,243'
list_length = 256
output = range(list_length)
current_position = 0
skip_size = 0
select = []
reverse = []

for i in lengths.split(','):
    del select[:]
    current_length = int(i)
    print 'Current Position: ', current_position
    print 'Current Length: ', current_length

    counter = 0
    select_position = current_position
    while counter < current_length:
        select.append(output[select_position])
        if select_position + 1 >= len(output):
            select_position = 0
        else:
            select_position += 1
        counter += 1
    print 'List selected for reversing: ', select

    del reverse[:]
    counter = 0
    reverse_position = len(select) - 1
    while counter < len(select):
        reverse.append(select[reverse_position])
        counter += 1
        reverse_position -= 1
    print 'Reversed list: ', reverse

    counter = 0
    while counter < len(reverse):
        output[current_position] = reverse[counter]
        if current_position + 1 >= len(output):
            current_position = 0
        else:
            current_position += 1
        counter += 1
    print 'Output: ', output

    print 'Final position after reversing is: ', current_position

    if current_position + skip_size >= len(output):
        current_position = skip_size - (len(output) - current_position)
    else:
        current_position += skip_size
    print 'Skip size is: ', skip_size
    print 'Final position after skip is: ', current_position

    skip_size += 1

with open('spreadsheet.txt', 'r') as in_file:
    lines = (line for line in in_file)
    checksum = 0
    for line in lines:
        cells = line.split('\t')
        cells[-1]=cells[-1].strip('\n')
        min = int(cells[0])
        max = int(cells[0])
        for i in range(1, len(cells)):
            if int(cells[i]) > max:
                max = int(cells[i])
            if int(cells[i]) < min:
                min = int(cells[i])
            row_diff = max - min
        checksum = checksum + row_diff
print(checksum)

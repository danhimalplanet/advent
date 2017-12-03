import io
sum = 0

f = open('input.txt', mode='r')
for line in f:
    content = line.split('\t')
    content = map(int, content)
    content.sort()
    sum += content[len(content)-1] - content[0]

print sum

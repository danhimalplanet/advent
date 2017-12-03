import io
sum = 0

f = open('input.txt', mode='r')
for line in f:
    content = line.split('\t')
    content = map(int, content)
    content.sort()
    for i in content:
        for j in content:
            if (j != i) and (j % i == 0):
                sum += j / i

print sum

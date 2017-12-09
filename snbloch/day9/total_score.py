import io

f = open('input.txt', mode='r')
for line in f:
    stream = line
f.close()

# Flags:
ignore = False
garbage = False

open_groups = 0
total_score = 0
stream_iterator = 0

while stream_iterator < len(stream):
    char = stream[stream_iterator]
    if ignore == True:
        stream_iterator += 1
        char = stream[stream_iterator]
        ignore = False
    if char == '!':
        ignore = True
    if char == '<' and garbage == False:
        garbage = True
    if garbage == True and char == '>':
        garbage = False
    if char == '{' and garbage == False:
        open_groups += 1
        total_score += open_groups
    if char == '}' and garbage == False:
        open_groups -= 1
    stream_iterator += 1

print 'Total score: ', total_score

import io

f = open('input.txt', mode='r')
for line in f:
    stream = line
f.close()

# Flags:
ignore = False
garbage = False

garbage_count = 0
stream_iterator = 0

def count_garbage(char):
    global ignore
    global garbage
    global garbage_count
    global stream_iterator

    if ignore == True:
        if stream_iterator == len(stream) - 1:
            pass
        else:
            stream_iterator += 1
        ignore = False
        return
    if char == '!':
        ignore = True
        if stream_iterator == len(stream) - 1:
            pass
        else:
            stream_iterator += 1
        return
    if char == '<' and garbage == False:
        if stream_iterator == len(stream) - 1:
            pass
        else:
            stream_iterator += 1
        garbage = True
        return
    if garbage == True and char == '>':
        if stream_iterator == len(stream) - 1:
            pass
        else:
            stream_iterator += 1
        garbage = False
        return
    if char == '{' and garbage == False:
        pass
    if char == '}' and garbage == False:
        pass
    if garbage == True:
        garbage_count += 1
    stream_iterator += 1

while stream_iterator < len(stream):
    count_garbage(stream[stream_iterator])

print 'Total garbage: ', garbage_count

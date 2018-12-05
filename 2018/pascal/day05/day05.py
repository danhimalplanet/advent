import time

t0 = time.time()
d = open('input.txt').read()

# The slow way
#
# def flatten(s):
#     i = 0
#     s[:] = map(ord, s)
#     j = len(s)-1
#     r = 0
#     while i < j:
#         if s[i] ^ s[i+1] == 32:
#             s[i] = 33
#             s[i+1] = 33
#             i+=2
#             r+=2
#             continue
#         i+=1
#     s[:] = [ x for x in s if x != 33]
#     s[:] = map(chr, s)
#     return r
#
# def shortest(s):
#     while flatten2(s):
#         pass
#     return len(s)

# more or less from r/adventofcode, after looking for ways tos peed the above up

def react(s):
    stack = [s.pop()]

    while s:
        x = s.pop()

        if not stack:
            stack.append(x)
            continue

        if ord(x) ^ ord(stack[-1]) == 32:
            stack.pop()
        else:
            stack.append(x)

    return len(stack)


# Part 1
print(react(list(d)))

# Part 2
counts = []
for i in range(ord('A'), ord('Z') + 1):
    rm = chr(i)
    counts.append(react(list(d.replace(rm.lower(), '').replace(rm.upper(), ''))))

counts.sort()
print(counts[0])
t1 = time.time()
print(t1 - t0)

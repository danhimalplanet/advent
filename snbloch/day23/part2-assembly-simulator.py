def runit():
    a = 1
    b = 0
    c = 0
    d = 0
    e = 0
    f = 0
    g = 0
    h = 0

    b = 65
    c = b
    b *= 100
    b += 100000
    c = b
    c += 17000
    while True:
        f = 1
        d = 2
        e = 2
        while True:
            if (b % d == 0):
                f = 0
            d += 1
            if d != b:
                continue
            if f == 0:
                h += 1
            if b == c:
                return h
            b += 17
            break

print runit()

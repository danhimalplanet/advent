a = 1
b = 0
c = 0
d = 0
e = 0
f = 0
g = 0
h = 0

b = 57
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
        g = d
        g *= e
        g -= b
        if g == 0:
            f = 0
        else:
            e -= 1
            g = e
            g -= b
            if g == 0:
                continue
            d += 1
            g = d
            g -= b
            if g == 0:
                break
            if f == 0:
                h += 1
            else:
                if b == c:
                    print(f"h: {h}")
                else:
                    b -= 17
                    break


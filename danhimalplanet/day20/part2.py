class Particle:

    def __init__(self, p, v, a):
        self.p = p
        self.v = v
        self.a = a

    def __str__(self):
        return f'pos: {self.p} vel: {self.p} acc: {self.a} '

    def move(self):
        self.v[0] += self.a[0]
        self.v[1] += self.a[1]
        self.v[2] += self.a[2]
        self.p[0] += self.v[0]
        self.p[1] += self.v[1]
        self.p[2] += self.v[2]

    def distance(self):
        return abs(self.p[0]) + abs(self.p[1]) + abs(self.p[2])

def closest_to_zero(particles):
    index = None
    distance = None
    for x in range(0, len(particles)):
        if index == None:
            index = x
            distance = particles[x].distance()
        else:
            if particles[x].distance() < distance:
                distance = particles[x].distance()
                index = x
    return index

particles={}

f = open("in.txt", "r")

j=0
for line in f:
    _p = line.split(", ")[0].strip("p=< ").strip(">").strip("\n")
    p = []
    for _ in _p.split(","):
        p.append(int(_.strip("'")))
    _v = line.split(", ")[1].strip("v=< ").strip(">")
    v = []
    for _ in _v.split(","):
        v.append(int(_.strip("'")))
    a=[]
    _a = line.split(", ")[2].strip("a=< ").split(",")
    _a[2] = _a[2].strip('>\n')
    #_a = a[0:-2]
    for _ in _a:
        a.append(int(_.strip("'")))
    particles[j] = Particle(p,v,a)
    j = j + 1


def removekey(d, key):
    r = dict(d)
    del r[key]
    return r

x = 1
while x < 2000:
    for key, _ in particles.items():
        particles[key].move()
    naughty = []
    for k, value in particles.items():
        for j in particles.keys():
            if k != j:
                if particles[k].p == particles[j].p:
                    naughty.append(k)
                    naughty.append(j)
    for n in set(sorted(naughty, reverse=True)):
        particles.pop(n)
    print(len(particles))
    x = x + 1

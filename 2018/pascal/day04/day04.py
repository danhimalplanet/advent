from datetime import datetime
import numpy as np

d = open('input.txt').readlines()
d = [ [datetime.strptime(x[1:17], '%Y-%m-%d %H:%M'), x.split()[3]] for x in d]
d.sort(key=lambda k: k[0])

# Count number of guards
guardcnt = sum([x[1][0] == '#' for x in d])

# Map of guard ID -> row
guardmap = {}

guarddata = np.zeros((guardcnt, 60), dtype=np.int)

guard = None
wakes: datetime = None
sleeps: datetime = None

i=0
for t,e in d:
    if e.startswith('#'):
        guard = int(e[1:])
        continue

    if e.startswith('a'):
        sleeps = t
        continue

    if e.startswith('u'):
        wakes = t
        if guard not in guardmap:
            guardmap[guard] = i
            i += 1

        guarddata[guardmap[guard], sleeps.minute:wakes.minute] += 1
        continue

# Build reverse guard map
guardmap2 = {v: k for k, v in guardmap.items()}

# part 1
sums = np.apply_along_axis(np.sum, 1, guarddata)
sleepyguard_row = sums.argmax()
sleepyguard_id = guardmap2[sleepyguard_row]
sleepyguard_minute = guarddata[sleepyguard_row,:].argmax()
print(sleepyguard_id * sleepyguard_minute)

# part 2
sleepyguard = np.unravel_index(np.argmax(guarddata), guarddata.shape)
sleepyguard_id = guardmap2[sleepyguard[0]]
sleepyguard_minute = sleepyguard[1]
print(sleepyguard_id * sleepyguard_minute)
import io

f = open('input.txt', mode='r')

programs = []

for line in f:
    if '->' in line:
        programs.append(str(line.replace('->','|').split('|')[0]).strip())
f.close()

counter = {}
f = open('input.txt', mode='r')
for line in f:
    for prog in programs:
        if prog.split(' ')[0] in line:
            if counter.has_key(prog.split(' ')[0]):
                counter[prog.split(' ')[0]] += 1
            else:
                counter[prog.split(' ')[0]] = 1

for name, count in counter.iteritems():
    if count == 1:
        print name

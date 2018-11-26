import io

valid_passwords = 0

f = open('input.txt', mode='r')
for line in f:
    line = line.split(' ')
    content = []
    deduplicated_content = set([])
    for i in line:
        i = ''.join(sorted(i)).strip()
        content.append(i)
        deduplicated_content.add(i)
    if len(content) != len(deduplicated_content):
        print 'invalid password' + str(content)
    else:
        valid_passwords += 1

print 'Number of valid password: ' + str(valid_passwords)

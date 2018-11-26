import io

valid_passwords = 0

f = open('input.txt', mode='r')
for line in f:
    line = line.split(' ')
    content = []
    deduplicated_content = set([])
    for i in line:
        content.append(i.strip())
        deduplicated_content.add(i.strip())
    if len(content) != len(deduplicated_content):
        print 'invalid password' + str(content)
    else:
        valid_passwords += 1

print 'Number of valid password: ' + str(valid_passwords)

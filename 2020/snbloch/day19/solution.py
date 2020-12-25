import regex

input_rules = {}
input_messages = []
with open('input.txt', 'r') as inputfile:
    rules, messages = inputfile.read().split('\n\n')
for rule in rules.split('\n'):
    id = int(rule.strip().split(': ')[0])
    input_rules[id] = rule.strip().split(': ')[1].replace('"', '')
for message in messages.strip().split('\n'):
    input_messages.append(message.strip())

def expand(rule):
    if rule.isdigit():
        return group(int(rule))
    else:
        return rule

def group(id):
    return '(?:' + ''.join(map(expand, input_rules[id].split())) + ')'

def match(rules, messages):
    reg = regex.compile(group(0))
    counter = 0
    for message in messages:
        if reg.fullmatch(message):
            counter += 1
    return counter

def part1():
    total = match(input_rules, input_messages)
    print(total)

def part2():
    input_rules[8] = '42 +'
    input_rules[11] = '(?P<group> 42 (?&group)? 31 )'
    total = match(input_rules, input_messages)
    print(total)

if __name__ == '__main__':
    part1()
    part2()
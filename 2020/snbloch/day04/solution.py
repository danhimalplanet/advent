import io
passport_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']

def is_field_valid(key, value):
    if key == 'byr':
        if int(value) >= 1920 and int(value) <= 2002:
            return True
        else:
            return False
    if key == 'iyr':
        if int(value) >= 2010 and int(value) <= 2020:
            return True
        else:
            return False
    if key == 'eyr':
        if int(value) >= 2020 and int(value) <= 2030:
            return True
        else:
            return False
    if key == 'hgt':
        if 'cm' in value:
            if int(value.split('cm')[0]) >= 150 and int(value.split('cm')[0]) <= 193:
                return True
            else:
                return False
        elif 'in' in value:
            if int(value.split('in')[0]) >= 59 and int(value.split('in')[0]) <= 76:
                return True
            else:
                return False
        else:
            return False
    if key == 'hcl':
        if len(value) != 7:
            return False
        if value[0] != '#':
            return False
        for i in value[1:]:
            if i not in '01234567890abcdef':
                return False
        return True
    if key == 'ecl':
        if value in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
            return True
        else:
            return False
    if key == 'pid':
        if len(value) != 9:
            return False
        for i in value:
            if i not in '0123456789':
                return False
        return True

def is_passport_valid(passport, optional, validate_fields):
    for field in passport_fields:
        if field in optional:
            continue
        else:
            if field not in passport:
                return False
            if validate_fields:
                if not is_field_valid(field, passport[field]):
                    return False
    return True

def part1():
    values = []
    with open('input.txt', 'r') as inputfile:
        current_dict = {}
        for line in inputfile:   
            if line.strip() == '':
                values.append(current_dict)
                current_dict = {}
            else:
                for field in line.strip().split():
                    kv_pair = field.split(':')
                    key, value = kv_pair[0], kv_pair[1]
                    current_dict[key] = value
    valid_count = 0
    for v in values:
        if is_passport_valid(v, ['cid'], False):
            valid_count +=1
    print(valid_count)

def part2():
    values = []
    with open('input.txt', 'r') as inputfile:
        current_dict = {}
        for line in inputfile:   
            if line.strip() == '':
                values.append(current_dict)
                current_dict = {}
            else:
                for field in line.strip().split():
                    kv_pair = field.split(':')
                    key, value = kv_pair[0], kv_pair[1]
                    current_dict[key] = value
    valid_count = 0
    for v in values:
        if is_passport_valid(v, ['cid'], True):
            valid_count +=1
    print(valid_count)

if __name__ == '__main__':
    part1()
    part2()
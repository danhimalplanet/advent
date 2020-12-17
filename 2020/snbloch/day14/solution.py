def part1():
    mem_registers = {}
    with open('input.txt', 'r') as inputfile:
        for line in inputfile:
            if line.strip().startswith('mask'):
                curr_mask_positions = {}
                mask = line.strip().split('mask = ')[1]
                for i in range(len(mask)):
                    if mask[i] == 'X':
                        continue
                    else:
                        curr_mask_positions[i] = int(mask[i])
            else:
                register = int(line.strip().split('[')[1].split(']')[0])
                value = int(line.strip().split(' = ')[1])
                value_as_binary = list(bin(value)[2:].zfill(36))
                for i in curr_mask_positions:
                    value_as_binary[i] = curr_mask_positions[i]
                value_as_binary = ''.join(str(i) for i in value_as_binary)
                value_as_decimal = int(value_as_binary, 2)
                mem_registers[register] = value_as_decimal
    total = 0
    for i in mem_registers:
        total += mem_registers[i]
    print(total)

def part2():
    mem_registers = {}
    with open('input.txt', 'r') as inputfile:
        for line in inputfile:
            if line.strip().startswith('mask'):
                curr_mask_positions = {}
                mask = line.strip().split('mask = ')[1]
                for i in range(len(mask)):
                    if mask[i] == 'X':
                        curr_mask_positions[i] = mask[i]
                    else:
                        curr_mask_positions[i] = int(mask[i])
            else:
                register = int(line.strip().split('[')[1].split(']')[0])
                value = int(line.strip().split(' = ')[1])
                register_as_binary = list(bin(register)[2:].zfill(36))
                registers_to_modify = set()
                for i in curr_mask_positions:
                    if curr_mask_positions[i] == 0:
                        continue
                    elif curr_mask_positions[i] == 1:
                        register_as_binary[i] = 1
                for i in curr_mask_positions:
                    if curr_mask_positions[i] == 'X':
                        if len(registers_to_modify) == 0:
                            modify_register = register_as_binary[:]
                            for j in range(2):
                                modify_register[i] = j
                                registers_to_modify.add(''.join(str(i) for i in modify_register))
                        else:
                            reg = registers_to_modify.copy()
                            for r in reg:
                                modify_register = [int(j) for j in r]
                                for k in range(2):
                                    modify_register[i] = k
                                    registers_to_modify.add(''.join(str(i) for i in modify_register))
                for i in registers_to_modify:
                    register_as_decimal = int(i, 2)
                    mem_registers[register_as_decimal] = value
    total = 0
    for i in mem_registers:
        total += mem_registers[i]
    print(total)
    
if __name__ == '__main__':
    part1()
    part2()
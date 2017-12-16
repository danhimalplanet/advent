import io

programs = []
programs.append('a')
programs.append('b')
programs.append('c')
programs.append('d')
programs.append('e')
programs.append('f')
programs.append('g')
programs.append('h')
programs.append('i')
programs.append('j')
programs.append('k')
programs.append('l')
programs.append('m')
programs.append('n')
programs.append('o')
programs.append('p')

dance_moves = []

file = open('input.txt', 'r')
for i in file.read().split(','):
    dance_moves.append(i)

counter = 0
while counter < 16: # Dance has periodicity of 48, and 1,000,000,000 % 48 is 16
    for i in dance_moves:
        if i[0] == 's':
            spin = int(i[1:].strip())
            temp = []
            spin_position = len(programs) - spin
            while spin_position < len(programs):
                temp.append(programs[spin_position])
                spin_position += 1
            spin_position = 0
            while spin_position < len(programs) - spin:
                temp.append(programs[spin_position])
                spin_position += 1
            programs = temp

        elif i[0] == 'x':
            exchange = i[1:].strip()
            exchange_first_position = int(exchange.split('/')[0])
            exchange_second_position = int(exchange.split('/')[1])
            exchange_first_value = programs[exchange_first_position]
            exchange_second_value = programs[exchange_second_position]
            programs[exchange_first_position] = exchange_second_value
            programs[exchange_second_position] = exchange_first_value

        elif i[0] == 'p':
            partner = i[1:].strip()
            partner_first_program = partner.split('/')[0]
            partner_second_program = partner.split('/')[1]
            partner_first_position = programs.index(partner_first_program)
            partner_second_position = programs.index(partner_second_program)
            programs[partner_first_position] = partner_second_program
            programs[partner_second_position] = partner_first_program
    counter += 1

print ''.join(programs)

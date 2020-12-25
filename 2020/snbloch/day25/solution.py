card_public_key = 17115212
door_public_key = 3667832
subject_number = 7
divisor = 20201227

def loop(subject_number, value):
    return (value * subject_number) % divisor

def part1():
    card_value = 1
    card_loop_counter = 0
    while card_value != card_public_key:
        card_value = loop(subject_number, card_value)
        card_loop_counter += 1
    
    door_value = 1
    door_loop_counter = 0
    while door_value != door_public_key:
        door_value = loop(subject_number, door_value)
        door_loop_counter += 1
    
    encryption_key = 1
    for _ in range(card_loop_counter):
        encryption_key = loop(door_public_key, encryption_key)
    
    print(encryption_key)

if __name__ == '__main__':
    part1()
import io
from collections import Counter

position = []
velocity = []
acceleration = []
closest_particle = []

file = open('input.txt', 'r')
for i in file:
    p = i.split(', ')[0]
    v = i.split(', ')[1]
    a = i.split(', ')[2]
    p = str(p).replace('p=<', '').replace('>', '')
    p_list = []
    for j in p.split(','):
        p_list.append(int(j))
    position.append(p_list)
    v = str(v).replace('v=<', '').replace('>', '')
    v_list = []
    for j in v.split(','):
        v_list.append(int(j))
    velocity.append(v_list)
    a = str(a).replace('a=<', '').replace('>', '')
    a_list = []
    for j in a.split(','):
        a_list.append(int(j))
    acceleration.append(a_list)

iter_counter = 0
while iter_counter < 1000:
    particle_counter = 0
    closest = None
    min_distance = None
    while particle_counter < len(position):
        distance = abs(position[particle_counter][0]) + abs(position[particle_counter][1]) + abs(position[particle_counter][2])
        if min_distance == None:
            min_distance = distance
            closest = particle_counter
        elif distance < min_distance:
            min_distance = distance
            closest = particle_counter
        velocity[particle_counter][0] += acceleration[particle_counter][0]
        velocity[particle_counter][1] += acceleration[particle_counter][1]
        velocity[particle_counter][2] += acceleration[particle_counter][2]
        position[particle_counter][0] += velocity[particle_counter][0]
        position[particle_counter][1] += velocity[particle_counter][1]
        position[particle_counter][2] += velocity[particle_counter][2]
        particle_counter += 1
    closest_particle.append(closest)
    iter_counter += 1

print Counter(closest_particle)

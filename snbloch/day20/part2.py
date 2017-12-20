import io

position = []
velocity = []
acceleration = []

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

particles_to_remove = set()
iter_counter = 0
while iter_counter < 100:
    print 'Iteration: ', iter_counter
    particle_counter = 0
    while particle_counter < len(position):
        comparison_counter = 0
        while comparison_counter < len(position):
            if particle_counter == comparison_counter:
                pass
            else:
                if position[particle_counter][0] == position[comparison_counter][0] and position[particle_counter][1] == position[comparison_counter][1] and position[particle_counter][2] == position[comparison_counter][2]:
                    particles_to_remove.add(particle_counter)
                    particles_to_remove.add(comparison_counter)
            comparison_counter += 1
        velocity[particle_counter][0] += acceleration[particle_counter][0]
        velocity[particle_counter][1] += acceleration[particle_counter][1]
        velocity[particle_counter][2] += acceleration[particle_counter][2]
        position[particle_counter][0] += velocity[particle_counter][0]
        position[particle_counter][1] += velocity[particle_counter][1]
        position[particle_counter][2] += velocity[particle_counter][2]
        particle_counter += 1
    iter_counter += 1

print len(position) - len(particles_to_remove)

import io
import operator

def part1():
    steps = {}
    final_output = ''
    with open('input.txt', 'r') as inputfile:
        for line in inputfile:
            line = line.strip().split()
            if steps.get(line[1]) is None:
                steps[line[1]] = []
            if steps.get(line[7]) is None:
                steps[line[7]] = []
    with open('input.txt', 'r') as inputfile:
        for line in inputfile:
            line = line.strip().split()
            steps[line[7]].append(line[1])
    while len(steps) > 0:
        changed = False
        round_output = ''
        for i in steps.keys():
            if len(steps[i]) == 0 and changed == False:
                round_output += i
                for j in steps.keys():
                    if i in steps[j]:
                        steps[j].remove(i)
                del steps[i]
                changed = True
            else:
                for j in steps[i]:
                    if j in final_output:
                        steps[i].remove(j)
                        changed = True
        for i in sorted(round_output):
            final_output += i
    print 'Part 1:',final_output

def part2():
    constant = 60
    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    elf_count = 5
    elves = {}
    step_count = 0
    in_progress = []
    available = []
    steps = {}
    final_output = ''
    with open('input.txt', 'r') as inputfile:
        for line in inputfile:
            line = line.strip().split()
            if steps.get(line[1]) is None:
                steps[line[1]] = []
            if steps.get(line[7]) is None:
                steps[line[7]] = []
    with open('input.txt', 'r') as inputfile:
        for line in inputfile:
            line = line.strip().split()
            steps[line[7]].append(line[1])
    counter = 0
    while counter < elf_count:
        elves[counter] = ['', None]
        counter += 1
    print 'Part 2:'
    finished = False
    while finished == False:
        changed = False
        removed = False
        for i in steps.keys():
            if len(steps[i]) == 0 and i not in in_progress and i not in available:
                print 'Found',i,'available for processing.'
                available.append(i)
        for elf in elves:
            if elves[elf][1] == 0:
                done_processing = elves[elf][0]
                final_output += done_processing
                in_progress.remove(done_processing)
                elves[elf] = ['', None]
                for i in steps.keys():
                    if steps.get(i) is not None:
                        if done_processing in steps[i]:
                            steps[i].remove(done_processing)
                for i in steps.keys():
                    if steps.get(done_processing) is not None:
                        if len(steps[done_processing]) == 0:
                            del steps[done_processing]
                            print 'Deleting',done_processing,'from list of steps'
                removed = True
            elif elves[elf][1] > 0 and removed == False:
                elves[elf][1] -= 1
                changed = True
            if elves[elf][0] == '' and len(available) > 0:
                to_process = sorted(available)[0]
                elves[elf] = [to_process, constant + alpha.find(to_process) + 1]
                in_progress.append(to_process)
                available.remove(to_process)
                print 'Elf',elf,'is processing',to_process,'for',elves[elf][1],'seconds'
        if changed == True and removed == False:
            step_count += 1
        if len(steps) == 0 and len(available) == 0 and len(in_progress) == 0:
            finished = True

if __name__ == '__main__':
    part1()
    part2()

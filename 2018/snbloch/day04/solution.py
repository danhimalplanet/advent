import io, operator
from collections import Counter

def part1():
    timesheet = {}
    sleeps = []
    minutes_slept_by_guard = {}
    with open('input.txt', 'r') as inputfile:
        for line in inputfile:
            timestamp = line.strip().split(']')[0].replace('[', '')
            timesheet[timestamp] = line.strip().split(']')[1].strip()
    current_guard = None
    for i in sorted(timesheet):
        if 'begins shift' in timesheet[i]:
            current_guard = int(timesheet[i].replace('Guard #', '').replace(' begins shift', ''))
        if 'falls asleep' in timesheet[i]:
            minute = int(i.split(':')[1])
            sleeps.append((current_guard, minute))
        if 'wakes up' in timesheet[i]:
            minute = int(i.split(':')[1])
            sleeps.append((current_guard, minute))
    i = 0
    while i < len(sleeps) - 1:
        guard = sleeps[i][0]
        time_slept = sleeps[i + 1][1] - sleeps[i][1]
        if minutes_slept_by_guard.get(guard) is None:
            minutes_slept_by_guard[guard] = 0
        minutes_slept_by_guard[guard] += time_slept
        i += 2
    most_slept_guard = sorted(minutes_slept_by_guard.items(), key=operator.itemgetter(1), reverse=True)[0][0]
    specific_minute_slept = Counter()
    i = 0
    while i < len(sleeps) - 1:
        if sleeps[i][0] == most_slept_guard:
            start_minute = sleeps[i][1]
            end_minute = sleeps[i + 1][1] - 1
            j = start_minute
            while j <= end_minute:
                specific_minute_slept[j] += 1
                j += 1
        i += 2
    most_slept_minute = specific_minute_slept.most_common(1)[0][0]
    print 'Part 1: ID * minute =',most_slept_guard * most_slept_minute

def part2():
    timesheet = {}
    sleeps = []
    guards = {}
    with open('input.txt', 'r') as inputfile:
        for line in inputfile:
            timestamp = line.strip().split(']')[0].replace('[', '')
            timesheet[timestamp] = line.strip().split(']')[1].strip()
    current_guard = None
    for i in sorted(timesheet):
        if 'begins shift' in timesheet[i]:
            current_guard = int(timesheet[i].replace('Guard #', '').replace(' begins shift', ''))
        if 'falls asleep' in timesheet[i]:
            minute = int(i.split(':')[1])
            sleeps.append((current_guard, minute))
        if 'wakes up' in timesheet[i]:
            minute = int(i.split(':')[1])
            sleeps.append((current_guard, minute))
    i = 0
    while i < len(sleeps) - 1:
        specific_minute_slept = Counter()
        guard = sleeps[i][0]
        start_minute = sleeps[i][1]
        end_minute = sleeps[i + 1][1] - 1
        j = start_minute
        while j <= end_minute:
            specific_minute_slept[j] += 1
            j += 1
        i += 2
        for k in specific_minute_slept:
            if guards.get(guard) is None:
                guards[guard] = Counter()
            guards[guard][k] += specific_minute_slept[k]
    most_slept_frequency = 0
    for i in guards:
        if guards[i].most_common(1)[0][1] > most_slept_frequency:
            most_slept_frequency = guards[i].most_common(1)[0][1]
            most_slept_guard = i
    most_slept_minute = guards[most_slept_guard].most_common(1)[0][0]
    print 'Part 2: ID * minute =',most_slept_guard * most_slept_minute

if __name__ == '__main__':
    part1()
    part2()

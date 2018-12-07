#!/usr/bin/env python

from collections import defaultdict
from os.path import join
try:
    from string import ascii_uppercase as ucase
except ImportError:
    from string import uppercase as ucase


def deptree(lines):
    """Build a tree of what step depends on what other step(s).

    Test input becomes

    {'A': set(['C']), 'C': set([]), 'B': set(['A']),
     'E': set(['B', 'D', 'F']), 'D': set(['A']),
     'F': set(['C'])}

    A depends on C
    B depends on A
    C depends on nothing (starting point)
    D depends on A
    E depends on B, D, F
    F depends on C
    """

    coll = defaultdict(set)
    for line in lines:
        parts = line.split()
        coll[parts[7]].add(parts[1])
        if parts[1] not in coll:
            coll[parts[1]] = set()

    return dict(coll)


def removedeps(step, deps):
    """Remove a step.

    Since other steps might depend on it, once we're done with the
    step, we need to remove it from their dependencies.
    """

    maybenext = []

    del deps[step]
    for otherstep, deplist in deps.items():
        if step in deplist:
            deps[otherstep].remove(step)
            # if otherstep now has no dependencies, it's a
            # candidate for the next step to take
            if not deps[otherstep]:
                maybenext.append(otherstep)

    return maybenext


def order(deps):
    """Loop through deps in order.

    Using the test input:

    - find the steps that depends on nothing (just one in the beginning -- C)
    - sort this list of steps
    - store C (the first item) in retls, meaning we've "taken" the step
    - remove C from the deps dictionary
    - loop over other key/value pairs to find steps that depend on C
    - remove C from those values
    - at this point, some other step or steps will depend on nothing
      so loop back and operate on them
    - we know we're done when there is nothing left in deps
      at this point, return all the steps we've taken.
    """

    taken = []
    zerodeps = []
    for step, deplist in deps.items():
        if not deplist:
            zerodeps.append(step)

    while zerodeps:
        zerodeps.sort()
        step = zerodeps.pop(0)
        taken.append(step)
        zerodeps.extend(removedeps(step, deps))
        zerodeps = list(set(zerodeps))

    return "".join(taken)


def part1(deps):
    return order(deps)


def order2(deps, numworkers):
    """Multiple workers.

    Each worker is assigned a list with two items
    [step, time-in-seconds]

    When the time-in-seconds reaches zero, the worker has completed
    the step.

    On every loop, we subtract 1 second from every working worker's
    list.  Then we find steps that are completed, and mark the workers
    as free.

    If there are free workers, and steps to take, we assign workers
    steps.  If there are no steps to take, we know we're done.

    Return the time it took to complete all the steps.
    """

    workers = [None] * numworkers
    curtime = 0
    # keep track of which steps are being worked on
    working = set()

    # find initial list of steps to take (steps that depend on nothing)
    zerodeps = []
    for step, deplist in deps.items():
        if not deplist:
            zerodeps.append(step)

    while zerodeps:
        # each worker does one second of "work"
        for idx in range(numworkers):
            if workers[idx]:
                workers[idx][1] -= 1

        # loop over the list of workers, find free ones and
        # the ones that are done working
        freeworkers = []
        freeingworkers = []
        for idx, worker in enumerate(workers):
            if not worker:
                freeworkers.append(idx)
            elif worker[1] == 0:
                freeingworkers.append(idx)

        # free the ones that are done working on a step
        for idx in freeingworkers:
            step = workers[idx][0]
            # remove step from other steps' dependencies
            zerodeps.extend(removedeps(step, deps))
            # we're done with it, so forget it
            zerodeps.remove(step)
            # mark worker as idle
            workers[idx] = None
            freeworkers.append(idx)

        # if we have any free workers and steps we're not working on
        # assign the workers steps to perform
        if freeworkers:
            zerodeps = list(set(zerodeps))
            zerodeps.sort()

            # not efficient
            for idx in freeworkers:
                for step in zerodeps:
                    if step not in working:
                        workers[idx] = [step, ucase.index(step)+61]
                        working.add(step)
                        break

        # advance the clock
        curtime += 1

    return curtime-1


def part2(deps):
    return order2(deps, 5)


if __name__ == "__main__":
    INSTRUCTIONS = [instruction for instruction in open(join("resources", "input.txt"))]
    print(part1(deptree(INSTRUCTIONS)))
    print(part2(deptree(INSTRUCTIONS)))

# eof

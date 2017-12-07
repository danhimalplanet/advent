#!/usr/bin/env python

from collections import defaultdict
from pprint import pprint
import sys


def readinput(lines):
    weights = {}
    above = {}

    for line in lines:
        if line.find("->") == -1:
            program, weight = line.split()
            weight = int(weight.replace("(", "").replace(")", ""), 10)
            weights[program] = weight
            above[program] = []
        else:
            program, weight, _ignore, discs = line.split(" ", 3)
            weight = int(weight.replace("(", "").replace(")", ""), 10)
            weights[program] = weight
            above[program] = [disc.strip() for disc in discs.split(",")]

    return weights, above


def printtree(base, tree, weights, indent=0):
    subs = tree[base]
    if subs:
        print("%s %s (%d) ->" % (" " * indent, base, weights[base]))
    else:
        print("%s %s (%d)" % (" " * indent, base, weights[base]))
    for sub in subs:
        printtree(sub, tree, weights, indent + 2)


def maketree(weights, above):
    alldiscs = set(weights.keys())
    possiblebases = [base for base in above if above[base]]
    for base in possiblebases:
        seen = {base}
        tree = {base: {}}
        queue = [base]
        while queue:
            for disc in queue:
                queue.remove(disc)
                seen.add(disc)
                tree[disc] = above[disc]
                queue.extend(above[disc])
        if seen == alldiscs:
            # printtree(base, tree, weights)
            return tree, base


def one(base):
    return base


def two(weights, above, tree, base, diff=0):
    def sumweights(subtree):
        s = weights[subtree]
        for sub in tree[subtree]:
            s += sumweights(sub)
        return s

    wsub = defaultdict(list)
    for disc in tree[base]:
        wsub[sumweights(disc)].append(disc)

    # print(base, weights[base], wsub)
    if len(wsub) == 2:
        # something is heavier/lighter than the rest
        # make wsub[keys[0]] the unbalanced subtree root
        keys = wsub.keys()
        keys.sort(key=lambda k: len(wsub[k]))
        # print(keys)
        diff = keys[1] - keys[0]
        return two(weights, above, tree, wsub[keys[0]][0], diff)
    else:
        return weights[base] + diff


def main(args):
    weights, above = readinput((line.strip()
                                for line in open(args[0]).readlines()))
    tree, base = maketree(weights, above)

    print(one(base))
    print(two(weights, above, tree, base))


if __name__ == "__main__":
    main(sys.argv[1:])

# eof

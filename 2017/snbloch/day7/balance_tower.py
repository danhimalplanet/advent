import io

programs = []
counter = {}

# Find the bottom element of the tower
f = open('input.txt', mode='r')
for line in f:
    if '->' in line:
        programs.append(str(line.replace('->','|').split('|')[0]).strip())
f.close()

f = open('input.txt', mode='r')
for line in f:
    for prog in programs:
        if prog.split(' ')[0] in line:
            if counter.has_key(prog.split(' ')[0]):
                counter[prog.split(' ')[0]] += 1
            else:
                counter[prog.split(' ')[0]] = 1

for name, count in counter.iteritems():
    if count == 1:
        bottom = name
f.close()

weights = {}
tower_weights = {}
children = {}
parents = {}

# Read in the file again, populating dictionaries for weights, children, and parents of each node
f = open('input.txt', mode='r')
for line in f:
        line = line.strip().replace('->','|')
        name = line.split('|')[0].split(' ')[0]
        weights[name] = int(line.split('|')[0].split(' ')[1].replace('(','').replace(')',''))
        if '|' in line:
            children[name] = []
            for i in line.split('|')[1].split(', '):
                children[name].append(str(i).strip())
            for i in children[name]:
                parents[i] = name
f.close()

# Return a recursive weighting of the subtower from any position in the tree
def get_tower_weight(node):
    global children
    global weights
    global tower_weights
    tower_weights[node] = weights[node]
    if children.get(node) == None:
        return tower_weights[node]
    else:
        for i in children[node]:
            tower_weights[node] += get_tower_weight(i)
        return tower_weights[node]

unbalanced = True
cur_children = []
cur_parent = bottom

# Precompute the subtower weights for all positions in the tree
for i in weights:
    get_tower_weight(i)

while unbalanced == True:
    if children.get(cur_parent) != None:
        del cur_children[:]
        cur_child_weights = {}
        for j in children[cur_parent]:
            cur_children.append(j)
            cur_child_weights[j] = tower_weights[j]
        if len(set([tower_weights[c] for c in cur_children])) > 1:
            unbalanced_child_weights = []
            for child in cur_children:
                unbalanced_child_weights.append(cur_child_weights[child])
            for child_weight in unbalanced_child_weights:
                if unbalanced_child_weights.count(child_weight) == 1:
                    unbalanced_child_weight = child_weight
            for child, weight in cur_child_weights.iteritems():
                if weight == unbalanced_child_weight:
                    unbalanced_child = child
            cur_parent = unbalanced_child
        else:
            unbalanced = False

fix_weight = set(unbalanced_child_weights)
fix_weight.remove(tower_weights[unbalanced_child])
diff_weight = tower_weights[unbalanced_child] - list(fix_weight)[0]
fixed = weights[unbalanced_child] - diff_weight
print 'Fixed value to balance tower: ', fixed

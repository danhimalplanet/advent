from collections import defaultdict

class recipe:
    def __init__(self):
        self.ingredients = []
        self.allergens = []

def part1():
    recipe_list = []
    allergens_identified = []
    with open('input.txt') as inputfile:
        for line in inputfile:
            curr_recipe = recipe()
            for ing in line.strip().split(' (')[0].split():
                curr_recipe.ingredients.append(ing)
            for aller in line.strip().split('contains ')[1].split(')')[0].split(', '):
                curr_recipe.allergens.append(aller)
            recipe_list.append(curr_recipe)
    all_allergens = defaultdict(int)
    for r in recipe_list:
        for a in r.allergens:
            all_allergens[a] += 1
    while len(allergens_identified) < len(all_allergens):
        for a in all_allergens:
            usage = defaultdict(int)
            for r in recipe_list:
                if a in r.allergens:
                    for i in r.ingredients:
                        usage[i] += 1
            count = 0
            for i in usage:
                if usage[i] == all_allergens[a]:
                    count += 1
            if count == 1:
                for ing in usage:
                    if usage[ing] == all_allergens[a]:
                        allergens_identified.append((a, ing))
                        for r in recipe_list:
                            if ing in r.ingredients:
                                r.ingredients.remove(ing)
    total = 0
    for r in recipe_list:
        total += len(r.ingredients)
    print(total)

def part2():
    recipe_list = []
    allergens_identified = []
    with open('input.txt') as inputfile:
        for line in inputfile:
            curr_recipe = recipe()
            for ing in line.strip().split(' (')[0].split():
                curr_recipe.ingredients.append(ing)
            for aller in line.strip().split('contains ')[1].split(')')[0].split(', '):
                curr_recipe.allergens.append(aller)
            recipe_list.append(curr_recipe)
    all_allergens = defaultdict(int)
    for r in recipe_list:
        for a in r.allergens:
            all_allergens[a] += 1
    while len(allergens_identified) < len(all_allergens):
        for a in all_allergens:
            usage = defaultdict(int)
            for r in recipe_list:
                if a in r.allergens:
                    for i in r.ingredients:
                        usage[i] += 1
            count = 0
            for i in usage:
                if usage[i] == all_allergens[a]:
                    count += 1
            if count == 1:
                for ing in usage:
                    if usage[ing] == all_allergens[a]:
                        allergens_identified.append((a, ing))
                        for r in recipe_list:
                            if ing in r.ingredients:
                                r.ingredients.remove(ing)
    sorted_allergens = sorted(aller[0] for aller in allergens_identified)
    sorted_ingredients = []
    for a1 in sorted_allergens:
        for a2 in allergens_identified:
            if a2[0] == a1:
                sorted_ingredients.append(a2[1])
    print(','.join(sorted_ingredients))

if __name__ == '__main__':
    part1()
    part2()
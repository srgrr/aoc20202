import sys
from functools import reduce

recipes_list = []
recipes_with_sets = {}

with open(sys.argv[1], 'r') as f:
  line = f.readline().strip()
  while line:
    ingredients, allergens = line.replace(')', '').split('(')
    recipes_list.append(ingredients.split())
    for allergen in map(str.strip, allergens.replace('contains', '').split(',')):
      recipes_with_sets.setdefault(allergen, []).append(set(recipes_list[-1]))
    line = f.readline().strip()

# part 1
for allergen, sets in recipes_with_sets.items():
  recipes_with_sets[allergen] = reduce(set.intersection, sets)

changes = True

while changes:
  changes = False
  unambiguous_ingredients = set()
  for ig_set in recipes_with_sets.values():
    if len(ig_set) == 1:
      unambiguous_ingredients.add(list(ig_set)[0])
  for allergen, ig_set in recipes_with_sets.items():
    if len(ig_set) > 1:
      ig_list = list(ig_set)
      for ig in ig_list:
        if ig in unambiguous_ingredients:
          ig_set.remove(ig)
          changes = True

banned_ingredients = reduce(set.union, recipes_with_sets.values())

print(sum(len([x for x in recipe if x not in banned_ingredients]) for recipe in recipes_list))
# part 2
print(','.join(list(x[1])[0] for x in sorted([(a, ig) for a, ig in recipes_with_sets.items()], key=lambda x: x[0])))
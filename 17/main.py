import sys
from itertools import product
from collections import Counter


def get_next_state(cubes, ndim=3):
    active_neighbors = Counter()
    for c in cubes:
        for d in product([-1, 0, 1], repeat=ndim):
            active_neighbors[tuple(b + o for b, o in zip(c, d))] += 1
    next_state = set()
    for c in active_neighbors:
        adj = active_neighbors[c]
        if (c in cubes and adj in [3, 4]) or (c not in cubes and adj == 3):
            next_state.add(c)
    return next_state


grid = [x.strip() for x in open(sys.argv[1], 'r').readlines()]
ndim = int(sys.argv[2])

active_cubes = \
    set(
        [
            tuple([x, y] + [0] * (ndim - 2)) 
            for x,y in 
            product(range(len(grid)), range(len(grid[0]))) if grid[x][y] == '#'
        ]
    )

for _ in range(6):
    active_cubes = get_next_state(active_cubes, ndim)

print(len(active_cubes))

import sys
import numpy as np
from itertools import product
from collections import Counter


grid = [[x for x in line.strip()] for line in open(sys.argv[1]).readlines()]
part = int(sys.argv[2])


def next_cell_state(grid, i, j, p):
	if grid[i][j] != '.':
		cnt = Counter()
		for (di, dj) in product([-1, 0, 1], [-1, 0, 1]):
			if not (di == 0 and dj == 0):
				for k in range(1, max(len(grid), len(grid[0])) if p == 2 else 2):
					oi, oj = i + k * di, j + k * dj
					if oi >= 0 and oi < len(grid) and oj >= 0 and oj < len(grid[0]):
						if grid[oi][oj] != '.':
							cnt[grid[oi][oj]] += 1
							break
		if grid[i][j] == 'L':
			return '#' if cnt['#'] == 0 else 'L'
		else:
			return 'L' if cnt['#'] >= (5 if p == 2 else 4) else '#'
	return '.'


def compute_next(grid, p):
	new_grid = [
		[next_cell_state(grid, i, j, p) for j in range(len(grid[0]))]
		for i in range(len(grid))
	]
	return new_grid


new_grid = compute_next(grid, part)


while grid != new_grid:
	grid, new_grid = new_grid, compute_next(new_grid, part)


print(sum(x.count('#') for x in grid))
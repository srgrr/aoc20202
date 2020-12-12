import random as rng
import numpy as np
import sys

n, m = map(int, sys.argv[1:])

def get_char_map(i, j, n, m):
	norm_dist = (np.linalg.norm([i - n // 2, j - n // 2]) / (np.sqrt(n ** 2.0 + m ** 2.0)))
	return \
	rng.choice(['#', 'L']) if \
	norm_dist < rng.random() / 3.0 \
	else '.'

for i in range(n):
	print(''.join(get_char_map(i, j, n, m) for j in range(m)))
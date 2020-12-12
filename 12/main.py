import sys

dir_vecs = {
	'N': lambda v, k: [1, 0],
	'S': lambda v, k: [-1, 0],
	'E': lambda v, k: [0, 1],
	'W': lambda v, k: [0, -1],
	'F': lambda v, k: v,
	'R90': lambda v, k: [-v[1], v[0]],
	'R': lambda v, k: dir_vecs['R90'](v, k) if k == 90
						else dir_vecs['R'](dir_vecs['R90'](v, k), k - 90),
	'L': lambda v, k: dir_vecs['R'](v, 360 - k)
}

lines = [(x[0], int(x[1:])) for x in open(sys.argv[1]).readlines()]

pos = [0, 0]
direction = [0, 1]

for (op, val) in lines:
	dir_vec = dir_vecs[op](direction, val)
	if op not in ['L', 'R']:
		pos = [pos[0] + val * dir_vec[0], pos[1] + val * dir_vec[1]]
	else:
		direction = dir_vec

print(abs(pos[0]) + abs(pos[1]))
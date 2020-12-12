import sys

dir_vecs = {
	'N': lambda v, k: [v[0] + k, v[1]],
	'S': lambda v, k: [v[0] - k, v[1]],
	'E': lambda v, k: [v[0], v[1] + k],
	'W': lambda v, k: [v[0], v[1] - k],
	'F': lambda v, k: v,
	'R90': lambda v, k: [-v[1], v[0]],
	'R': lambda v, k: dir_vecs['R90'](v, k) if k == 90
						else dir_vecs['R'](dir_vecs['R90'](v, k), k - 90),
	'L': lambda v, k: dir_vecs['R'](v, 360 - k)
}

lines = [(x[0], int(x[1:])) for x in open(sys.argv[1]).readlines()]

pos = [0, 0]
direction = [1, 10]

for (op, val) in lines:
	if op == 'F':
		pos = [pos[0] + val * direction[0], pos[1] + val * direction[1]]
	else:
		direction = dir_vecs[op](direction, val)
	print(pos)

print(abs(pos[0]) + abs(pos[1]))
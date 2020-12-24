import sys
from itertools import product

offsets = {
  'e': [0, 2],
  'w': [0, -2],
  'ne': [1, 1],
  'nw': [1, -1],
  'se': [-1, 1],
  'sw': [-1, -1]
}

black_tiles = set()

# part 1
with open(sys.argv[1], 'r') as f:
  line = f.readline().strip()
  while line:
    r, i = (0, 0), 0
    while i < len(line):
      j = 1 if line[i] in ['e', 'w'] else 2
      o = offsets[line[i:i + j]]
      r = (r[0] + o[0], r[1] + o[1])
      i += j
    if r in black_tiles:
      black_tiles.remove(r)
    else:
      black_tiles.add(r)
    line = f.readline().strip()

print(len(black_tiles))

def count_black(s, b):
  return len([o for o in offsets.values() if (s[0] + o[0], s[1] + o[1]) in b])

# part 2
for _ in range(100):
  white_tiles = set()
  for black_tile, o in product(black_tiles, offsets.values()):
    adj_tile = (black_tile[0] + o[0], black_tile[1] + o[1])
    if adj_tile not in black_tiles:
      white_tiles.add(adj_tile)
  black_tiles_c = black_tiles.copy()
  for nb in black_tiles_c:
    if count_black(nb, black_tiles_c) not in [1, 2]:
      black_tiles.remove(nb)
  for w in white_tiles:
    if count_black(w, black_tiles_c) == 2:
      black_tiles.add(w)


print(len(black_tiles))
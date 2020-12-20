import sys
import re
from itertools import combinations, product
from copy import deepcopy
from random import shuffle

class Tile:

  def _build_identifiers(self):
    self.at, self.al, self.ab, self.ar = [None] * 4
    n, m = len(self.grid), len(self.grid[0])
    self.t = sum((self.grid[0][i] == '#') * (2 ** i) for i in range(m))
    self.l = sum((self.grid[i][0] == '#') * (2 ** i) for i in range(n))
    self.b = sum((self.grid[n - 1][i] == '#') * (2 ** i) for i in range(m))
    self.r = sum((self.grid[i][m - 1] == '#') * (2 ** i) for i in range(n))


  def __init__(self, id, grid):
    self.id = id
    self.grid = grid
    self.positioned = False
    self._build_identifiers()


  def horizontal_mirror(self):
    self.grid = [''.join(reversed(x)) for x in self.grid]
    self._build_identifiers()


  def vertical_mirror(self):
    self.grid = list(reversed(self.grid))
    self._build_identifiers()


  def rotate_right(self):
    self.grid = [''.join(x) for x in list(zip(*self.grid))[::-1]]
    self._build_identifiers()


  def is_valid(self):
    return not(self.at is None and self.ab is None) and not(self.ar is None and self.al is None)


  def match_left(self, other):
    if self.l == other.r:
      self.al = other
      other.ar = self


  def match_right(self, other):
    if self.r == other.l:
      self.ar = other
      other.al = self


  def match_top(self, other):
    if self.t == other.b:
      self.at = other
      other.ab = self


  def match_bottom(self, other):
    if self.b == other.t:
      self.ab = other
      other.at = self


  def match_with(self, other):
    self.match_left(other)
    self.match_right(other)
    self.match_top(other)
    self.match_bottom(other)


  def __str__(self):
    return f'{self.id}'


  def __hash__(self):
    return self.id


def transform(t, i):
  t.at, t.al, t.ab, t.ar = [None] * 4
  if i & 1:
    t.horizontal_mirror()
  if i & 2:
    t.vertical_mirror()


def rotate(t, i):
  t.at, t.al, t.ab, t.ar = [None] * 4
  for _ in range(i):
    t.rotate_right()


def grid_without_borders(g):
  return [''.join(x for x in g[i][1:len(g[0]) - 1]) for i in range(1, len(g) - 1)]


# Parse input
tiles = []

with open(sys.argv[1]) as f:
  line = f.readline().strip()
  while line:
    tile_id = int(re.match(r'Tile ([0-9]+):', line).groups()[0])
    grid = []
    line = f.readline().strip()
    while line:
      grid.append(line)
      line = f.readline().strip()
    line = f.readline().strip()
    tiles.append(Tile(tile_id, grid))

shuffle(tiles)

# Part 1
for t0_transf, t0_rot in product(range(4), repeat=2):
  tiles_c = deepcopy(tiles)
  transform(tiles_c[0], t0_transf)
  rotate(tiles_c[0], t0_rot)

  fixed = set([tiles_c[0]])

  remaining = set(tiles_c)
  remaining.remove(tiles_c[0])

  changes = True

  while changes:
    old_l = len(remaining)
    rf = None
    for f, r in product(fixed, remaining):
      for r_transf, r_rot in product(range(4), repeat=2):
        transform(r, r_transf)
        rotate(r, r_rot)
        f.match_with(r)
        if any([x == f for x in [r.at, r.al, r.ab, r.ar]]):
          rf = r
          break
        rotate(r, 4 - r_rot)
        transform(r, r_transf)
      if rf is not None:
        break
    if rf is not None:
      fixed.add(rf)
      remaining.remove(rf)
    changes = old_l != len(remaining)

  if len(fixed) == len(tiles):
    for f1, f2 in product(fixed, repeat=2):
      if f1.id != f2.id:
        f1.match_with(f2)
    top_left = [x for x in fixed if x.at is None and x.al is None][0]
    top_right = [x for x in fixed if x.at is None and x.ar is None][0]
    bottom_left = [x for x in fixed if x.ab is None and x.al is None][0]
    bottom_right = [x for x in fixed if x.ab is None and x.ar is None][0]
    print(top_left.id * top_right.id * bottom_left.id * bottom_right.id)
    break

# Part 2
current_node = top_left
first_in_row = top_left
current_row = []
mega_grid = []
while current_node is not None:
  current_row.append(grid_without_borders(current_node.grid))
  if current_node.ar is not None:
    current_node = current_node.ar
  else:
    for row in range(len(current_row[0])):
      mega_row = ''.join(g[row] for g in current_row)
      mega_grid.append(mega_row)
    current_node, first_in_row = first_in_row.ab, first_in_row.ab
    current_row = []

pattern = ["                  # ", "#    ##    ##    ###", " #  #  #  #  #  #   "]

for transf, rot in product(range(4), repeat=2):
  mega_tile = Tile(0xDEADBEEF, deepcopy(mega_grid))
  transform(mega_tile, transf)
  rotate(mega_tile, rot)
  ans = sum(x.count('#') for x in mega_tile.grid)
  inc = 0
  for i in range(0, len(mega_tile.grid) - len(pattern)):
    for j in range(0, len(mega_tile.grid[0]) - len(pattern[0])):
      all_match = True
      for ii, jj in product(range(len(pattern)), range(len(pattern[0]))):
        all_match = all_match and (pattern[ii][jj] != '#' or mega_tile.grid[i + ii][j + jj] == '#')
      if all_match:
        inc += sum(x.count('#') for x in pattern)
  if inc:
    print(ans - inc)

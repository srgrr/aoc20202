import sys
import re


answer = 0
mem = {}

with open(sys.argv[1]) as f:
  line = f.readline().strip()
  while line:
    mask = ''.join(reversed(line.split(' = ')[1]))
    line = f.readline().strip()  
    def is_mask_line(line):
      return line.startswith('mask =')
    while line and not is_mask_line(line):
      pos, num = map(int, re.match(r'mem\[([0-9]+)\] = ([0-9]+)', line).groups())
      mem[pos] = \
        sum(
          (int(mask[i]) << i) if mask[i] != 'X'
          else num & (1 << i) for i in range(36)
          )
      line = f.readline().strip()

print(sum(mem.values()))
import sys
import re


answer = 0
mem = {}


def write_mem(addr_mask, current_bit, pos, num):
  if current_bit == len(addr_mask):
    mem[pos] = num
  else:
    if addr_mask[current_bit] != 2:
      write_mem(
        addr_mask,
        current_bit + 1,
        pos | (addr_mask[current_bit] << current_bit),
        num
      )
    else:
      write_mem(addr_mask, current_bit + 1, pos, num)
      write_mem(addr_mask, current_bit + 1, pos | (1 << current_bit), num)


with open(sys.argv[1]) as f:
  line = f.readline().strip()
  while line:
    mask = ''.join(reversed(line.split(' = ')[1]))
    line = f.readline().strip()  
    def is_mask_line(line):
      return line.startswith('mask =')
    while line and not is_mask_line(line):
      pos, num = \
        map(
          int,
          re.match(r'mem\[([0-9]+)\] = ([0-9]+)', line).groups()
        )
      def bit(n, i):
        return 1 if n & (1 << i) else 0
      addr_mask = \
        [
          bit(pos, i) if mask[i] == '0'
            else 1 if mask[i] == '1'
              else 2
          for i in range(36)
        ]
      write_mem(addr_mask, 0, 0, num)
      line = f.readline().strip()

print(mem)

print(len(mem.keys()))
print(sum(mem.values()))
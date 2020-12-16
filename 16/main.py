import re
import sys
from functools import reduce

def read_blank_lines(f, r=1):
  for _ in range(r):
    f.readline()


def field_suits_ticket(x, ticket_intervals):
  i1, i2 = ticket_intervals
  return (i1[0] <= x <= i1[1]) or (i2[0] <= x <= i2[1])


fields = {}

with open(sys.argv[1]) as f:
  line = f.readline().strip()
  while line:
    field, i1, i2, i3, i4 = \
      re.match(r'([^:]*): ([0-9]+)-([0-9]+) or ([0-9]+)-([0-9]+)', line).groups()
    fields[field] = ((int(i1), int(i2)), (int(i3), int(i4)))
    line = f.readline().strip()
  read_blank_lines(f, 1)
  my_ticket = list(map(int, f.readline().strip().split(',')))
  read_blank_lines(f, 2)
  line = f.readline()
  other_tickets = []
  while line:
    other_tickets.append(list(map(int, line.split(','))))
    line = f.readline().strip()

valid_tickets = []

# part 1
ans = 0
for ticket in other_tickets:
  invalid_rate = \
    sum([x for x in ticket if not any([field_suits_ticket(x, intervals) for intervals in fields.values()])])
  if invalid_rate == 0:
    valid_tickets.append(ticket)
  ans += invalid_rate

print(ans)

# part 2
valid_indices = {name: set() for name in fields.keys()}
for field in fields:
  for index in range(len(my_ticket)):
    all_suit = all(field_suits_ticket(ticket[index], fields[field]) for ticket in valid_tickets)
    if all_suit:
      valid_indices[field].add(index)

final_indices = {}

while valid_indices:
  final_pair = [(name, indices) for (name, indices) in valid_indices.items() if len(indices) == 1][0]
  name, index = final_pair[0], final_pair[1].pop()
  final_indices[name] = index
  valid_indices.pop(name)
  for (k, v) in valid_indices.items():
    if index in v:
      valid_indices[k].remove(index)

print(reduce(int.__mul__, [my_ticket[index] for name, index in final_indices.items() if name.startswith('departure')]))

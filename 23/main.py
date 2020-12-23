import sys

class Node(object):
  def __init__(self, value):
    self.value = value
    self.prev_in_list, self.next_in_list, self.prev_in_val = None, None, None

  def __eq__(self, other):
    return self.value == other.value

  def __str__(self):
    return str(self.value)

  def __hash__(self):
    return self.value



def move(start_point):
  current_cup = start_point
  picked_cups = \
    [
      start_point.next_in_list,
      start_point.next_in_list.next_in_list,
      start_point.next_in_list.next_in_list.next_in_list
    ]

  next_to_picked = picked_cups[-1].next_in_list
  prev_cup = current_cup.prev_in_val
  while prev_cup in picked_cups:
    prev_cup = prev_cup.prev_in_val

  current_cup.next_in_list = next_to_picked
  next_to_picked.prev_in_list = current_cup

  next_to_prev = prev_cup.next_in_list

  prev_cup.next_in_list = picked_cups[0]
  picked_cups[0].prev_in_list = prev_cup

  next_to_prev.prev_in_list = picked_cups[-1]
  picked_cups[-1].next_in_list = next_to_prev


  return next_to_picked

def print_ring(start_point, list_len):
  root = start_point
  list_to_print = []
  for _ in range(list_len):
    list_to_print.append(root.value)
    root = root.next_in_list
  print(list_to_print)

cups = [x for x in map(int, [x for x in open(sys.argv[1], 'r').readline().strip()])]
if sys.argv[2] == '2':
  cups += list(range(len(cups) + 1, 1000001))

nodes = [Node(c) for c in cups]

nodes_with_val = {v.value: i for (i, v) in enumerate(nodes)}

for i in range(len(nodes)):
  prev_ind = (i - 1) % len(nodes)
  next_ind = (i + 1) % len(nodes)
  prev_val = ((nodes[i].value - 2) % len(nodes)) + 1
  nodes[i].prev_in_list = nodes[prev_ind]
  nodes[i].next_in_list = nodes[next_ind]
  nodes[i].prev_in_val = nodes[nodes_with_val[prev_val]]

start_point = nodes[0]

if sys.argv[2] == '1':
  print_ring(start_point, len(nodes))

for _ in range(10 if sys.argv[2] == '1' else 10000000):
  start_point = move(start_point)

if sys.argv[2] == '1':
  print_ring(start_point, len(nodes))

node_with_1 = [x for x in nodes if x.value == 1][0]

print(node_with_1.next_in_list.value * node_with_1.next_in_list.next_in_list.value)

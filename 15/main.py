import sys

def main(until):
  nums = list(map(int, input().split(',')))

  turns = {}

  for i, num in enumerate(nums):
    turns.setdefault(num, []).append(i + 1)

  last_num, num_count = nums[-1], len(nums)

  while num_count < until:
    new_num = \
      num_count - turns[last_num][-2] if len(turns[last_num]) > 1 else 0
    num_count += 1
    turns.setdefault(new_num, []).append(num_count)
    if len(turns[new_num]) > 2:
      turns[new_num] = turns[new_num][-2:]
    last_num = new_num

  print(last_num)


if __name__ == '__main__':
  main(int(sys.argv[1]))
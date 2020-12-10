import sys

nums = list(sorted([int(x.strip()) for x in open(sys.argv[1]).readlines()]))

# parte 1
d = [nums[i] - nums[i - 1] for i in range(1, len(nums))]

print((d.count(1) + 1) * (d.count(3) + 1))

# parte 2
s = set(nums)
n = max(nums) + 4
# ponemos las dos puntas en la lista
s.add(0)
s.add(n - 1)

ways = [0] * (max(nums) + 4)
ways[-1] = 1

for i in range(n - 2, -1, -1):
	if i in s:
		ways[i] = ways[i + 1] + ways[i + 2] + ways[i + 3]

print(ways[0])
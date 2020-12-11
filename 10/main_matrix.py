import sys
import numpy as np

nums = list(sorted([int(x.strip()) for x in open(sys.argv[1]).readlines()]))

# parte 1
d = [nums[i] - nums[i - 1] for i in range(1, len(nums))]

print((d.count(1) + 1) * (d.count(3) + 1))

# parte 2
nums = [0] + nums + [max(nums) + 3]
n = len(nums)
m = np.zeros((n, n), dtype=np.uint64)

for i in range(n - 1):
	for j in range(i + 1, min(n, i + 4)):
		m[i, j] = nums[j] - nums[i] <= 3

print(sum(np.linalg.matrix_power(m, i)[0, n - 1] for i in range(n)))

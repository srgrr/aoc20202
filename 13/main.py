from functools import reduce
min_t = int(input())
bus_schedule = input().split(',')
timestamps = [int(x) for x in bus_schedule if x != 'x']
indices = [i for i, x in enumerate(bus_schedule) if x != 'x']

# Part 1
for i in range(min_t, min_t + max(timestamps) + 1):
	l = [k for k in timestamps if i % k == 0]
	if l: print(l[0] * (i - min_t)); break

# Part 2
remainders = [t - i for t, i in zip(timestamps, indices)]
N = reduce(int.__mul__, timestamps)
y = [N // t for t in timestamps]
z = [pow(r, t - 2, t) for r, t in zip(y, timestamps)]
print(sum([ri * yi * zi for ri, yi, zi in zip(remainders, y, z)]) % N)

min_t = int(input())
bus_schedule = list(reversed([(i, int(x)) for (i, x) in enumerate(input().split(',')) if x != 'x']))
indices, timestamps = map(list, zip(*bus_schedule))

# Part 1
for i in range(min_t, min_t + max(timestamps) + 1):
	l = [k for k in timestamps if i % k == 0]
	if l: print(l[0] * (i - min_t)); break

# Part 2
# pos = 1 para evitar dar el 0 por bueno
pos, leap = 1, 1
while indices:
  t, k = timestamps.pop(), indices.pop()
  while (pos % t) != ((t - k) % t):
    pos += leap
  leap *= t

print(pos)
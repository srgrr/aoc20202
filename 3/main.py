g = [x[:-1] for x in open('input.txt').readlines()]

c = 0
r = 0

cnt = 0

while r < len(g):
    cnt += g[r][c] == '#'
    c += 3
    c %= len(g[0])
    r += 1

print(cnt)

g = [x[:-1] for x in open('input.txt').readlines()]

slopes = [
    [1, 1],
    [3, 1],
    [5, 1],
    [7, 1],
    [1, 2]
]

prod = 1

for (oc, oi) in slopes:
    c, r, t = 0, 0, 0
    while r != len(g) - 1:
        t += g[r][c] == '#'
        c = (c + oc) % len(g[0])
        r = (r + oi) % len(g) 
    print(f'Slope ({oc},{oi}) contains {t} trees')
    prod *= t

print(prod)

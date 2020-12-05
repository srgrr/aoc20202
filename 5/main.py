def get_id(ident, space_size, l_id, r_id):
    l, r = 0, space_size
    for part in ident:
        h = (l + r + 1) // 2
        if part == l_id:
            r = h - 1
        else:
            l = h
    return l


highest_id = 0

for line in open('input.txt', 'r').readlines():
    row = get_id(line[:7], 127, 'F', 'B')
    col = get_id(line[7:-1], 7, 'L', 'R')
    highest_id = max(highest_id, row * 8 + col)

print(highest_id)

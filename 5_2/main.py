def get_id(ident, space_size, l_id, r_id):
    l, r = 0, space_size
    for part in ident:
        h = (l + r + 1) // 2
        if part == l_id:
            r = h - 1
        else:
            l = h
    return l


seat_ids = set([])


for line in open('input.txt', 'r').readlines():
    row = get_id(line[:7], 127, 'F', 'B')
    col = get_id(line[7:-1], 7, 'L', 'R')
    seat_ids.add(row * 8 + col)


for i in range(1000):
    if (i - 1 in seat_ids) and (not i in seat_ids) and (i + 1 in seat_ids):
        print(i)

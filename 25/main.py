import sys
from itertools import dropwhile, count

p1, p2 = map(int, [x.strip() for x in open(sys.argv[1], 'r').readlines()])

s = (pow(7, p1 * p2, 20201227) * pow(7, 20201227 - 2, 20201227)) % 20201227

print(s)

l = next(dropwhile(lambda x: pow(7, x, 20201227) != p1, count()))
print(pow(p2, l , 20201227))
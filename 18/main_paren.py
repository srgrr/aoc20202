import sys

for line in open(sys.argv[1]).readlines():
  print(eval('(' + line.strip().replace('*', ')*(') + ')'))
import re
regex = re.compile(r'([0-9]+)-([0-9]+) ([a-z]): ([a-z]+)')

total_number = 0

for line in open('input.txt', 'r').readlines():
    match = re.match(regex, line)
    at_least, at_most, criteria_char, password = \
        [match.group(i) for i in range(1, 5)]
    occurences = password.count(criteria_char)
    if occurences >= int(at_least) and occurences <= int(at_most):
        total_number += 1

print(total_number)

import re
regex = re.compile(r'([0-9]+)-([0-9]+) ([a-z]): ([a-z]+)')

total_number = 0

for line in open('input.txt', 'r').readlines():
    match = re.match(regex, line)
    pos_1, pos_2, criteria_char, password = \
        [match.group(i) for i in range(1, 5)]
    occurences = password.count(criteria_char)
    if (password[int(pos_1) - 1] == criteria_char) ^ (password[int(pos_2) - 1] == criteria_char):
        total_number += 1

print(total_number)

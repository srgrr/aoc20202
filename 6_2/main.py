import re
import string

blank_regex = re.compile(r'(?:\n){2,}')

groups = re.split(blank_regex, open('sample.txt', 'r').read().strip())

answer = \
sum(
  len(
      [
        x for x in string.ascii_lowercase
        if all(x in member for member in group.split('\n'))
      ]
    )
    for group in groups
)

print(answer)

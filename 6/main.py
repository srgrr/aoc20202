import re
import string

blank_regex = re.compile(r'(?:\n){2,}')

groups = [
  x.replace('\n', '')
  for x in re.split(
    blank_regex,
    open('sample.txt', 'r').read().strip()
  )
]

answer = sum(len(set(group)) for group in groups)

print(answer)

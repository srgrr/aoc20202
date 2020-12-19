import re
import sys
from itertools import combinations

rules = {}


def matches(line, rule, l, r, dp):
  subp = (rule, l, r)
  if subp in dp:
    return dp[subp]
  if isinstance(rules[rule], str):
    return l == r and rules[rule] == line[l]
  dp[subp] = False
  for branch in rules[rule]:
    comb_gen = \
      combinations(range(l, r), len(branch) - 1) if len(branch) > 1 else [[]]
    for k in comb_gen:
      splitters = [l - 1] + list(k) + [r]
      rec = \
        all(matches(line, branch[i], splitters[i] + 1, splitters[i + 1], dp) for i in range(len(branch)))
      dp[subp] = dp[subp] or rec
  return dp[subp]


with open(sys.argv[1], 'r') as f:
  line = f.readline().strip()
  while line:
    rule_id, rule_body = map(str.strip, line.split(':'))
    terminal_m = re.match(r'"([a-z])"', rule_body)
    if terminal_m:
      rules[int(rule_id)] = terminal_m.groups()[0]
    else:
      for branching_rule in rule_body.split(' | '):
        rules.setdefault(int(rule_id), []).append(list(map(int, branching_rule.strip().split(' '))))
    line = f.readline().strip()

  line = f.readline().strip()
  total = 0

  while line:
    dp = {}
    if matches(line, 0, 0, len(line) - 1, dp):
      total += 1
      print(line)
    line = f.readline().strip()
  print(total)
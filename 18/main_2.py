import sys
from functools import reduce


def _update_mul_stack(mul_stack, val, oper):
  if oper is None or oper == '*':
    mul_stack.append(val)
  else:
    mul_stack[-1] += val


def _eval_expr(line, i):
  mul_stack, oper = [], None
  while i < len(line) and line[i] != ')':
    current_char = line[i]
    if current_char.isdigit():
      val = int(current_char)
      _update_mul_stack(mul_stack, val, oper)
    elif current_char in ['+', '*']:
      oper = current_char
    else:
      val, new_i = _eval_expr(line, i + 1)
      _update_mul_stack(mul_stack, val, oper)
      i = new_i
    i += 1
  retval = reduce(int.__mul__, mul_stack)
  return retval, i


def eval_expr(line):
  return _eval_expr(line, 0)


print(sum(eval_expr('(' + line.strip().replace(' ', '') + ')')[0] for line in open(sys.argv[1]).readlines()))


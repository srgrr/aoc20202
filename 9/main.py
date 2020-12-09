from itertools import combinations
nums = [int(x.strip()) for x in open('input.txt').readlines()]

# part 1
sums = {}
for i, j in combinations(range(25), 2):
  if nums[i] != nums[j]:
    sums.setdefault(nums[i] + nums[j], set()).add(i)


for i in range(25, len(nums)):
  val = nums[i]
  if val not in sums.keys():
    p1_answer = val
  for j in range(i - 24, i):
    # remove no longer valid sums
    a, b = nums[i - 25], nums[j]
    if a != b:
      s = a + b
      sums[s].remove(i - 25)
      if not sums[s]:
        sums.pop(s)
    # add the new valid ones
    if b != val:
      s = b + val
      sums.setdefault(s, set()).add(j)

print(p1_answer)

# part 2
s = nums[0] + nums[1]
i, j, n = 0, 1, len(nums)
while i < n:
  while j < n and s < p1_answer:
    j += 1
    s += nums[j]
  if s == p1_answer:
    val_range = nums[i : j + 1]
    print(min(val_range) + max(val_range))
    break
  if i < j - 1 and s > p1_answer:
    s -= nums[i]
    i += 1
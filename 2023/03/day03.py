#!/usr/bin/env python3
import sys
from functools import reduce
from operator import mul

lines = [l.rstrip('\n') for l in sys.stdin.readlines()]
n_rows = len(lines)
n_cols = len(lines[0])

char = lambda r, c: lines[r][c] if r >= 0 and r < n_rows and c >= 0 and c < n_cols else '.'
is_symbol = lambda s: not s.isnumeric() and s != '.'
neighbours = lambda r, c: [(r+dr,c+dc) for dr, dc in [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]]

numbers = []
num_pos = []

cur_n = []
cur_p = []

for r in range(n_rows):
  for c in range(n_cols):
    s = char(r, c)
    if s.isnumeric():
      cur_n.append(s)
      cur_p.append((r,c,))
    else:
      if cur_n:
        numbers.append(cur_n)
        num_pos.append(cur_p)
      cur_n = []
      cur_p = []
  if cur_n:
    numbers.append(cur_n)
    num_pos.append(cur_p)
  cur_n = []
  cur_p = []

numbers = [int(''.join(n)) for n in numbers]

part_numbers = []
for i, n in enumerate(numbers):
  if any(any(is_symbol(char(*q)) for q in neighbours(*p)) for p in num_pos[i]):
    part_numbers.append(n)

print("Sum of part numbers:", sum(part_numbers))

part_digits = {}
for i, n in enumerate(numbers):
  for p in num_pos[i]:
    part_digits[p] = n

gear_ratios = []

for r in range(n_rows):
  for c in range(n_cols):
    if char(r, c) == '*':
      gear_ratios.append({part_digits[p] for p in neighbours(r, c) if p in part_digits})

gear_ratios = [reduce(mul, gr) for gr in gear_ratios if len(gr) == 2]
print("Sum of gear ratios:", sum(gear_ratios))

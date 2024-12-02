#!/usr/bin/env python3
import sys
from functools import reduce
from operator import mul

lines = [l.rstrip('\n') for l in sys.stdin.readlines()]

games = {}

for l in lines:
  g, sets = l.split(': ')
  g_id = int(g.split(' ')[1])
  sets = sets.split('; ')
  sets = [{c.split(' ')[1]: int(c.split(' ')[0]) for c in s.split(', ')} for s in sets]
  games[g_id] = sets

for g in games:
  print("Game", g, ":", games[g])
print()

bag = {'red': 12, 'green': 13, 'blue': 14}
possible = [g for g in games if all(all(s[c] <= bag[c] for c in s) for s in games[g])]
print("Sum possible:", sum(possible))
print()

bag_max = lambda b1, b2: {c: max(b1[c], b2[c] if c in b2 else 0) for c in b1}

min_bags = {g: reduce(bag_max, games[g], {'red': 0, 'green': 0, 'blue': 0}) for g in games}
for g in min_bags:
  print("Game",g,":", min_bags[g], reduce(mul, min_bags[g].values()))
print()

print("Sum powers:", sum(reduce(mul, min_bags[g].values()) for g in min_bags))

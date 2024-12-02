#!/usr/bin/env python3
import sys
from collections import defaultdict

lines = [l.rstrip('\n') for l in sys.stdin.readlines()]

seeds = [int(s) for s in lines.pop(0).split(': ')[1].split(' ')]
maps = defaultdict(list)
m = ''
for l in lines:
  if not l.strip(' '):
    continue
  if l.endswith('map:'):
    m = l.split(' ')[0]
  else:
    d, s, r = map(int, l.split(' '))
    maps[m].append((d,s,r,))
for m in maps:
  maps[m].sort(key=lambda t: t[1]) # Sort by increasing source id

map_list = ['seed', 'soil', 'fertilizer', 'water', 'light', 'temperature', 'humidity', 'location']

def convert(m, x):
  for d, s, r in maps[m]:
    if s > x:
      break
    if s <= x and x < s+r:
      return d + x - s
  return x

locations = []
for seed in seeds:
  y = seed
  for i in range(1, len(map_list)):
    y = convert('{}-to-{}'.format(map_list[i-1],map_list[i]), y)
  locations.append(y)

locations.sort()
print("\nLowest location:", locations[0])

ranges = defaultdict(set)
ranges['seed'] = {(seeds[i], seeds[i] + seeds[i+1] - 1) for i in range(0, len(seeds), 2)}

def convert_range(m, x, y):
  spans = set()
  cur_x = x
  for d, s, r in m:
    if cur_x > y or s > y:
      break
    if cur_x >= s + r:
      continue
    if cur_x < s:
      spans.add((cur_x, s-1,)) # Non-overlapping
      cur_x = s
    right = min(y, s + r - 1)
    spans.add((d + cur_x - s, d + right - s,))
    cur_x = right + 1
  if cur_x <= y:
    spans.add((cur_x, y,))
  return spans

for i in range(1, len(map_list)):
  m = maps['{}-to-{}'.format(map_list[i-1], map_list[i])]
  for x, y in ranges[map_list[i-1]]:
    ranges[map_list[i]] = ranges[map_list[i]].union(convert_range(m, x, y))

print("\nLowest location:", min(ranges['location'], key=lambda r: r[0])[0])

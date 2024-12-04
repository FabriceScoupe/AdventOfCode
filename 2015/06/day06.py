#!/usr/bin/env python3
import re
import sys

lines = [l.rstrip('\n') for l in sys.stdin.readlines()]

p = re.compile(r'(turn off|turn on|toggle) (\d+),(\d+) through (\d+),(\d+)')

cmds = map(lambda l:p.match(l).groups(), lines)

def do1(g, op, x1, y1, x2, y2):
  x1, y1, x2, y2 = map(int, [x1, y1, x2, y2])
  print(op, x1, y1, x2, y2)
  for x in range(x1, x2+1):
    for y in range(y1, y2+1):
      if op == 'turn on':
        g[x][y] = 1
      elif op == 'turn off':
        g[x][y] = 0
      else:
        g[x][y] = 1 - g[x][y]
  return g

def do2(g, op, x1, y1, x2, y2):
  x1, y1, x2, y2 = map(int, [x1, y1, x2, y2])
  print(op, x1, y1, x2, y2)
  for x in range(x1, x2+1):
    for y in range(y1, y2+1):
      if op == 'turn on':
        g[x][y] += 1
      elif op == 'turn off':
        g[x][y] = g[x][y]-1 if g[x][y] > 1 else 0
      else:
        g[x][y] += 2
  return g

grid1 = [[0 for _ in range(1000)] for _ in range(1000)]
grid2 = [[0 for _ in range(1000)] for _ in range(1000)]
for c in cmds:
  grid1 = do1(grid1, *c)
  grid2 = do2(grid2, *c)

print("Lights on (1):", sum(sum(r) for r in grid1))
print("Lights on (2):", sum(sum(r) for r in grid2))

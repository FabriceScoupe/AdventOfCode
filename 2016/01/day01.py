#!/usr/bin/env python3
import sys

lines = [l.rstrip('\n') for l in sys.stdin.readlines()]
steps = lines[0].split(', ')
d = 1j
moves = [int(s[1:])*(d:=d*(1j if s[0]=='L' else -1j)) for s in steps]
manh = lambda z: abs(z.real)+abs(z.imag)
print("Blocks:", manh(sum(moves)))
z = 0
d = 1j
seen = {0}
found = False
while not found and steps:
  s = steps.pop(0)
  d *= 1j if s[0]=='L' else -1j
  for _ in range(1, int(s[1:])+1):
    z += d
    if z in seen:
      print("Visited twice:", z, manh(z))
      found = True
      break
    seen.add(z)

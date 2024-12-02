#!/usr/bin/env python3
import sys

lines = [l.rstrip('\n') for l in sys.stdin.readlines()]

floor = 0
for c in lines[0]:
  floor += 1 if c == '(' else -1

print("Floor:", floor)

floor = 0
for i, c in enumerate(lines[0]):
  floor += 1 if c == '(' else -1
  if floor < 0:
    print("Position:", i+1)
    break

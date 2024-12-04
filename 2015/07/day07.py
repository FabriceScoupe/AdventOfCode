#!/usr/bin/env python3
import sys
from collections import defaultdict
from operator import and_, or_, rshift, lshift

lines = [l.rstrip('\n') for l in sys.stdin.readlines()]

commands = [l.split(' -> ') for l in lines]
commands = [(c[0].split(' '), c[1]) for c in commands]

ops = { 'AND': and_, 'OR': or_, 'RSHIFT': rshift, 'LSHIFT': lshift }

def signals(src_cmds):
  signs = {}
  cmds = list(src_cmds)
  while cmds:
    c = cmds.pop(0)
    expr, res = c
    if any(e.islower() and e not in signs for e in expr):
        cmds.append(c)
        continue
    expr = list(map(lambda e: int(e) if e.isnumeric() else signs[e] if e.islower() else e, expr))
    if len(expr) == 1: # ... ->
      signs[res] = expr[0]
    elif len(expr) == 2: # NOT ... ->
      signs[res] = (~expr[1]) % 65536
    else:
      signs[res] = (ops[expr[1]](expr[0], expr[2])) % 65536
  return signs

s = signals(commands)
print("Part 1:", s['a'] if 'a' in s else s)
commands = [([str(s['a'])], 'b') if c[1] == 'b' else c for c in commands]
s = signals(commands)
print("Part 2:", s['a'])

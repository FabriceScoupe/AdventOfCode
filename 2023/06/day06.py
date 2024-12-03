#!/usr/bin/env python3
import sys
from functools import reduce
from operator import mul
from math import sqrt, floor, ceil

lines = [l.rstrip('\n') for l in sys.stdin.readlines()]

times = [int(t) for t in lines[0].split(':')[1].split(' ') if t.strip(' ')]
dists = [int(d) for d in lines[1].split(':')[1].split(' ') if d.strip(' ')]

raced = [[h*(t-h) for h in range(t+1)] for t in times]

wins = [sum(r > dists[i] for r in raced[i]) for i in range(len(raced))]
print("\nNumber of ways to win:", reduce(mul, wins))

t = int(''.join(n for n in lines[0].split(':')[1].split(' ') if n.strip(' ')))
d = int(''.join(n for n in lines[1].split(':')[1].split(' ') if n.strip(' ')))

delta = t*t - 4*d
r1 = (t - sqrt(delta))/2.0
r2 = (t + sqrt(delta))/2.0

print("\nTo win: floor({})-ceil({})+1 = {}".format(r1, r2, floor(r2) - ceil(r1) + 1))



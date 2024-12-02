#!/usr/bin/env python3
import sys

lines = [l.rstrip('\n') for l in sys.stdin.readlines()]

presents = [tuple(map(int, l.split('x'))) for l in lines]
#print(presents)

def wrapping(p):
  a, b, c = sorted(p)
  return 3*a*b + 2*b*c + 2*a*c

print("Total wrapping:", sum(wrapping(p) for p in presents))

def ribbon(p):
  a, b, c = sorted(p)
  return a*b*c + 2*a + 2*b

print("Total ribbon:", sum(ribbon(p) for p in presents))

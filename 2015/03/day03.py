#!/usr/bin/env python3
import sys

lines = [l.rstrip('\n') for l in sys.stdin.readlines()]

z = 0
dirs = {'^':1j, 'v':-1j, '<':-1, '>': 1}
print("Number of houses:", len({(z := z + dirs[c]) for c in lines[0]}))
z1 = z2 = 0
print("Number of houses:", len({(z1:=z1+dirs[c]) for c in lines[0][::2]}|{(z2:=z2+dirs[c]) for c in lines[0][1::2]}))

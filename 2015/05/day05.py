#!/usr/bin/env python3
import re
import sys

lines = [l.rstrip('\n') for l in sys.stdin.readlines()]

p1 = re.compile(r'[aeiou]')
p2 = re.compile(r'(.)\1')
p3 = re.compile(r'ab|cd|pq|xy')

nice = [l for l in lines if len(p1.findall(l)) >= 3 and p2.findall(l) and not p3.findall(l)]
print("Nice:", len(nice))

p1 = re.compile(r'(..).*\1')
p2 = re.compile(r'(.).\1')

nice = [l for l in lines if p1.findall(l) and p2.findall(l)]
print("Nice:", len(nice))

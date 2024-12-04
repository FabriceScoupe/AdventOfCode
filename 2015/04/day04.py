#!/usr/bin/env python3
from hashlib import md5
from itertools import count
import sys

lines = [l.rstrip('\n') for l in sys.stdin.readlines()]
start = lines[0]

def find(s, p):
  for c in count(1):
    h = md5(bytes(f"{s}{c}", "utf-8")).hexdigest()
    if h.startswith(p):
      return c

print(find(start, '00000'))
print(find(start, '000000'))

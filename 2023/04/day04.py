#!/usr/bin/env python3
import sys

lines = [l.rstrip('\n') for l in sys.stdin.readlines()]

cards = []

for l in lines:
  l = l.split(': ')[1]
  winning, numbers = l.split('| ')
  winning = {w for w in winning.split(' ') if w}
  numbers = {n for n in numbers.split(' ') if n}
  cards.append((winning, numbers,))

matching = [len(w.intersection(n)) for w, n in cards]

print("Points:", sum(2**(m-1) if m else 0 for m in matching))

instances = [1 for c in cards]

for i, m in enumerate(matching):
  for p in range(m):
    instances[i+p+1] += instances[i]

print("Total scratchcards:", sum(instances))

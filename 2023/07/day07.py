#!/usr/bin/env python3
import sys
from collections import Counter
from functools import reduce
from operator import itemgetter

lines = [l.rstrip('\n') for l in sys.stdin.readlines()]

bids = {l.split(' ')[0]: int(l.split(' ')[1]) for l in lines}

cards = {c: i for i, c in enumerate('23456789TJQKA')}

def convert(h):
  m = tuple(map(itemgetter(1), Counter(h).most_common()))
  return (m, tuple(cards[c] for c in h))

hands = sorted(bids.keys(), key=convert)

print("\nTotal winnings:", sum((i+1)*bids[h] for i, h in enumerate(hands)))

cards2 = {c: i for i, c in enumerate('J23456789TQKA')}

def convert2(h):
  most_c = Counter([c for c in h if c != 'J'] or h).most_common(1)[0][0]
  hh = ''.join(most_c if c == 'J' else c for c in h)
  m = tuple(map(itemgetter(1), Counter(hh).most_common()))
  return (m, tuple(cards2[c] for c in h))

hands = sorted(bids.keys(), key=convert2)

print("\nNew total winnings:", sum((i+1)*bids[h] for i, h in enumerate(hands)))

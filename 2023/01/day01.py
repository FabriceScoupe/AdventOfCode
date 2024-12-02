#!/usr/bin/env python3
import re
import sys

lines = [l.rstrip('\n') for l in sys.stdin.readlines()]

# Use this empty dict for first part
#digits = {}

digits = {
  'zero': '0',
  'one': '1',
  'two': '2',
  'three': '3',
  'four': '4',
  'five': '5',
  'six': '6',
  'seven': '7',
  'eight': '8',
  'nine': '9',
}

digits.update({i:i for i in '0123456789'})

reversed_digits = {''.join(reversed(k)):v for k, v in digits.items()}

p1 = re.compile('('+'|'.join(digits.keys())+')')
p2 = re.compile('('+'|'.join(reversed_digits.keys())+')')

first_digits = [digits[p1.findall(l)[0]] for l in lines]
last_digits = [reversed_digits[p2.findall(''.join(reversed(l)))[0]] for l in lines]
numerics = [int(''.join(p)) for p in zip(first_digits, last_digits)]

for i, l in enumerate(lines):
  print(numerics[i],":", l)

print()
print("Result:", sum(numerics))

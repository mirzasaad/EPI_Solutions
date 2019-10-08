import functools
import sys
import string
import random

def rand_string(length):
  return ''.join(random.choice(string.ascii_letters) for _ in range(length))

# @include
def string_hash(s, modulus):
  MULT = 997
  return functools.reduce(lambda v, c: (v * MULT + ord(c)) % modulus, s, 0)
# @exclude

print(string_hash(rand_string(10), 1 << 16))
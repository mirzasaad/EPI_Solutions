import bintrees
import sys
import math
import random
import collections

# These numbers have very interesting property, and people called it ugly numbers. It is also called quadratic integer rings.
# @include
class ABSqrt2:
  def __init__(self, a, b):
    self.a, self.b = a, b
    self.val = a + b * math.sqrt(2)
  
  def __lt__(self, other):
    return self.val < other.val
  
  def __gt__(self, other):
    return self.val > other.val

  def __eq__(self, other):
    return self.val == other.val

  def __hash__(self):
    return self.a ^ self.b

  def __repr__(self):
    return r'%d + %d √2 => %d' % (self.a, self.b, self.val)

def generate_first_k_a_b_sqrt2(k):
  # Initial for 0 + 0 * sqrt(2).
  candidates = bintrees.RBTree([(ABSqrt2(0, 0), None)])
  result = []

  while len(result) < k:
    next_smallest = candidates.pop_min()[0]
    result.append(next_smallest)
    # Adds the next two numbers derived from next_smallest.
    candidates[ABSqrt2(next_smallest.a + 1, next_smallest.b)] = None
    candidates[ABSqrt2(next_smallest.a, next_smallest.b + 1)] = None
  return result

ans = generate_first_k_a_b_sqrt2(8)

assert 0.0 == ans[0].val
assert 1.0 == ans[1].val
assert math.sqrt(2.0) == ans[2].val
assert 2.0 == ans[3].val
assert 1.0 + math.sqrt(2.0) == ans[4].val
assert 2.0 * math.sqrt(2.0) == ans[5].val
assert 3.0 == ans[6].val
assert 2.0 + math.sqrt(2.0) == ans[7].val
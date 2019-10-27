import sys
sys.path.append(".")
import arrays_5
from arrays_5 import next_permutation

def permutation_improved_with_next_permutation(A):
  result = []
  while True:
    result.append(A.copy())
    A = next_permutation(A)
    if not A:
      break
  return result

assert [['a', 'b', 'c'], ['a', 'c', 'b'], ['b', 'a', 'c'], ['b', 'c', 'a'], ['c', 'a','b'], ['c', 'b', 'a']] == permutation_improved_with_next_permutation(perm)
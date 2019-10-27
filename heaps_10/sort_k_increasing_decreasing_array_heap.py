  
import sys
import random
import itertools
from merge_sorted_arrays_heapq import merge_sorted_arrays_pythonic

def sort_k_increasing_decreasing_array(A):
  INCREASING, DECREASING = range(2)
  start_index = 0
  subarray_type = INCREASING
  result = []
  for i in range(1, len(A) + 1):
    if (i == len(A) or  # A is ended. Adds the last subarray.
      (A[i - 1] < A[i] and subarray_type == DECREASING) or
      (A[i - 1] >= A[i] and subarray_type == INCREASING)):
      
      result.append(
        A[start_index:i] if subarray_type == INCREASING else A[i - 1:start_index - 1:-1]
      )
      subarray_type ^= 1
      start_index = i
  return merge_sorted_arrays_pythonic(result)

def sort_k_increasing_decreasing_array_pythonic(A):
  class Monotonic:
    def __init__(self):
      self._last = float('-inf')

    def __call__(self, current):
      is_smaller = current < self._last
      self._last = current
      return is_smaller
    
  return merge_sorted_arrays_pythonic(
    [list(group)[::-1 if is_decreasing else 1]
    for is_decreasing, group in itertools.groupby(A, Monotonic())
  ])

assert [57, 73, 190, 221, 294, 339, 418, 442, 452, 493] == sort_k_increasing_decreasing_array_pythonic([57, 73, 493, 221, 294, 339, 418, 452, 442, 190])

A = [1, 2, 3, 2, 1, 4, 5, 10, 9, 4, 4, 1, -1]
assert sorted(A) == sort_k_increasing_decreasing_array(
    A) == sort_k_increasing_decreasing_array_pythonic(A)

A = [-2**64, -1, 0, 1, 2, 4, 8, 2**64 - 1]
assert sorted(A) == sort_k_increasing_decreasing_array(
    A) == sort_k_increasing_decreasing_array_pythonic(A)

A = list(reversed(A))
assert sorted(A) == sort_k_increasing_decreasing_array(
    A) == sort_k_increasing_decreasing_array_pythonic(A)
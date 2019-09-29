import sys
import random
import heapq

# @include
def merge_sorted_arrays(sorted_arrays):
  min_heap = []
  # Builds a list of iterators for each array in sorted_arrays.
  sorted_arrays_iters = [iter(x) for x in sorted_arrays]

  for i, it in enumerate(sorted_arrays_iters):
    first_element = next(it, None)
    if first_element is not None:
      heapq.heappush(min_heap, (first_element, i))

  result = []

  while min_heap:
    smallest_entry, smallest_array_index = heapq.heappop(min_heap)
    result.append(smallest_entry)
    smallest_array_iter = sorted_arrays_iters[smallest_array_index]
    next_element =  next(smallest_array_iter, None)
    if next_element is not None:
      heapq.heappush(min_heap, (next_element, smallest_array_index))
  return result
# @exclude

# Pythonic solution, uses the heapq.merge() method which takes multiple inputs.
def merge_sorted_arrays_pythonic(sorted_arrays):
  return list(heapq.merge(*sorted_arrays))

A = [3, 5, 6]
B = [0, 6]
C = [0, 5, 28]

sorted_arrays = [A, B, C]
assert merge_sorted_arrays_pythonic(sorted_arrays) == [0, 0, 3, 5, 5, 6, 6, 28]

S = [[1, 5, 10], [2, 3, 100], [2, 12, 2**64 - 1]]
assert merge_sorted_arrays(S) == merge_sorted_arrays_pythonic(S) == [1, 2, 2, 3, 5, 10, 12, 100, 2**64 - 1]

S = [[1]]
assert merge_sorted_arrays(S) == merge_sorted_arrays_pythonic(S) == [1]

S = [[], [1], [2]]
assert merge_sorted_arrays(S) == merge_sorted_arrays_pythonic(S) == [1, 2]

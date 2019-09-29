import itertools
import heapq

def sort_approximately_sorted_array(sequence, k):
  min_heap = []
  # Adds the first k elements into min_heap. Stop if there are fewer than k elements.
  result = []
  for x in itertools.islice(sequence, k):
    heapq.heappush(min_heap, x)
  # For every new element, add it to min_heap and extract the smallest.
  for x in sequence:
    smallest = heapq.heappushpop(min_heap, x)
    result.append(smallest)
  
  while min_heap:
    result.append(heapq.heappop(min_heap))
  return result

assert [-1, 2, 3, 4, 5, 6, 8] == sort_approximately_sorted_array(iter([3, -1, 2, 6, 4, 5, 8]), 3)

A = [2, 1, 5, 4, 3, 9, 8, 7, 6]
assert sort_approximately_sorted_array(iter(A), 3) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
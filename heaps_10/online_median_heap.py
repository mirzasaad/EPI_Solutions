import heapq

def online_median(sequence):
  # min_heap stores the larger half seen so far.
  min_heap = []
  # max_heap stores the smaller half seen so far.
  # values in max_heap are negative
  max_heap = []
  result = []
  for x in sequence:
    heapq.heappush(max_heap, -heapq.heappushpop(min_heap, x))
    # Ensure min_heap and max_heap have equal number of elements if an even
    # number of elements is read; otherwise, min_heap must have one more element than max_heap.
    if len(max_heap) > len(min_heap):
      heapq.heappush(min_heap, -heapq.heappop(max_heap))
    
    result.append(0.5 * (min_heap[0] + (-max_heap[0]))
      if len(min_heap) == len(max_heap) else min_heap[0]
    )
    
  return result

assert online_median(iter([5, 4, 3, 2, 1])) == [5, 4.5, 4, 3.5, 3]
assert online_median(iter([1, 2, 3, 4, 5])) == [1, 1.5, 2, 2.5, 3]
assert online_median(iter([1, 0, 3, 5, 2, 0, 1])) == [1, 0.5, 1, 2, 2, 1.5, 1]
assert online_median(iter([-1])) == [-1]

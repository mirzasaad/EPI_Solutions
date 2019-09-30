import heapq

# @include
def k_largest_in_binary_heap(A, k):
  if k <= 0:
    return []
  
  # Stores the (-value, index)-pair in candidate_max_heap. This heap is
  # ordered by value field. Uses the negative of value to get the effect of a max heap.
  candidate_max_heap = []
  # The largest element in A is at index 0.
  heapq.heappush(candidate_max_heap, (-A[0], 0))
  result = []
  for _ in range(k):
    candidate_index = candidate_max_heap[0][1]
    result.append(-heapq.heappop(candidate_max_heap)[0])

    left_child_index = 2 * candidate_index + 1
    if left_child_index < len(A):
      heapq.heappush(candidate_max_heap, (-A[left_child_index], left_child_index))
    
    right_child_index = 2 * candidate_index + 2
    if right_child_index < len(A):
      heapq.heappush(candidate_max_heap, (-A[right_child_index], right_child_index))
    print(candidate_max_heap)
  
  return result

A = [561, 401, 314, 28, 156, 359, 271, 11, 3]
print(k_largest_in_binary_heap(A, 3))

def search_smallest(A):
  left, right = 0, len(A) - 1
  while left < right:
    middle = left + (right - left) // 2
    # Minimum cannot be in A[mid + 1:right + 1] so it must be in A[left:mid + 1].
    if A[middle] < A[right]:
      right = middle
    else:
      # Minimum must be in A[mid + 1:right + 1].
      left = middle + 1
    # Loop ends when left == right.
  return left

A = [3, 1, 2]
assert 1 == search_smallest(A)
A = [0, 2, 4, 8]
assert 0 == search_smallest(A)
A[0] = 16
assert 1 == search_smallest(A)
A = [2, 3, 4]
assert 0 == search_smallest(A)
A = [100, 101, 102, 2, 5]
assert 3 == search_smallest(A)
A = [10, 20, 30, 40, 5]
assert 4 == search_smallest(A)
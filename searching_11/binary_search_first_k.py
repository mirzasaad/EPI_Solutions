import bisect

def search_first_of_k(A, k):
  left, right, result = 0, len(A) - 1, -1
  while left <= right:
    middle = left + (right - left) // 2
    if A[middle] < k:
      left = middle + 1
    elif A[middle] > k:
      right = middle - 1
    elif A[middle] == k:
      result = middle
      right = middle - 1
  return result

def search_first_of_k_pythonic(A, k):
  i = bisect.bisect_left(A, k)
  return i if i >= 0 and i < len(A) else -1
A = [-14, -10, 2, 108, 108, 243, 285, 285, 285, 410]
assert search_first_of_k(A, 108) == 3

A = [0, 1, 2, 3, 4, 5, 6, 7]
assert 0 == search_first_of_k(A, 0)
assert 1 == search_first_of_k(A, 1)
assert 4 == search_first_of_k(A, 4)
assert 6 == search_first_of_k(A, 6)
assert 7 == search_first_of_k(A, 7)
assert -1 == search_first_of_k(A, 8)
assert -1 == search_first_of_k(A, -2**64)
A[0] = 1
assert 0 == search_first_of_k(A, 1)
A[5] = 4
A[6] = 4
assert 4 == search_first_of_k(A, 4)
A = [1, 1, 1, 1, 1, 2]
assert -1 == search_first_of_k(A, 0)
assert 0 == search_first_of_k(A, 1)
assert 5 == search_first_of_k(A, 2)
A[4] = 2
assert 4 == search_first_of_k(A, 2)
def b_search(A, n):
  left, right = 0, len(A) - 1
  while left <= right:
    middle = left + (right - left) // 2
    if A[middle] < n:
      left = middle + 1
    elif A[middle] > n:
      right = middle - 1
    elif A[middle] == n:
      return middle
  return -1

A = [1, 2, 3, 4, 5, 6, 7]
print(b_search(A, 1))
def matrix_search(A, x):
  row, col = 0, len(A[0]) - 1
  while row < len(A) and col >= 0:
    if A[row][col] == x:
      return True
    elif A[row][col] > x:
      col -= 1
    else:
      row += 1
  return False

A = [[1]]
assert not matrix_search(A, 0)
assert matrix_search(A, 1)

A = [[1, 5], [2, 6]]
assert not matrix_search(A, 0)
assert matrix_search(A, 1)
assert matrix_search(A, 2)
assert matrix_search(A, 5)
assert matrix_search(A, 6)
assert not matrix_search(A, 3)
assert not matrix_search(A, float('inf'))

A = [[2, 5], [2, 6]]
assert not matrix_search(A, 1)
assert matrix_search(A, 2)

A = [[1, 5, 7], [3, 10, 100], [3, 12, float('inf')]]
assert matrix_search(A, 1)
assert not matrix_search(A, 2)
assert not matrix_search(A, 4)
assert matrix_search(A, 3)
assert matrix_search(A, 10)
assert matrix_search(A, float('inf'))
assert matrix_search(A, 12)
def search_entry_equal_to_its_index(A):
  left, right = 0, len(A) - 1
  while left <= right:
    mid = left + (right - left) // 2
    difference = A[mid] - mid
    # A[mid] == mid if and only if difference == 0.
    if difference == 0:
      return mid
    elif difference > 0:
      right = mid - 1
    else: # difference < 0.
      left = mid + 1
  return -1

A = [0, 1, 2, 3]
assert -1 != search_entry_equal_to_its_index(A)
assert 0 <= search_entry_equal_to_its_index(
    A) and search_entry_equal_to_its_index(A) <= 3
A[0] = -1
A[2] = 4
A[3] = 5
assert 1 == search_entry_equal_to_its_index(A)
A = [0]
assert -1 != search_entry_equal_to_its_index(A)
A[0] = -1
assert -1 == search_entry_equal_to_its_index(A)

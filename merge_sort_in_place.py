import math

def merge(A, left, middle, right):
  L = A[left:middle]
  R = A[middle:right]
  i = 0
  j = 0
  k = left

  while i < len(L) and j < len(R):
    if L[i] < R[j]:
      A[k] = L[i]
      i += 1
    else:
      A[k] = R[j]
      j += 1
    k += 1

  while i < len(L):
    A[k] = L[i]
    i += 1
    k += 1

  while j < len(R):
    A[k] = R[j]
    j += 1
    k += 1

def merge_sort_helper(A, left, right):
  if right - left > 1:
    middle = (left + right) // 2
    merge_sort_helper(A, left, middle)
    merge_sort_helper(A, middle, right)
    merge(A, left, middle, right)
def merge_sort(A):
  return merge_sort_helper(A, 0, len(A))



A = [2, 5, 1, 3, 7, 4, 2, 3, 9, 8, 6, 3]
B = [3, 1, 25]
print(merge_sort(A))
print(A)
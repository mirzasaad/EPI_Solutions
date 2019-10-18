def parition(A, left, right):
  pivot = A[right]
  slow = 0
  for fast in range(0, right):
    if A[fast] <= pivot:
      A[fast], A[slow] = A[slow], A[fast]
      slow += 1
  A[right], A[slow] = A[slow], A[right]
  return slow

def quick_sort_helper(A, left, right):
  if left < right:
    pi = parition(A, left, right)
    quick_sort_helper(A, left, pi - 1)
    quick_sort_helper(A, pi + 1, right)
def quick_sort(A):
  return quick_sort_helper(A, 0, len(A) - 1)


A = [2, 5, 1, 3, 7, 4, 2, 3, 9, 8, 6, 3]
B = [3, 1, 25]
print(quick_sort(A))
print(A)
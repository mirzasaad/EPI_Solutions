import random

def find_kth_largest(A, k):
  comp = {
    'greater': lambda a, b: a > b,
  }
  def find_kth(compare):
    def partition_around_pivot(left, right, pivot_index):
      pivot_value = A[pivot_index]
      A[right], A[pivot_index] = A[pivot_index], A[right]
      new_pivot_index = left
      for i in range(left, right):
        if compare(A[i], pivot_value):
          A[new_pivot_index], A[i] = A[i], A[new_pivot_index]
          new_pivot_index += 1
      A[right], A[new_pivot_index] = A[new_pivot_index], A[right]
      return new_pivot_index

    left, right = 0, len(A) - 1
    while left <= right:
      pivot_index = random.randint(left, right)
      new_pivot_index = partition_around_pivot(left, right, pivot_index)
      if new_pivot_index == k - 1:
        return A[new_pivot_index]
      elif new_pivot_index > k - 1:
        right = new_pivot_index - 1
      else: # new_pivot_index < k - 1:
        left = new_pivot_index + 1
    return -1
  return find_kth(comp.get('greater'))
  
  

A = [3, 2, 1, 5, 4]
assert find_kth_largest(A, 3) == 3
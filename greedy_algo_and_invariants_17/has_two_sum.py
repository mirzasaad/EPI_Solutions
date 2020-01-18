import itertools

A = [-2, 1, 2, 4, 7, 11]

def has_two_sum_pythonic(A, t):
  return any(i+j == t for i, j in itertools.combinations(A, 2))

def has_two_sum(A, t):
  i, j = 0, len(A) - 1
  while i <= j:
    if A[i] + A[j] == t:
      return True
    elif A[i] + A[j] > t:
      j -= 1
    else: 
      i += 1
  return False

assert has_two_sum(A, 13) == has_two_sum_pythonic(A, 13)
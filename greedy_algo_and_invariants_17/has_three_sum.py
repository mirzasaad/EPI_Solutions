A = [11, 2, 5, 7, 3]

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

def has_three_sum(A, t):
  A.sort()
  return any(has_two_sum(A, t - i) for i in A)

assert has_three_sum(A, 21) == True
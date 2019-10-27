def permutations(A):
  def directed_permutations(i):
    if i == len(A) - 1:
      result.append(A.copy())
      return

    for j in range(i, len(A)):
      A[i], A[j] = A[j], A[i]
      directed_permutations(i + 1)
      A[j], A[i] = A[i], A[j]

  result = []
  directed_permutations(0)
  return result

A = ['a', 'b', 'c']
assert [['a', 'b', 'c'], ['a', 'c', 'b'], ['b', 'a', 'c'], ['b', 'c', 'a'], ['c', 'b','a'], ['c', 'a', 'b']] == permutations(A)
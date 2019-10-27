import random
def merge_sorted_array_in_place(A, m, B, n):
  m, n, write_index = m - 1, n - 1, m + n - 1
  while m >= 0 and n >= 0:
    if A[m] > B[n]:
      A[write_index] = A[m]
      write_index, m = write_index - 1, m - 1
    else:
      A[write_index] = B[n]
      write_index, n = write_index - 1, n - 1
  while n >= 0:
    A[write_index] = B[n]
    write_index, n = write_index - 1, n - 1

m = random.randint(0, 10000)
n = random.randint(0, 10000)
A = sorted(random.randint(-(m + n), m + n)
        for _ in range(m)) + [None] * n
B = sorted(random.randint(-(m + n), m + n) for _ in range(n))
merge_sorted_array_in_place(A, m, B, n)
assert all(A[i - 1] <= A[i] for i in range(1, len(A)))
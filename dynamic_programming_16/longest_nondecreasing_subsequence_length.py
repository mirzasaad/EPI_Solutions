# @include
def longest_nondecreasing_subsequence_length(A):
  # max_length[i] holds the length of the longest nondecreasing subsequence
  # of A[:i + 1].
  max_length = [1] * len(A)
  for i in range(1, len(A)):
    max_length[i] = max(1 + max(
      [max_length[j] for j in range(i) if A[i] >= A[j]], default=0), max_length[i])
  return max(max_length)
# @exclude

def find_longest_increasing_subarray(A):
  result = Subarray(0, 0)
  i, max_length = 0, 1
  while i < len(A) - max_length:
    # Backward check and skip if A[j] >= A[j + 1].
    for j in range(i + max_length, i, -1):
      if A[j - 1] >= A[j]:
        i = j
        break
      else:  # Forward check if it is not skippable (the loop ended normally)
        i += max_length
        while i < len(A) and A[i - 1] < A[i]:
          i, max_length = i + 1, max_length + 1
        result = Subarray(i - max_length, i - 1)
  return result
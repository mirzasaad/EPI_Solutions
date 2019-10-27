def longest_subarray_with_distinct_entries(A):
  # Records the most recent occurrences of each entry.
  most_recent_occurrence = {}
  longest_dup_free_subarray_start_idx = result = 0
  for i, a in enumerate(A):
    if a in most_recent_occurrence:
      dup_idx = most_recent_occurrence[a]
      # A[i] appeared before. Did it appear in the longest current subarray?
      if dup_idx >= longest_dup_free_subarray_start_idx:
        result = max(result, i - longest_dup_free_subarray_start_idx)
        longest_dup_free_subarray_start_idx = dup_idx + 1
    most_recent_occurrence[a] = i
  return max(result, len(A) - longest_dup_free_subarray_start_idx)

assert 1 == longest_subarray_with_distinct_entries([1, 1, 1])
assert 2 == longest_subarray_with_distinct_entries([1, 2, 1])
assert 3 == longest_subarray_with_distinct_entries([1, 2, 1, 3, 1, 2, 1])
assert 2 == longest_subarray_with_distinct_entries(
    [1, 2, 2, 3, 3, 1, 1, 2, 1])


import math

def merge(L1, L2):
  i, j, result = 0, 0, []

  while i < len(L1) and j < len(L2):
    if L1[i] < L2[j]:
      result.append(L1[i])
      i += 1
    elif L2[j] < L1[i]:
      result.append(L2[j])
      j += 1
    elif L1[i] == L2[j]:
      result.append(L1[i])
      result.append(L2[j])
      i += 1
      j += 1

  while i < len(L1):
    result.append(L1[i])
    i += 1
  while j < len(L2):
    result.append(L2[j])
    j += 1

  return result

def merge_sort(A):
  if len(A) == 1:
    return A

  middle = math.floor(len(A) / 2)
  left = A[:middle]
  right = A[middle:]

  return merge(
    merge_sort(left),
    merge_sort(right),
  )



A = [2, 5, 1, 3, 7, 4, 2, 3, 9, 8, 6, 3]
print(merge_sort(A))
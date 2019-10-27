import bisect
def intersect_sorted_arrays_1(A, B):
  return [a for i, a in enumerate(A) if (i == 0 or a != A[i - 1]) and A[i] in B]

def intersect_sorted_arrays_2(A, B):
  def is_present(k):
    i = bisect.bisect_left(B, k)
    return i < len(B) and B[i] == k
  return [a for i, a in enumerate(A) if (i == 0 or a != A[i - 1]) and is_present(a)]

def intersect_sorted_arrays_3(A, B):
  i, j, intersection_A_B = 0, 0, []
  while i < len(A) and len(B):
    if A[i] < B[j]:
      i += 1
    elif A[i] > B[j]:
      j += 1
    elif A[i] == B[j]:
      if i == 0 or A[i] != A[i - 1]:
        intersection_A_B.append(A[i])
      i, j = i + 1, j + 1
  return intersection_A_B
A = [2, 3, 3, 5, 7, 11]
B = [3, 3, 7, 15, 31]

print(intersect_sorted_arrays_3(A, B))
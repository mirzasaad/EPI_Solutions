from tabulate import tabulate

A = "hyundai"
B = "honda"
distance_between_prefixes = [[-1] * len(B) for _ in A]

def levenshtein_distance(A, B):
  distance_between_prefixes = [[i] + [0] * (len(A) + 1) if i > 0 else list(range(len(A) + 1)) for i in range(len(B) + 1)]

  for i in range(1, len(B) + 1):
    for j in range(1, len(A) + 1):
      if B[i - 1] == A[j - 1]:
        distance_between_prefixes[i][j] = distance_between_prefixes[i - 1][j - 1]
      else:
        add = distance_between_prefixes[i][j - 1]
        delete = distance_between_prefixes[i - 1][j]
        substitute = distance_between_prefixes[i - 1][j - 1]
        distance_between_prefixes[i][j] = min(add, delete, substitute) + 1
  return levenshtein_distance[-1][-1]
levenshtein_distance(A, B)

def levenshtein_distance(A, B):
  def compute_distance_between_prefixes(A_idx, B_idx):
    if A_idx < 0:
      # A is empty so add all of B's characters.
      return B_idx + 1
    elif B_idx < 0:
      # B is empty so delete all of A's characters.
      return A_idx + 1

    if distance_between_prefixes[A_idx][B_idx] == -1:
      if A[A_idx] == B[B_idx]:
        distance_between_prefixes[A_idx][B_idx] = (compute_distance_between_prefixes(A_idx - 1, B_idx - 1))
      else:
        substitute_last = compute_distance_between_prefixes(A_idx - 1, B_idx - 1)
        add_last = compute_distance_between_prefixes(A_idx - 1, B_idx)
        delete_last = compute_distance_between_prefixes(A_idx, B_idx - 1)
        distance_between_prefixes[A_idx][B_idx] = (1 + min(substitute_last, add_last, delete_last))
    return distance_between_prefixes[A_idx][B_idx]

  return compute_distance_between_prefixes(len(A) - 1, len(B) - 1)



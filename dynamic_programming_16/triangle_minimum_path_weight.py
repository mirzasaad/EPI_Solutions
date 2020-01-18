triangle = [
  [2],
  [5,4],
  [5,5,7],
  [1,4,8,3]
]

def triangleMinSumPath(triangle):
  dp = [[0] * len(triangle[-1]) for _ in triangle]

  dp = triangle[-1][:]
  for row in range(len(triangle) - 2, -1, -1):
    for col in range(row + 1):
      dp[col] = triangle[row][col] + min(dp[col], dp[col + 1])
  return dp[0][0]

def minimum_path_weight(triangle):
  min_weight_to_curr_row = [0]
  for row in triangle:
    min_weight_to_curr_row = [
      row[j] +
      min(min_weight_to_curr_row[max(j - 1, 0)],
        min_weight_to_curr_row[min(j, len(min_weight_to_curr_row) - 1)])
      for j in range(len(row))
    ]
  return min(min_weight_to_curr_row)

A = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
print(minimum_path_weight(triangle))
triangleMinSumPath(triangle)

# http://www.zrzahid.com/min-sum-path-in-triangle/
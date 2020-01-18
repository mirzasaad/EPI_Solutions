from tabulate import tabulate
import itertools

def maximum_revenue(coins):
  def compute_maximum_revenue_for_range(a, b):
    if a > b:
      # No coins left.
      return 0

    if maximum_revenue_for_range[a][b] == 0:
      max_revenue_a = coins[a] + min(
        compute_maximum_revenue_for_range(a + 2, b),
        compute_maximum_revenue_for_range(a + 1, b - 1))
      max_revenue_b = coins[b] + min(
        compute_maximum_revenue_for_range(a + 1, b - 1),
        compute_maximum_revenue_for_range(a, b - 2))
      maximum_revenue_for_range[a][b] = max(max_revenue_a, max_revenue_b)
    return maximum_revenue_for_range[a][b]

  maximum_revenue_for_range = [[0] * len(coins) for _ in coins]
  return compute_maximum_revenue_for_range(0, len(coins) - 1)
# @exclude


def maximum_revenue_alternative(coins):
  def maximum_revenue_alternative_helper(a, b):
    if a > b:
      return 0
    elif a == b:
      return coins[a]

    if maximum_revenue_for_range[a][b] == -1:
      maximum_revenue_for_range[a][b] = max(
          coins[a] + prefix_sum[b] -
          (prefix_sum[a]
            if a + 1 > 0 else 0) - maximum_revenue_alternative_helper(
                a + 1, b), coins[b] + prefix_sum[b - 1] -
          (prefix_sum[a - 1] if a > 0 else 0
            ) - maximum_revenue_alternative_helper(a, b - 1))
    return maximum_revenue_for_range[a][b]

  prefix_sum = list(itertools.accumulate(coins))
  maximum_revenue_for_range = [[-1] * len(coins) for _ in coins]
  return maximum_revenue_alternative_helper(0, len(coins) - 1)


def greedy(coins):
  def greedy_helper(start, end):
    if start > end:
      return 0

    if coins[start] > coins[end]:
      gain = coins[start]
      if coins[start + 1] > coins[end]:
        gain += greedy_helper(start + 2, end)
      else:
        gain += greedy_helper(start + 1, end - 1)
    else:
      gain = coins[end]
      if coins[start] > coins[end - 1]:
        gain += greedy_helper(start + 1, end - 1)
      else:
        gain += greedy_helper(start, end - 2)
    return gain

  return greedy_helper(0, len(coins) - 1)


def simple_test():
  coins = [25, 5, 10, 5, 10, 5, 10, 25, 1, 25, 1, 25, 1, 25, 5, 10]
  assert 140 == maximum_revenue(coins)
  assert maximum_revenue_alternative(coins) == maximum_revenue(coins)
  assert 120 == greedy(coins)

def maximum_revenue_iterative(coins):
  maximum_revenue_for_range = [[0] * len(coins) for _ in coins]
  
  for row in range(len(coins)):
    for col in range(row, len(coins)):
      gap = col - row
      x, y, z = 0, 0, 0
      # Here x is value of F(i+2, j),  
      # y is F(i+1, j-1) and z is  
      # F(i, j-2) in above recursive formula 
      if (gap + 2) <= col:
        x = maximum_revenue_for_range[gap + 2][col]
      if (gap + 1) <= col - 1:
        y = maximum_revenue_for_range[gap + 1][col - 1]
      if gap <= col - 2:
        z = maximum_revenue_for_range[gap][col - 2]
      maximum_revenue_for_range[gap][col] = max(
        min(x, y) + coins[gap],
        min(y, z) + coins[col]
      )
  return maximum_revenue_for_range[0][-1]

print(maximum_revenue_iterative([25, 5, 10, 4, 12, 15, 20]))

simple_test()
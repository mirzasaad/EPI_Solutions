import math

def square_root(x):
  left, right = 0, x
  while left <= right:
    mid = (left + right) // 2
    mid_squared = mid * mid
    if mid_squared <= x:
      left = mid + 1
    else:
      right = mid
  return left - 1

assert math.isclose(square_root(1.0), math.sqrt(1.0))
assert math.isclose(square_root(2.0), math.sqrt(2.0))
assert math.isclose(square_root(0.001), math.sqrt(0.001))
assert math.isclose(square_root(0.5), math.sqrt(0.5))
assert math.isclose(square_root(100000000.001), math.sqrt(100000000.001))
assert math.isclose(square_root(1024.0), math.sqrt(1024.0))

import math

def square_root(x):
  # Decides the search range according to x's value relative to 1.0.
  left, right = (x, 1.0) if x < 1.0 else (1.0, x)
  # Keeps searching as long as left != right.
  while not math.isclose(left, right):
    mid = 0.5 * (left + right)
    mid_squared = mid * mid
    if mid_squared > x:
      right = mid
    else:
      left = mid
  return left

assert math.isclose(square_root(1.0), math.sqrt(1.0))
assert math.isclose(square_root(2.0), math.sqrt(2.0))
assert math.isclose(square_root(0.001), math.sqrt(0.001))
assert math.isclose(square_root(0.5), math.sqrt(0.5))
assert math.isclose(square_root(100000000.001), math.sqrt(100000000.001))
assert math.isclose(square_root(1024.0), math.sqrt(1024.0))

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

assert square_root(0) == 0
assert square_root(1) == 1
assert square_root(2) == 1
assert square_root(3) == 1
assert square_root(4) == 2
assert square_root(7) == 2
assert square_root(121) == 11
assert square_root(64) == 8
assert square_root(300) == 17
assert square_root(2147483647) == 46340

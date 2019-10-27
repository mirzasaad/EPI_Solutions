def fibonacci(n, cache={}):
  if n <= 1:
    return n
  elif n not in cache:
    cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
  return cache[n]

def fibonacci_dp(n):
  if n <= 1:
    return n

  f_minus_2, f_minus_1 = 0, 1
  for _ in range(1, n):
    f = f_minus_2 + f_minus_1
    f_minus_2, f_minus_1 = f_minus_1, f
  return f_minus_1

assert fibonacci(10) == 55
assert fibonacci(0) == 0
assert fibonacci(1) == 1
assert fibonacci(16) == 987
assert fibonacci(40) == 102334155
assert fibonacci(10) == fibonacci_dp(10)
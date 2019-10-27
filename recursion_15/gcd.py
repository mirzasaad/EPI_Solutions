def gcd(x, y):
  return x if y == 0 else gcd(y, x%y)

assert gcd(270, 192) == 6
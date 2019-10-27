def test_collatz_conjecture(n):
  # Stores odd numbers already tested to converge to 1.
  verified_numbers = set()
  # Starts from 3, hypothesis holds trivially for 1.
  for i in range(3, n + 1):
    sequence = set()
    test_i = i
    while test_i >= i:
      if test_i in sequence:
        # We previously encountered test_i, so the Collatz sequence has fallen into a loop. This disproves the hypothesis, so we short-circuit, returning False.
        return False
      sequence.add(test_i)
      if test_i & 1:
        if test_i in verified_numbers:
          break
        verified_numbers.add(test_i)
        test_i = test_i * 3 + 1
      else:
        test_i //= 2
  return True

def collatz_check(x, visited):
  if x == 1:
    return True
  elif x in visited:
    return False
  visited.add(x)
  if x & 1:  # odd number
    return collatz_check(3 * x + 1, visited)
  else:  # even number
    return collatz_check(x >> 1, visited)  # divide by 2

assert collatz_check(4, set()) == True
assert test_collatz_conjecture(11) == True
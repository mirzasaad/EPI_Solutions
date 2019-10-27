from math import log2

def generate_power_set(S):
  power_set = []
  for i in range(1 << len(S)):
    bit_array = i
    subset = []
    while bit_array:
      lsb = bit_array & ~(bit_array - 1)
      subset.append(int(log2(lsb)))
      bit_array &= (bit_array - 1)
    power_set.append(subset)
  return power_set

def generate_power_set_2(s):
  power_set = []
  for i in range(1 << len(s)):
    subset = []
    for j in range(len(s)):
      if i & (1 << j):
        subset.append(s[j])
    power_set.append(subset)
  return power_set

assert generate_power_set([0, 1, 2]) == [[], [0], [1], [0, 1], [2], [0, 2], [1, 2], [0, 1, 2]]
assert generate_power_set_2([0, 1, 2]) == [[], [0], [1], [0, 1], [2], [0, 2], [1, 2], [0, 1, 2]]
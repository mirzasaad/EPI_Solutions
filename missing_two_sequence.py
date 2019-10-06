#https://www.geeksforgeeks.org/find-two-missing-numbers-set-2-xor-based-solution/
from functools import reduce
A = [1, 3, 5, 6]
n = 6

n_XOR = reduce(lambda v, i: v ^ i, list(range(1, n + 1)), 0)
XOR = reduce(lambda v, i: v ^ i, A, 0) ^ n_XOR
right_most_bit_set = XOR & ~(XOR - 1)

first = reduce(lambda p, c: p ^ (c if right_most_bit_set & c else 0), A, 0) ^ n_XOR
second = reduce(lambda p, c: p ^ (c if not right_most_bit_set & c else 0), A, 0) ^ n_XOR

assert first == 2
assert second == 3

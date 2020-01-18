def number_of_ways_to_top(top, maximum_step):
  def compute_number_of_ways_to_h(h):
    if h <= 1:
      return 1

    if number_of_ways_to_h[h] == 0:
      number_of_ways_to_h[h] = sum(
        compute_number_of_ways_to_h(h - i)
        for i in range(1, min(h, maximum_step) + 1))

    return number_of_ways_to_h[h]

  number_of_ways_to_h = [0] * (top + 1)
  return compute_number_of_ways_to_h(top)

assert 5 == number_of_ways_to_top(4, 2)
assert 1 == number_of_ways_to_top(1, 2)
assert 1 == number_of_ways_to_top(0, 3)

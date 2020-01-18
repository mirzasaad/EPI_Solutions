def compute_binomial_coefficient(n, k):
  def compute_x_choose_y(x, y):
    if y in (0, x):
      return 1

    if number_of_ways[x][y] == 0:
      without_y = compute_x_choose_y(x - 1, y)
      with_y = compute_x_choose_y(x - 1, y - 1)
      number_of_ways[x][y] = without_y + with_y
    return number_of_ways[x][y]

  number_of_ways = [[0] * (k + 1) for _ in range(n + 1)]
  a = compute_x_choose_y(n, k)
  print(number_of_ways)
  return a

print(compute_binomial_coefficient(6, 3))

def pascal(n):
  line = [1]
  for k in range(n):
    line.append(line[k] * (n - k)/(k + 1))
  return line
print(pascal(6))

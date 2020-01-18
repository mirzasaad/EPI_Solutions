import collections

# @include
MPG = 20

# gallons[i] is the amount of gas in city i, and distances[i] is the
# distance city i to the next city.
def find_ample_city(gallons, distances):
  remaining_gallons = 0
  CityAndRemainingGas = collections.namedtuple('CityAndRemainingGas', ('city', 'remaining_gallons'))

  city_remaining_gallons_pair = CityAndRemainingGas(0, 0)
  num_cities = len(gallons)
  for i in range(1, num_cities):
    remaining_gallons += gallons[i - 1] - distances[i - 1] // MPG
    if remaining_gallons < city_remaining_gallons_pair.remaining_gallons:
      city_remaining_gallons_pair = CityAndRemainingGas(i, remaining_gallons)
  return city_remaining_gallons_pair.city

gallons = (20, 15, 15, 15, 35, 25, 30, 15, 65, 45, 10, 45, 25)
distances = (15 * MPG, 20 * MPG, 50 * MPG, 15 * MPG, 15 * MPG, 30 * MPG,
20 * MPG, 55 * MPG, 20 * MPG, 50 * MPG, 10 * MPG, 15 * MPG,
15 * MPG)

assert find_ample_city(gallons, distances) == 8

gallons = (50, 20, 5, 30, 25, 10, 10)
distances = (900, 600, 200, 400, 600, 200, 100)

assert find_ample_city(gallons, distances) == 3
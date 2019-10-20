import csv
import heapq
import io
import math
import random
import sys

def find_closest_k_stars(stars , k) :
  # max-heap to store the closest k stars seen so far.
  max_heap = []
  for star in stars:
    # Add each star to the max-heap. If the max-heap size exceeds k, remove
    # the maximum element from the max-heap.
    # As python has only min-heap, insert tuple (negative of distance, star)
    # to sort in reversed distance order.
    heapq.heappush(max_heap, (-star.distance, star))
    if len(max_heap) == k + 1:
      heapq.heappop(max_heap)
    
  return [s[1] for s in heapq.nlargest(k, max_heap)]
class Star:
  def __init__(self, x, y, z):
    self.x, self.y, self.z = x, y, z

  @property
  def distance(self):
    return self.x**2 + self.y**2 + self.z**2

  def __lt__(self, rhs):
    return self.distance < rhs.distance

  def __str__(self):
    return ' '.join(map(str, (self.x, self.y, self.z)))

  def __eq__(self, rhs):
    return math.isclose(self.distance, rhs.distance)

stars = [Star(1, 2, 3), Star(5, 5, 5), Star(0, 2, 1), Star(9, 2, 1), Star(1, 2, 1), Star(2, 2, 1)]

closest_stars = find_closest_k_stars(stars, 3)

assert len(closest_stars) == 3
assert closest_stars[0].distance == Star(0, 2, 1).distance
assert closest_stars[0].distance == Star(2, 0, 1).distance
assert closest_stars[1].distance == Star(1, 2, 1).distance
assert closest_stars[1].distance == Star(1, 1, 2).distance

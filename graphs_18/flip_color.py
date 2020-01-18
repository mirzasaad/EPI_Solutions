import random
import collections
import copy 

def flip_color(x, y, A):
  Coordinate = collections.namedtuple('Coordinate', ('x', 'y'))
  q = collections.deque([Coordinate(x, y)])
  color = A[x][y]
  A[x][y] ^= 1

  while q:
    x, y = q.popleft()  
    for left, top in (0, 1), (0, -1), (1, 0), (-1, 0):
      next_x, next_y = x + left, y + top
      if (0 <= next_x < len(A) and 0 <= next_y < len(A[next_x]) and
        A[next_x][next_y] == color):
        A[next_x][next_y] ^= 1
        q.append(Coordinate(next_x, next_y))

def flip_color_recursive(x, y, A):
  color = A[x][y]
  A[x][y] ^= 1
  for left, top in (0, 1), (0, -1), (1, 0), (-1, 0):
    next_x, next_y = x + left, y + top
    if (0 <= next_x < len(A) and 0 <= next_y < len(A[next_x]) and
      A[next_x][next_y] == color):
      flip_color_recursive(next_x, next_y, A)

n = 10 or random.randint(1, 10)
A = [[random.randint(0, 1) for _ in range(n)] for _ in range(n)]
AA = copy.deepcopy(A)
i, j = random.randrange(n), random.randrange(n)
print('color =>',A[i][j], 'row =>', i, 'column =>', j)
for i in range(n):
  print(*A[i])
flip_color(i, j, A)
flip_color_recursive(i, j, AA)
print()
for i in range(n):
  print(*A[i])
assert A == AA

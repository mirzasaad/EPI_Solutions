import random
import collections

# @include
def fill_surrounded_regions(board):
  n, m = len(board), len(board[0])
  q = collections.deque(
    [(i, j) for k in range(n) for i, j in ((k, 0), (k, m - 1))] +
    [(i, j) for k in range(m) for i, j in ((0, k), (n - 1, k))])
  while q:
    x, y = q.popleft()
    if 0 <= x < n and 0 <= y < m and board[x][y] == 'W':
      board[x][y] = 'T'
      q.extend([(x, y - 1), (x, y + 1), (x + 1, y), (x - 1, y)])
  board[:] = [['B' if col != 'T' else 'W' for col in row] for row in board]

A = [['B', 'B', 'B', 'B'], ['W', 'B', 'W', 'B'], ['B', 'W', 'W', 'B'], ['B', 'B', 'B', 'B']]
fill_surrounded_regions(A)
golden = [['B', 'B', 'B', 'B'], ['W', 'B', 'B', 'B'], ['B', 'B', 'B', 'B'], ['B', 'B', 'B', 'B']]
assert A == golden

n = random.randint(1, 50)
m = random.randint(1, 50)
board = [[random.choice(('B', 'W')) for _ in range(m)] for _ in range(n)]
for row in board:
  print(*row, sep='')
fill_surrounded_regions(board)
print()
for row in board:
  print(*row, sep='')
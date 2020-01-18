import random
import collections
from tabulate import tabulate

# @include
WHITE, BLACK = range(2)

Coordinate = collections.namedtuple('Coordinate', ('x', 'y'))

def search_maze(maze, s, e):
  # Perform DFS to find a feasible path.
  def search_maze_helper(cur):
    # Checks cur is within maze and is a white pixel.
    if not (0 <= cur.x < len(maze) and 0 <= cur.y < len(maze[cur.x]) and maze[cur.x][cur.y] == WHITE):
      return False
    
    path.append(cur)
    maze[cur.x][cur.y] = BLACK

    if cur == e:
      return True

    if any(map(search_maze_helper, [Coordinate(cur.x + 1, cur.y), Coordinate(cur.x, cur.y + 1), Coordinate(cur.x - 1, cur.y), Coordinate(cur.x, cur.y - 1)])):
      return True
    del path[-1]
    return False

  path = []
  
  if not search_maze_helper(s):
    return []  # No path between s and e.
  return path

n = random.randint(1, 10)
m = random.randint(1, 10)
maze = [[random.randrange(2) for _ in range(m)] for _ in range(n)]
white = []
for i in range(n):
  for j in range(m):
    if maze[i][j] == WHITE:
      white.append(Coordinate(i, j))
  print(*maze[i])
print()

print()
if white:
  start = random.randrange(len(white))
  end = random.randrange(len(white))
  print('start => ', white[start].x, white[start].y)
  print('end => ', white[end].x, white[end].y)
  path = search_maze(maze, white[start], white[end])
  print('path => no path') if not path else print('path =>') 
  for i in range(len(path)):
    print(path[i])
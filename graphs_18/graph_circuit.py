import collections
import random

class GraphVertex:
  def __init__(self):
    self.d = -1
    self.edges = []

  def __repr__(self):
    return '(distance => %d, id => %d, edges => [%s])' % (self.d, id(self), ','.join(
      str(id(x)) for x in self.edges))

def is_any_placement_feasible(G):
  def bfs(s):
    s.d = 0
    q = collections.deque([s])

    while q:
      for t in q[0].edges:
        if t.d == -1:  # Unvisited vertex.
          t.d = q[0].d + 1
          q.append(t)
        elif t.d == q[0].d:
          return False
      del q[0]
    return True

  return all(bfs(v) for v in G if v.d == -1)

def is_two_colorable(G):
  for v in G:
    v.d = -1

  def dfs(s):
    for t in s.edges:
      if t.d == -1:
        t.d = int(not s.d)
        if not dfs(t):
          return False
      elif t.d == s.d:
        return False
    return True

  for v in G:
    if v.d == -1:
      v.d = 0
      if not dfs(v):
        return False
  return True  

#https://cp-algorithms.com/graph/bipartite-check.html
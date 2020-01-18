import collections
import random

class GraphVertex:
  def __init__(self, label):
    self.label = label
    self.edges = []

  def __repr__(self):
    return '%d => (%s)' % (self.label, ','.join(str(x.label) for x in self.edges))

def clone_graph(G):
  if not G:
    return None

  q = collections.deque([G])
  vertex_map = { G: GraphVertex(G.label) }
  while q:
    v = q.popleft()
    for edge in v.edges:
      # Try to copy vertex e.
      if edge not in vertex_map:
        vertex_map[edge] = GraphVertex(edge.label)
        q.append(edge)
      # Copy edge v->e.
      vertex_map[v].edges.append(vertex_map[edge])
  return vertex_map

G = [GraphVertex(_) for _ in range(3)]
G[0].edges.append(G[1])
G[1].edges.append(G[2])
G[2].edges.append(G[0])

clone = clone_graph(G[0])
print(G[0].edges)
print(clone[G[0]].edges)

class GraphVertex:
  white, gray, black = range(3)
  colors = ['white', 'gray', 'black']
  def __init__(self):
    self.color = GraphVertex.white
    self.edges = []

  def __repr__(self):
    return 'id => %s color => %s edges => [%s]' % (str(id(self)), GraphVertex.colors[self.color], ','.join(str(id(x)) for x in self.edges))

def is_deadlocked(G):
  def has_cycle(cur):
    # Visiting a gray vertex means a cycle.
    if cur.color == GraphVertex.gray:
      return True

    cur.color = GraphVertex.gray  # Marks current vertex as a gray one.
    # Traverse the neighbor vertices.
    if any(next.color != GraphVertex.black and has_cycle(next)
        for next in cur.edges):
      return True
    cur.color = GraphVertex.black  # Marks current vertex as black.
    return False

  return any(vertex.color == GraphVertex.white and has_cycle(vertex) for vertex in G)

G = [GraphVertex() for _ in range(2)]
G[0].edges.append(G[1])
G[1].edges.append(G[0])

assert is_deadlocked(G) == True

G = [GraphVertex() for _ in range(3)]
G[0].edges.append(G[1])
G[1].edges.append(G[2])
G[2].edges.append(G[0])

assert is_deadlocked(G) == True

# star tree
G = [GraphVertex() for _ in range(4)]
G[0].edges.append(G[1])
G[0].edges.append(G[2])
G[0].edges.append(G[3])

assert is_deadlocked(G) == False

# line tree
G = [GraphVertex() for _ in range(4)]
G[0].edges.append(G[1])
G[1].edges.append(G[2])
G[2].edges.append(G[3])
result = is_deadlocked(G)

assert not result
G[3].edges.append(G[1])
result = is_deadlocked(G)

assert not result

# directed binary tree
G = [GraphVertex() for _ in range(7)]
G[0].edges.append(G[1])
G[0].edges.append(G[2])
G[1].edges.append(G[3])
G[1].edges.append(G[4])
G[2].edges.append(G[5])
G[2].edges.append(G[6])
result = is_deadlocked(G)

assert not result

# two seperate cycles
G = [GraphVertex() for _ in range(6)]
G[0].edges.append(G[1])
G[1].edges.append(G[2])
G[2].edges.append(G[0])
G[3].edges.append(G[4])
G[4].edges.append(G[5])
G[5].edges.append(G[3])
result = is_deadlocked(G)

assert result
import collections
import random
import string

def rand_string(length):
  return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))

class GraphVertex:
  def __init__(self, label):
    self.label = label
    self.d = -1
    self.edges = []

  def __repr__(self):
    return '(distance => %d, label => %s, edges => [%s])' % (self.d, self.label, ','.join(
      str(x.label) for x in self.edges))
    # return '(distance => %d, id => %d, edges => [%s])' % (self.d, id(self), ','.join(
    #   str(id(x)) for x in self.edges))
def transform_string(D, s, t):
  StringWithDistance = collections.namedtuple('StringWithDistance', ('candidate_string', 'distance'))
  q = collections.deque([StringWithDistance(s, 0)])
  D.remove(s)  # Marks s as visited by erasing it in D.

  while q:
    f = q.popleft()
    # Returns if we find a match.
    if f.candidate_string == t:
      return f.distance

    # Tries all possible transformations of f.candidate_string.
    for i in range(len(f.candidate_string)):
      for c in string.ascii_lowercase:
        cand = f.candidate_string[:i] + c + f.candidate_string[i + 1:]
        if cand in D:
          D.remove(cand)
          q.append(StringWithDistance(cand, f.distance + 1))
  return -1  # Cannot find a possible transformations.

length = 3
s = rand_string(length)
t = rand_string(length)
n = 720
D = {s, t} | {rand_string(length) for _ in range(n)}

print(D, s, t)
print(transform_string(D, s, t))
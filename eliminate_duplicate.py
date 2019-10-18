import itertools

# @include
class Name:
  def __init__(self, first_name, last_name):
    self.first_name, self.last_name = first_name, last_name

  def __eq__(self, other):
    return self.first_name == other.first_name

  def __lt__(self, other):
    return (self.first_name < other.first_name
              if self.first_name != other.first_name else
              self.last_name < other.last_name)
# @exclude
  def __repr__(self):
    return '%s %s' % (self.first_name, self.last_name)


# @include
def eliminate_duplicate(A):
  A.sort()  # Makes identical elements become neighbors.
  write_idx = 1
  for cand in A[1:]:
    if cand != A[write_idx - 1]:
      A[write_idx] = cand
      write_idx += 1
  del A[write_idx:]
# @exclude


def eliminate_duplicate_pythonic(A):
  A.sort()
  write_idx = 0
  for cand, _ in itertools.groupby(A):
    A[write_idx] = cand
    write_idx += 1
  del A[write_idx:]



A = [Name('Foo', 'Bar'), Name('ABC', 'XYZ'), Name('Foo', 'Widget')]
eliminate_duplicate(A)
assert len(A) == 2
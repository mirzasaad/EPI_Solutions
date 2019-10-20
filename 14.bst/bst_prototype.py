# @include
class BSTNode:
  def __init__(self, data=None, left=None, right=None):
    self.data, self.left, self.right = data, left, right

  def __repr__(self):
    return '%s <= %s => %s' % (self.left.data if self.left else None, self.data, self.right.data if self.right else None)
# @exclude
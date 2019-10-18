# @include
class ListNode:
  def __init__(self, data=0, next_node=None):
    self.data = data
    self.next = next_node
# @exclude

  def __repr__(self):
    return '%s <- %s -> %s' % (self.left and self.left.data, self.data, self.right and self.right.data)
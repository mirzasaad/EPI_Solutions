from bst_prototype import BSTNode
import collections
import sys

# @include
Interval = collections.namedtuple('Interval', ('left', 'right'))

def range_lookup_in_bst(tree, interval):
  def range_lookup(tree):
    if not tree:
      return

    if interval.left <= tree.data <= interval.right:
      range_lookup(tree.left)
      result.append(tree.data)
      range_lookup(tree.right)
    elif interval.left > tree.data:
      range_lookup(tree.right)
    else:# interval.right > tree.data:
      range_lookup(tree.left)
  
  result = []
  range_lookup(tree)
  return result

tree = BSTNode(19)
tree.left = BSTNode(7)
tree.left.left = BSTNode(3)
tree.left.left.left = BSTNode(2)
tree.left.left.right = BSTNode(5)
tree.left.right = BSTNode(11)
tree.left.right.right = BSTNode(17)
tree.left.right.right.left = BSTNode(13)
tree.right = BSTNode(43)
tree.right.left = BSTNode(23)
tree.right.left.right = BSTNode(37)
tree.right.left.right.left = BSTNode(29)
tree.right.left.right.left.right = BSTNode(31)
tree.right.left.right.right = BSTNode(41)
tree.right.right = BSTNode(47)
tree.right.right.right = BSTNode(53)

assert sorted(range_lookup_in_bst(tree, Interval(16, 31))) == [17, 19, 23, 29, 31]
assert len(range_lookup_in_bst(tree, Interval(38, 39))) == 0
assert range_lookup_in_bst(tree, Interval(38, 42)) == [41]
assert len(range_lookup_in_bst(tree, Interval(-1, 1))) == 0
assert len(range_lookup_in_bst(tree, Interval(sys.maxsize - 1, sys.maxsize))) == 0
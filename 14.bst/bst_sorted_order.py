from bst_prototype import BSTNode

# @include
def bst_in_sorted_order(tree):
  s, result = [], []

  while s or tree:
    if tree:
      s.append(tree)
      # Going left.
      tree = tree.left
    else:
      # Going up.
      tree = s.pop()
      result.append(tree.data)
      # Going right.
      tree = tree.right
  return result
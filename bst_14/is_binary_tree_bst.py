from binary_tree_prototype import BinaryTreeNode

def is_binary_tree_bst(tree, low_range=float('-inf'), high_range=float('inf')):
  if not tree:
    return True
  elif not low_range <= tree.data <= high_range:
    return False
  return (is_binary_tree_bst(tree.left, low_range, tree.data) and is_binary_tree_bst(tree.right, tree.data, high_range))

def is_binary_tree_bst_alternative(tree):
  def inorder_traversal(tree):
    if not tree:
      return True
    elif not inorder_traversal(tree.left):
      return False
    elif prev[0] and prev[0].data > tree.data:
      return False
    prev[0] = tree
    return inorder_traversal(tree.right)
  prev = [None]
  return inorder_traversal(tree)

#      3
#    2   5
#  1    4 6
tree = BinaryTreeNode(3)
tree.left = BinaryTreeNode(2)
tree.left.left = BinaryTreeNode(1)
tree.right = BinaryTreeNode(5)
tree.right.left = BinaryTreeNode(4)
tree.right.right = BinaryTreeNode(6)
# should output True.
assert is_binary_tree_bst(tree)
assert is_binary_tree_bst_alternative(tree)
#      10
#    2   5
#  1    4 6
tree.data = 10
# should output False.
assert not is_binary_tree_bst(tree)
assert not is_binary_tree_bst_alternative(tree)
# should output True.
assert is_binary_tree_bst(None)
assert is_binary_tree_bst_alternative(None)

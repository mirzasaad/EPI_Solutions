from binary_tree_prototype import BinaryTreeNode

def has_path_sum(root, remaining_weight):
  if not root:
    return False
  elif not root.left and not root.right:#leaf
    return remaining_weight - root.data == 0

  return (has_path_sum(root.left, remaining_weight - root.data) or
          has_path_sum(root.right, remaining_weight - root.data))

#      3 
#    2   5
#  1    4 6
tree = BinaryTreeNode(3)
assert has_path_sum(tree, 3)
tree.left = BinaryTreeNode(2)
assert has_path_sum(tree, 5)
tree.left.left = BinaryTreeNode(1)
assert has_path_sum(tree, 6)
tree.right = BinaryTreeNode(5)
assert has_path_sum(tree, 8)
assert not has_path_sum(tree, 7)
tree.right.left = BinaryTreeNode(4)
assert has_path_sum(tree, 12)
assert not has_path_sum(tree, 1)
assert not has_path_sum(tree, 3)
assert not has_path_sum(tree, 5)
tree.right.right = BinaryTreeNode(6)
assert has_path_sum(tree, 6)
assert not has_path_sum(tree, 7)
assert has_path_sum(tree, 14)
assert not has_path_sum(tree, -1)
assert not has_path_sum(tree, 2**64 - 1)
assert not has_path_sum(tree, -2**64)
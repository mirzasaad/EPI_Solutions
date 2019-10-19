from binary_tree_prototype import BinaryTreeNode

def binary_tree_depth_order(tree):
  if not tree:
    return []
  result, curr_depth_nodes = [], [tree]
  while curr_depth_nodes:
    result.append([current.data for current in curr_depth_nodes])
    curr_depth_nodes = [
      child
      for current in curr_depth_nodes for child in (current.left, current.right) if child
    ]
  return result
#       3
#     2   5
#   1    4 6
# 10
#   13
tree = BinaryTreeNode(3)
tree.left = BinaryTreeNode(2)
tree.left.left = BinaryTreeNode(1)
tree.left.left.left = BinaryTreeNode(0)
tree.left.left.left.right = BinaryTreeNode(13)
tree.right = BinaryTreeNode(5)
tree.right.left = BinaryTreeNode(4)
tree.right.right = BinaryTreeNode(6)

print(binary_tree_depth_order(tree))
assert binary_tree_depth_order(tree) == [[3], [2, 5], [1, 4, 6], [0], [13]]
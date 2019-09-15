from binary_tree_prototype import BinaryTreeNode

def lca(node_0, node_1):
  def get_depth(node):
    depth = 0
    while node:
      depth += 1
      node = node.parent
    return depth

  depth_0, depth_1 = get_depth(node_0), get_depth(node_1)
  if depth_1 > depth_0:
    node_0, node_1 = node_1, node_0
  
  diff = abs(depth_0 - depth_1)

  while diff:
    diff -= 1
    node_0 = node_0.parent

  while node_0 is not node_1:
    node_0, node_1 = node_0.parent, node_1.parent

  return node_0
#      3
#    2   5
#  1    4 6
root = BinaryTreeNode(3, None, None, None)
root.left = BinaryTreeNode(2, None, None, root)
root.left.left = BinaryTreeNode(1, None, None, root.left)
root.right = BinaryTreeNode(5, None, None, root)
root.right.left = BinaryTreeNode(4, None, None, root.right)
root.right.right = BinaryTreeNode(6, None, None, root.right)

# should output 3
assert lca(root.left, root.right).data == 3
print(lca(root.left, root.right).data)
# should output 5
assert lca(root.right.left, root.right.right).data == 5
print(lca(root.right.left, root.right.right).data)
# should output 3
assert lca(root.left, root.right.left).data == 3
print(lca(root.left, root.right.left).data)
# should output 2
assert lca(root.left, root.left.left).data == 2
print(lca(root.left, root.left.left).data)


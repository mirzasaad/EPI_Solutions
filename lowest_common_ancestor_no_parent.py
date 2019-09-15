from binary_tree_prototype import BinaryTreeNode
from collections import namedtuple

# go to left and right node and check if nodes match (add match node from child to parent) 
def lca(tree, node0, node1):
  Status = namedtuple ('Status' ,('num_target_nodes' , 'ancestor'))
  def lca_helper(root, node0, node1):
    if not root:
      return Status(0, None)

    left = lca_helper(root.left, node0, node1)
    if left.num_target_nodes == 2:
      return left

    right = lca_helper(root.right, node0, node1)
    if right.num_target_nodes == 2:
      return right

    num_target_nodes = left.num_target_nodes + right.num_target_nodes + int(root is node0) + int(root is node1)
    # print(root.data, num_target_nodes)
    return Status(num_target_nodes, root if num_target_nodes == 2 else None)
  return lca_helper(tree, node0, node1).ancestor

#      3
#    2   5
#  1    4 6
tree = BinaryTreeNode(3)
tree.left = BinaryTreeNode(2)
tree.left.left = BinaryTreeNode(1)
tree.right = BinaryTreeNode(5)
tree.right.left = BinaryTreeNode(4)
tree.right.right = BinaryTreeNode(6)
# should output 3
x = lca(tree, tree.left, tree.right)
assert x.data == 3
print(x.data)
# should output 5
x = lca(tree, tree.right.left, tree.right.right)
assert x.data == 5
print(x.data)
# should output 5
x = lca(tree, tree.right, tree.right.right)
assert x.data == 5
print(x.data)
# should output 3
x = lca(tree, tree, tree.left.left)
assert x.data == 3
print(x.data)
# should output 2
x = lca(tree, tree.left, tree.left.left)
assert x.data == 2
print(x.data)
from binary_tree_prototype import BinaryTreeNode

def tree_traversal_inorder_iterative(tree):
  stack, result = [], []
  while tree or stack:
    if tree:
      stack.append(tree)
      tree = tree.left
    else:
      tree = stack.pop()
      result.append(tree.data)
      tree = tree.right
  return result

#           -
#           
#        *    50
#
#     +     +
#
#   /   3 6   5
#
# 22  11
tree = BinaryTreeNode('-')
tree.left = BinaryTreeNode('*')
tree.left.left = BinaryTreeNode('+')
tree.left.left.right = BinaryTreeNode('3')
tree.left.left.left = BinaryTreeNode('/')
tree.left.left.left.left = BinaryTreeNode('22')
tree.left.left.left.right = BinaryTreeNode('11')
tree.left.right = BinaryTreeNode('+')
tree.left.right.left = BinaryTreeNode('6')
tree.left.right.right = BinaryTreeNode('5')
tree.right = BinaryTreeNode('50')

assert tree_traversal_inorder_iterative(tree) == ['22', '/', '11', '+', '3', '*', '6', '+', '5', '-', '50']


from binary_tree_prototype import BinaryTreeNode

def tree_traversal_preorder_iterative(tree):
  path, result = [tree], []
  while path:
    current = path.pop()
    if current:
      result.append(current.data)
      path += [current.right, current.left]
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

assert tree_traversal_preorder_iterative(tree) == ['-', '*', '+', '/', '22', '11', '3', '+', '6', '5', '50']
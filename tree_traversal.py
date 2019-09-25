from binary_tree_prototype import BinaryTreeNode

def tree_travesal(root):
  if root:
    # print('Preorder: %s' % root.data)
    tree_travesal(root.left)
    print('Inorder: %s' % root.data)
    tree_travesal(root.right)
    # print('Postorder: %s' % root.data)
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

tree_travesal(tree)
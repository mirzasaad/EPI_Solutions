from binary_tree_prototype import BinaryTreeNode
from collections import namedtuple

def is_balanced_binary_tree(tree):
  BalancedStatusWithHeight = namedtuple('BalancedStatusWithHeight', ('balanced', 'height'))

  def check_balance(root):
    if not root:
      return BalancedStatusWithHeight(True, -1)

    left = check_balance(root.left)
    if not left.balanced:
      return BalancedStatusWithHeight(False, 0)
    
    right = check_balance(root.right)
    if not right.balanced:
      return BalancedStatusWithHeight(False, 0)

    height = max(left.height, right.height) + 1
    is_balance = abs(left.height - right.height) <= 1
    # print('data => %s height => %d is_balance => %d' % (root.data, height, is_balance))
    return BalancedStatusWithHeight(is_balance, height)

  return check_balance(tree).balanced
#  balanced binary tree test
#      3
#    2   5
#  1    4 6
#0
tree = BinaryTreeNode('3')
tree.left = BinaryTreeNode('2')
tree.left.left = BinaryTreeNode('1')
tree.right = BinaryTreeNode('5')
tree.right.left = BinaryTreeNode('4')
tree.right.right = BinaryTreeNode('6')
assert is_balanced_binary_tree(tree)
print(is_balanced_binary_tree(tree))
# Non-balanced binary tree test.
tree = BinaryTreeNode('0')
tree.left = BinaryTreeNode('1')
tree.left.left = BinaryTreeNode('2')
assert not is_balanced_binary_tree(tree)
print(is_balanced_binary_tree(tree))
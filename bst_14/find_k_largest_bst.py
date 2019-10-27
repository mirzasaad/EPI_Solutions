from binary_tree_prototype import BinaryTreeNode
import random
import sys


# @include
def find_k_largest_in_bst(tree, k):
  def find_k_largest_in_bst_helper(tree):
    # Perform reverse inorder traversal.
    if tree and len(k_largest_elements) < k:
      find_k_largest_in_bst_helper(tree.right)
      if len(k_largest_elements) < k:
        k_largest_elements.append(tree.data)
        find_k_largest_in_bst_helper(tree.left)
  k_largest_elements = []
  find_k_largest_in_bst_helper(tree)
  return k_largest_elements

#      3
#    2   5
#  1    4 6
tree = BinaryTreeNode(3)
tree.left = BinaryTreeNode(2)
tree.left.left = BinaryTreeNode(1)
tree.right = BinaryTreeNode(5)
tree.right.left = BinaryTreeNode(4)
tree.right.right = BinaryTreeNode(6)
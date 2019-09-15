from binary_tree_prototype import BinaryTreeNode

def is_symmetric(tree):
  def check_symmetric(subtree0, subtree1):
    if not subtree0 and not subtree1:
      return True
    elif subtree0 and subtree1:
      return (subtree1.data == subtree0.data and
        check_symmetric(subtree0.left, subtree1.right) and
        check_symmetric(subtree0.right, subtree1.left))
    return False
  return not tree or check_symmetric(tree.left, tree.right)

# Non symmetric tree test.
#      3
#    2   5
#  1    4 6
non_symm_tree = BinaryTreeNode()
non_symm_tree.left = BinaryTreeNode()
non_symm_tree.left.left = BinaryTreeNode()
non_symm_tree.right = BinaryTreeNode()
non_symm_tree.right.left = BinaryTreeNode()
non_symm_tree.right.right = BinaryTreeNode()
assert not is_symmetric(non_symm_tree)
print(is_symmetric(non_symm_tree))
# Symmetric tree test.
symm_tree = BinaryTreeNode()
symm_tree.left = BinaryTreeNode()
symm_tree.right = BinaryTreeNode()
assert is_symmetric(symm_tree)
print(is_symmetric(symm_tree))
# Empty tree test.
symm_tree = None
assert is_symmetric(symm_tree)
print(is_symmetric(symm_tree))
# traverse(tree)
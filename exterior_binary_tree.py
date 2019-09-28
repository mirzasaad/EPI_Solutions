from binary_tree_prototype import BinaryTreeNode
from reconstruct_preorder import reconstruct_preorder

def create_output_list(L):
  return [l.data for l in L]

def exterior_binary_tree(tree):
  def is_leaf(node):
    return not node.left and not node.right
  
  # Computes the nodes from the root to the leftmost leaf followed by all
  # the leaves in subtree.

  def left_boundary_and_leaves(subtree, is_boundary):
    if not subtree:
      return []

    return (([subtree] if is_boundary or is_leaf(subtree) else []) + left_boundary_and_leaves(subtree.left, is_boundary) + left_boundary_and_leaves(subtree.right, is_boundary and not subtree.left))

  # Computes the leaves in left-to-right order followed by the rightmost
  # leaf to the root path in subtree.

  def right_boundary_and_leaves(subtree, is_boundary):
    if not subtree:
      return []
    
    return (right_boundary_and_leaves(subtree.left, is_boundary and not subtree.right) + right_boundary_and_leaves(subtree.right, is_boundary) + ([subtree] if is_boundary or is_leaf(subtree) else []))

  return ([tree] + left_boundary_and_leaves(tree.left, is_boundary=True) + right_boundary_and_leaves(tree.right, is_boundary=True)) if tree else []

tree = BinaryTreeNode(0)

left_temp = BinaryTreeNode(2, left=BinaryTreeNode(1), right=BinaryTreeNode(3))
right_temp = BinaryTreeNode(6, left=BinaryTreeNode(5), right=BinaryTreeNode(7))
tree.left = BinaryTreeNode(4, left_temp, right_temp)

left_temp = BinaryTreeNode(10, left=BinaryTreeNode(9), right=BinaryTreeNode(11))
right_temp = BinaryTreeNode(13, left=BinaryTreeNode(12), right=BinaryTreeNode(14))
tree.right = BinaryTreeNode(15, left_temp, right_temp)

assert [node.data for node in exterior_binary_tree(tree)] == [0, 4, 2, 1, 3, 5, 7, 9, 11, 12, 14, 13, 15]

tree = None

# The example in the book.
A = [314, 6, 271, 28, 0, 561, 3, 17, 6, 2, 1, 401, 641, 257, 271, 28]
tree = reconstruct_preorder([
    A[0], A[1], A[2], A[3], None, None, A[4], None, None, A[5], None, A[6],
    A[7], None, None, None, A[8], A[9], None, A[10], A[11], None, A[12],
    None, None, A[13], None, None, A[14], None, A[15], None, None
])

assert create_output_list(exterior_binary_tree(
    tree)) == [314, 6, 271, 28, 0, 17, 641, 257, 28, 271, 6]

tree.left.left = None
print(create_output_list(exterior_binary_tree(tree)))
assert create_output_list(exterior_binary_tree(
    tree)) == [314, 6, 561, 3, 17, 641, 257, 28, 271, 6]

tree.right.right = None
assert create_output_list(
    exterior_binary_tree(tree)) == [314, 6, 561, 3, 17, 641, 257, 1, 2, 6]

tree.right = None
assert create_output_list(
    exterior_binary_tree(tree)) == [314, 6, 561, 3, 17]
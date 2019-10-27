from binary_tree_prototype import BinaryTreeNode


# @include
def rebuild_bst_from_preorder(preorder_sequence):
  if not preorder_sequence:
    return None

  transition_point = next((i for i, a in enumerate(preorder_sequence) if a > preorder_sequence[0]), len(preorder_sequence))

  return BinaryTreeNode(
    preorder_sequence[0],
    rebuild_bst_from_preorder(preorder_sequence[1: transition_point]),
    rebuild_bst_from_preorder(preorder_sequence[transition_point:]),
  )
# @exclude

preorder_sequence = [43,23,37,29,31,41,47,53]

tree = rebuild_bst_from_preorder(preorder_sequence)

assert tree.left.data == 23
assert tree.left.right.data == 37
assert tree.left.right.right.data == 41
assert tree.left.right.left.data == 29
assert tree.left.right.left.right.data == 31
assert tree.right.data == 47
assert tree.right.right.data == 53
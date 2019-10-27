from binary_tree_prototype import BinaryTreeNode


# @include
def rebuild_bst_from_preorder(preorder_sequence):
  def rebuild_bst_from_preorder_from_range(lower_bound, upper_bound):
    if root_idx[0] == len(preorder_sequence):
      return None

    root = preorder_sequence[root_idx[0]]
    if not lower_bound <= root <= upper_bound:
      return None

    root_idx[0] += 1
    # Note that rebuild_bst_from_preorder_on_value_range updates root_idx[0].
    # So the order of following two calls are critical.
    left = rebuild_bst_from_preorder_from_range(lower_bound, root)
    right = rebuild_bst_from_preorder_from_range(root, upper_bound)

    return BinaryTreeNode(root, left, right)

  root_idx = [0]
  return rebuild_bst_from_preorder_from_range(float('-inf'), float('inf'))

preorder_sequence = [43,23,37,29,31,41,47,53]

tree = rebuild_bst_from_preorder(preorder_sequence)

assert tree.left.data == 23
assert tree.left.right.data == 37
assert tree.left.right.right.data == 41
assert tree.left.right.left.data == 29
assert tree.left.right.left.right.data == 31
assert tree.right.data == 47
assert tree.right.right.data == 53
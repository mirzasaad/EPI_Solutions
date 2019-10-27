from binary_tree_prototype import BinaryTreeNode

def build_min_height_bst_from_sorted_array(A):
  def build_min_height_bst_from_sorted_sub_array(start, end):
    if start >= end:
      return None
    mid = (start + end) // 2
    return BinaryTreeNode(
      A[mid],
      build_min_height_bst_from_sorted_sub_array(start, mid),
      build_min_height_bst_from_sorted_sub_array(mid + 1, end),
    )
  return build_min_height_bst_from_sorted_sub_array(0, len(A))

A = [2,3,5,7,11,13,17,19,23]
tree = build_min_height_bst_from_sorted_array(A)
assert tree.right.right.data == 23
assert tree.left.left.data == 3
assert tree.left.left.left.data == 2
print(tree.right)
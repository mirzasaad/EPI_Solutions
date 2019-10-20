from binary_tree_prototype import BinaryTreeNode

def binary_tree_from_preorder_inorder(preorder, inorder):
  inorder_indexes = {data:i for i, data in enumerate(inorder)}
  
  def preorder_inorder_helper(preorder_start, preorder_end, inorder_start, inorder_end):

    if (preorder_end <= preorder_start or inorder_end <= inorder_start):
      return None
    root_index_inorder = inorder_indexes[preorder[preorder_start]]
    left_subtree_size = root_index_inorder - inorder_start

    return BinaryTreeNode(
      preorder[preorder_start],
      preorder_inorder_helper(
        preorder_start + 1, preorder_start + 1 + left_subtree_size,
        inorder_start, root_index_inorder,
      ),
      preorder_inorder_helper(
        preorder_start + 1 + left_subtree_size, preorder_end,
        root_index_inorder + 1, inorder_end,
      )
    )
  return preorder_inorder_helper(0, len(preorder), 0, len(inorder))
  # def tree_preorder_inorder_helper()

preorder = [1, 2, 4, 8, 9, 10, 11, 5, 3, 6, 7]
inorder = [8, 4, 10, 9, 11, 2, 5, 1, 6, 3, 7]
tree = binary_tree_from_preorder_inorder(preorder, inorder)
print(tree)
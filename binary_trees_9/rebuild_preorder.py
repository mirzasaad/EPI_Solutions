from binary_tree_prototype import BinaryTreeNode

def reconstruct_preorder(preorder):
  def reconstruct_preorder_helper(preorder_iter):
    node = next(preorder_iter)
    if (node is None):
      return None
    
    left = reconstruct_preorder_helper(preorder_iter)
    right = reconstruct_preorder_helper(preorder_iter)
    return BinaryTreeNode(node, left, right)
  return reconstruct_preorder_helper(iter(preorder))

preorder = [1, None, None]
result = reconstruct_preorder(preorder)
assert result.data == 1 and not result.left and not result.right

preorder = [1, None, 2, None, None]
result = reconstruct_preorder(preorder)
assert result.data == 1 and not result.left and result.right.data == 2

preorder = [1, None, 2, 3, None, None, None]
result = reconstruct_preorder(preorder)
assert result.data == 1 and not result.left and result.right.data == 2 and result.right.left.data == 3 and not result.right.right
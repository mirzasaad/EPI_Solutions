from binary_tree_prototype import BinaryTreeNode
from reconstruct_preorder import reconstruct_preorder

def consntruct_right_sibling(tree):
  def populate_children_next_field(start_node):
    while start_node and start_node.left:
      start_node.left.next = start_node.right
      start_node.right.next = start_node.next and start_node.next.left
      start_node = start_node.next
  while tree:
    populate_children_next_field(tree)
    tree = tree.left

tree = BinaryTreeNode(0)

left_temp = BinaryTreeNode(2, left=BinaryTreeNode(1), right=BinaryTreeNode(3))
right_temp = BinaryTreeNode(6, left=BinaryTreeNode(5), right=BinaryTreeNode(7))
tree.left = BinaryTreeNode(4, left_temp, right_temp)

left_temp = BinaryTreeNode(10, left=BinaryTreeNode(9), right=BinaryTreeNode(11))
right_temp = BinaryTreeNode(13, left=BinaryTreeNode(12), right=BinaryTreeNode(14))
tree.right = BinaryTreeNode(15, left_temp, right_temp)

tree_travesal(tree)
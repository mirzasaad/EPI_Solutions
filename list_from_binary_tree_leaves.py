from binary_tree_prototype import BinaryTreeNode

def create_list_of_leaves(tree):
  if not tree:
    return []
  elif not tree.left and not tree.right:
    return [tree]

  return create_list_of_leaves(tree.left) + create_list_of_leaves(tree.right)

#      3
#    2   5
#  1    4 6
tree = BinaryTreeNode(3)
tree.left = BinaryTreeNode(2)
L = create_list_of_leaves(tree)
assert len(L) == 1 and L[0].data == 2

tree.left.left = BinaryTreeNode(1)
tree.right = BinaryTreeNode(5)
tree.right.left = BinaryTreeNode(4)
tree.right.right = BinaryTreeNode(6)
L = create_list_of_leaves(tree)
output = []
# should output 1, 4, 6
for l in L:
    output.append(l.data)
    print(l.data)
golden_res = [1, 4, 6]
assert output == golden_res
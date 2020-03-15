# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        def collect(nodes, node):
            if not node:
                return
            else:
                collect(nodes, node.left)
                nodes.append(node.val)
                collect(nodes, node.right)

        def construct(nodes, i, j):
            if i > j:
                return None
            elif i == j:
                return TreeNode(nodes[i])
            else:
                node = TreeNode(nodes[(i + j) // 2])
                node.left = construct(nodes, i, (i + j) // 2 - 1)
                node.right = construct(nodes, (i + j) // 2 + 1, j)
                return node

        nodes = []
        collect(nodes, root)

        return construct(nodes, 0, len(nodes) - 1)

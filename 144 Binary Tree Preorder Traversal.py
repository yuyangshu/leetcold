# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        def traverse(node: TreeNode, results: List[int]) -> None:
            if not node:
                return
            else:
                results.append(node.val)
                if node.left:
                    traverse(node.left, results)
                if node.right:
                    traverse(node.right, results)

        results = []
        traverse(root, results)

        return results

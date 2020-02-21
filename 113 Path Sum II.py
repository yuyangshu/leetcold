# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        def is_valid_path(node: TreeNode, history: List[int], current_sum: int, target: int, results: List[int]) -> None:
            if node:
                if not node.left and not node.right and node.val + current_sum == target:
                    results.append(history + [node.val])
                else:
                    for child in [node.left, node.right]:
                        is_valid_path(child, history + [node.val], node.val + current_sum, target, results)

        results = []
        is_valid_path(root, [], 0, sum, results)

        return results

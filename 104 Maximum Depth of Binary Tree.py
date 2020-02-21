# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        import itertools

        previous = [root] if root is not None else []
        count = len(previous)

        while previous:
            chain = itertools.chain.from_iterable([[node.left, node.right] for node in previous if node])
            previous = [node for node in chain if node is not None]

            if len(previous) > 0:
                count += 1

        return count

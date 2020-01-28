# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def mirror(left: TreeNode, right: TreeNode) -> bool:
            if left is None and right is None:
                return True

            if (left is None) ^ (right is None):
                return False
            
            return left.val == right.val and mirror(left.left, right.right) and mirror(left.right, right.left)
        
        if not root:
            return True
        
        return mirror(root.left, root.right)

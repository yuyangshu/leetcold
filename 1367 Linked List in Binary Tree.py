# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:
        def traverse(tree_node: TreeNode):
            if try_from(head, tree_node):
                return True
            else:
                return tree_node.left and traverse(tree_node.left) or tree_node.right and traverse(tree_node.right)

        def try_from(list_node: ListNode, tree_node: TreeNode):
            if not list_node:
                return True
            elif not tree_node:
                return False
            else:
                return list_node.val == tree_node.val and (try_from(list_node.next, tree_node.left) or try_from(list_node.next, tree_node.right))

        return not head or traverse(root)

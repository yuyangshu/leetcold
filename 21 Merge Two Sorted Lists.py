# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        elif not l2:
            return l1

        new_list = ListNode()
        head = new_list
        while l1 and l2:
            if l1.val < l2.val:
                new_list.next = l1
                l1 = l1.next
            else:
                new_list.next = l2
                l2 = l2.next

            new_list = new_list.next
        else:
            if l2:
                new_list.next = l2
            elif l1:
                new_list.next = l1

        return head.next

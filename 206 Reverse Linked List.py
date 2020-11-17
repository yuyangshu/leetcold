# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev, next = None, None

        while head:
            prev = head.next
            head.next = next
            if prev:
                next = head
                head = prev
            else:
                return head

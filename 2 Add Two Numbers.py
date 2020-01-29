# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode("")
        current = dummy
        carry = 0

        while l1 is not None and l2 is not None:
            value = l1.val + l2.val + carry
            current.next = ListNode(value % 10)

            current = current.next
            carry = value // 10
            l1 = l1.next
            l2 = l2.next
        else:
            x = l2 if l1 is None else l1

            while x is not None:
                value = x.val + carry
                current.next = ListNode(value % 10)

                current = current.next
                carry = value // 10
                x = x.next
            else:
                if carry > 0:
                    current.next = ListNode(carry)
        
        return dummy.next
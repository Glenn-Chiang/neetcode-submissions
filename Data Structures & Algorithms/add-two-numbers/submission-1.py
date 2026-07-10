# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode()

        a, b, current = l1, l2, res
        carry = 0
        while a or b:
            a_val = a.val if a else 0
            b_val = b.val if b else 0
            sum = a_val + b_val + carry
            if sum >= 10:
                carry = 1
                current.next = ListNode(sum - 10)
            else:
                carry = 0
                current.next = ListNode(sum)
            
            # Move pointers
            if a:
                a = a.next
            if b:
                b = b.next
            current = current.next

        if carry > 0:
            current.next = ListNode(carry)

        return res.next
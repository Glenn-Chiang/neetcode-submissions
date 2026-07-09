# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Split list into two halves, using fast and slow pointers
        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
    
        l1 = head # First half 
        l2 = slow.next # Second half
        slow.next = None # Detach second half from first half

        l2 = self.rev(l2) # Reverse second half

        # Merge lists
        while l2:
            tmp1, tmp2 = l1.next, l2.next
            l1.next = l2
            l2.next = tmp1
            l1, l2 = tmp1, tmp2

    def rev(self, head):
        current = head
        res = None
        while current:
            nextNode = current.next
            current.next = res
            res = current
            current = nextNode
        return res
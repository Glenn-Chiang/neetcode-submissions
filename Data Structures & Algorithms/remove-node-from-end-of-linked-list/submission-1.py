# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:        
        # Initialize fast pointer
        fast = head
        # Initialize slow pointer at dummy node before head
        slow = ListNode()
        slow.next = head
        
        # Move fast pointer n nodes ahead of slow pointer
        for i in range(n):
            fast = fast.next
        
        # If fast pointer is null, the first node is to be removed
        if not fast:
            return head.next
        
        # Move both pointers until fast pointer reaches end of list
        while fast:
            fast = fast.next
            slow = slow.next

        # Now slow pointer is just before node to be removed
        slow.next = slow.next.next
        return head
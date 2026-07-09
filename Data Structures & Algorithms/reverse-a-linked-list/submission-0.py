# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curNode = head
        newHead = None
        while curNode != None:
            nextNode = curNode.next
            curNode.next = newHead
            newHead = curNode
            curNode = nextNode
        return newHead
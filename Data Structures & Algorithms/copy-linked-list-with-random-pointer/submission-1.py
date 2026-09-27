"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        node_map = {}
        copy = Node(0)

        cur_head, cur_copy = head, copy
        while cur_head:
            new_node = Node(cur_head.val)
            node_map[cur_head] = new_node
            cur_copy.next = new_node
            cur_copy = cur_copy.next
            cur_head = cur_head.next

        cur_head, cur_copy = head, copy.next
        while cur_head:
            if cur_head.random:
                cur_copy.random = node_map[cur_head.random]
            cur_head = cur_head.next
            cur_copy = cur_copy.next
        
        return copy.next


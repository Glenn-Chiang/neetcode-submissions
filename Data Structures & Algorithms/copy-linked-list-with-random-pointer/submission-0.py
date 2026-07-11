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
        node_map = {} # Map original node to copy node
        copy = Node(0) # Dummy head of copy list

        # Create copy of list
        cur_head, prev = head, copy
        while cur_head:
            new_node = Node(cur_head.val)
            node_map[cur_head] = new_node # Map original node to copy node
            prev.next = new_node
            prev = prev.next
            cur_head = cur_head.next

        # Iterate over copy list to set random pointers
        cur_head, cur_copy = head, copy.next
        while cur_head:
            # Map original random node to the copied version of that random node
            # Set current node's random pointer to the copied random node, not the original random node
            if cur_head.random:
                cur_copy.random = node_map[cur_head.random]
            cur_head = cur_head.next
            cur_copy = cur_copy.next

        return copy.next
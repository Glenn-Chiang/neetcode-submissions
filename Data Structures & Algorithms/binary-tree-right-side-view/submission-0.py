# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        res = []
        queue = deque()
        queue.append(root)

        while queue:
            level_length = len(queue)
            # Iterate over current level
            for i in range(level_length):
                current_node = queue.popleft()
                # If this is the last node in the current level, add its value to res
                if i == level_length - 1:
                    res.append(current_node.val)
                
                if current_node.left:
                    queue.append(current_node.left)
                if current_node.right:
                    queue.append(current_node.right)
            
        return res







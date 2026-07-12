# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        queue = deque()
        res = []
        
        queue.append(root)
        while queue:
            level_len = len(queue) # Number of nodes in current level
            level = []
            # Iterate over nodes in current level
            for i in range(level_len):
                current_node = queue.popleft()
                level.append(current_node.val)
                # Enqueue children
                if current_node.left:
                    queue.append(current_node.left)
                if current_node.right:
                    queue.append(current_node.right)
                    
            res.append(level)

        return res
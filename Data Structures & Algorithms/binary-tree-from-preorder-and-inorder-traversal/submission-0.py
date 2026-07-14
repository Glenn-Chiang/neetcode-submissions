# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Build hash map mapping each inorder value to its index
        inorder_map = {}
        for i in range(len(inorder)):
            inorder_map[inorder[i]] = i
        
        # Index of current root node in preorder list
        preorder_idx = 0

        def dfs(left, right):
            nonlocal preorder_idx

            if left > right:
                return None
            
            root_val = preorder[preorder_idx]
            root = TreeNode(root_val)
            preorder_idx += 1

            # Index of root node in inorder list
            mid = inorder_map[root_val]

            # Build left subtree with inorder [left, mid-1]
            root.left = dfs(left, mid - 1)
            # Build right subtree with inorder [mid+1, right]
            root.right = dfs(mid + 1, right)

            return root
        
        return dfs(0, len(inorder) - 1)

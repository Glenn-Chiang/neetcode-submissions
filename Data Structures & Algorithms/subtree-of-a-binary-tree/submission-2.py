# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def dfs(tree, subtree):
            if same_tree(tree, subtree):
                return True
            if not tree:
                return False
            return dfs(tree.left, subtree) or dfs(tree.right, subtree)

        def same_tree(a, b):
            if not a and not b:
                return True
            if not a or not b:
                return False
            return a.val == b.val and same_tree(a.left, b.left) and same_tree(a.right, b.right)
        
        return dfs(root, subRoot)

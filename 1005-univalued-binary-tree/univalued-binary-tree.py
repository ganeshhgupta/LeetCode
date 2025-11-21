# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        
        val = root.val

        def dfs(n):
            if not n:
                return True
            
            if n.val != val:
                return False
            
            return dfs(n.left) and dfs(n.right)
        
        return dfs(root)
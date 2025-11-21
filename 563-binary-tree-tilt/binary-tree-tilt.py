# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        
        res = 0

        def dfs(n):
            nonlocal res 

            if not n:
                return 0
            
            left = dfs(n.left)
            right = dfs(n.right)

            res += abs( left - right)
            return left + n.val + right
        
        dfs(root)
        return res
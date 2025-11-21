# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        
        res = float('inf')

        if not root:
            return -1

        li = []
        
        def dfs(n):
            if not n:
                return
            
            dfs(n.left)
            li.append(n.val)
            dfs(n.right)
            return

        dfs(root)
        
        for i in range(1, len(li)):
            res = min(res, li[i] - li[i-1])
        return res
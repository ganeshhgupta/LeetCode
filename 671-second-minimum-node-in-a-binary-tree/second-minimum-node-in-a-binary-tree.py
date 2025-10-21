# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        
        first = root.val 
        second = float('inf')

        def dfs(n):
            nonlocal second

            if not n:
                return

            if first < n.val < second:
                second = n.val

            if n.val == first:
                dfs(n.left)
                dfs(n.right)

        dfs(root)
        
        return second if second != float('inf') else -1
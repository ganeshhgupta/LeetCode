# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        # O(n), O(1)
        def dfs(n):
            if not n: return (0, 0)

            l_rob, l_not = dfs(n.left)
            r_rob, r_not = dfs(n.right)
            rob = l_not + n.val + r_not
            not_rob = max(l_not, l_rob) + max(r_not, r_rob)

            return rob, not_rob
        
        return max( dfs(root) )

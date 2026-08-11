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

            if not n:
                return (0, 0)
            
            left = dfs(n.left)
            right = dfs(n.right)

            rob = n.val + left[1] + right[1]    # take curr val 
                                                # + max val from left subtree if left child val is skipped
                                                # + max val from right subtree if right child val is skipped
            skip = max(left) + max(right)       # skip curr val, take max so far frmo left and right subtrees

            return (rob, skip)
        
        return max(dfs(root))

            
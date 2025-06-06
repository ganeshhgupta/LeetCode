# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        self.res = 0

        def dfs(node, maxVal):
            if not node:
                return 0
            
            self.res += 1 if node.val >= maxVal else 0
            maxVal = max(node.val, maxVal)

            dfs(node.left, maxVal)
            dfs(node.right, maxVal)

        dfs(root, root.val)
        return self.res

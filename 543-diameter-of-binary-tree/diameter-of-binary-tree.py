# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        self.diam = 0
        cache_map = {}

        def dfs(node):
            if not node:
                return 0
            if id(node) in cache_map:
                return cache_map[id(node)]

            left = dfs(node.left)
            right = dfs(node.right)

            self.diam = max(self.diam, left + right)
            cache_map[id(node)] = 1 + max(left, right)
            return cache_map[id(node)]

        dfs(root)
        return self.diam
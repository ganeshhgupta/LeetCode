"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        
        res = 0

        def dfs(n, path):
            nonlocal res

            if not n: return

            if not n.children:
                res = max(res, path) 

            for i in n.children:
                dfs(i , path + 1)
        
        dfs(root, 1)
        return res


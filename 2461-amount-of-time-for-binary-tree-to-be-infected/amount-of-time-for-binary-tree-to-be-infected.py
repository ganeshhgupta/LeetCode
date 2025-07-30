from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        par = {}
        target = None

        def dfs(n):
            nonlocal target
            if not n:
                return
            if n.val == start:
                target = n
            if n.left:
                par[n.left] = n
                dfs(n.left)
            if n.right:
                par[n.right] = n
                dfs(n.right)
        
        dfs(root)
        res = -1
        q = deque([target])
        seen = set([target])

        while q:
            for _ in range(len(q)):
                n = q.popleft()
                for nei in [n.left, n.right, par.get(n)]:
                    if nei and nei not in seen:
                        seen.add(nei)
                        q.append(nei)
            res += 1
        
        return res

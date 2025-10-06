from collections import deque
from typing import List, Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        # O(n), O(n)
        if not root:
            return []

        q = deque([root])
        res = []
        dir = 1

        while q:
            level = []
            for _ in range(len(q)):
                n = q.popleft()
                if n:
                    level.append(n.val)
                    if n.left: q.append(n.left)
                    if n.right: q.append(n.right)

            if dir == -1:
                level.reverse()
            res.append(level)
            dir *= -1

        return res

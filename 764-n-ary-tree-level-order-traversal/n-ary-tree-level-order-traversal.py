"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        
        # O(n), O(n)

        if not root:
            return []
            
        q = deque([root])
        res = []

        while q:
            level = []
            for _ in range(len(q)):

                node = q.popleft()
                if node:
                    level.append(node.val)

                    for nei in node.children:
                        q.append(nei)

            res.append(level.copy())
        
        return res

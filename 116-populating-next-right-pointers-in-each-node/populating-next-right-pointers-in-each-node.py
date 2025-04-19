"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        
        if not root:
            return None

        q = collections.deque()
        q.append(root)
        
        while q:
            l = len(q)
            level = []
            for i in range(l):
                node = q.popleft()
                if node:
                    level.append(node)
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)

            if level:
                for i in range(len(level) - 1):
                    level[i].next = level[i+1]
                level[-1].next = None

        return root
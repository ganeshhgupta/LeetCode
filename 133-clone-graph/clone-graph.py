"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        visited = {}

        def dfs(n):
            if n in visited:
                return visited[n]

            # Clone the node
            copy = Node(n.val)
            visited[n] = copy

            # Clone all the neighbors
            for neighbor in n.neighbors:
                copy.neighbors.append(dfs(neighbor))

            return copy

        return dfs(node)        
"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def inorderSuccessor(self, node: 'Node') -> 'Optional[Node]':
        # Case 1: Node has a right child, go down to the leftmost node of that subtree
        if node.right:
            successor = node.right
            while successor.left:
                successor = successor.left
            return successor
        
        # Case 2: No right child, go up until we find a node that is a left child of its parent
        while node.parent and node == node.parent.right:
            node = node.parent
        return node.parent

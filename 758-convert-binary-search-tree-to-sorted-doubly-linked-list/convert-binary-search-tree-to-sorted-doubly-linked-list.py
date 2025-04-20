"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None

        stack = []
        curr = root
        head = None   #left most node
        prev = None   #stores the last visited node

        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left  #traverse and store all left nodes from current root

            node = stack.pop()

            if not head:
                head = node  # First node we visit in-order is the smallest one
            if prev:
                prev.right = node
                node.left = prev

            prev = node  # Mark current node as the last visited
            curr = node.right  # Go to the right subtree

        # Now connect head and tail to make the list circular
        head.left = prev
        prev.right = head

        return head

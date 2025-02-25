# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        stack = []
        curr = root
        n = 0       #just a counter to keep track to total no. of elements

        while curr or stack:

            #traverse upto the left-most child (without 'visiting' any node)
            while curr:
                stack.append(curr)
                curr = curr.left

            #now we're at the left-most chlid. which is also the smallest element in a BST. nice.
            #now..

            #now pop/'visit' it:
            curr = stack.pop()
            n += 1 
            if n == k:
                return curr.val

            #from bottom up, does inorder traversal
            curr = curr.right
            

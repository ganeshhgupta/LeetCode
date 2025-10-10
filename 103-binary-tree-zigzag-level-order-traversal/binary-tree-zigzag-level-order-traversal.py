# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        # O(n), O(n)
        q = deque([root])
        res = []
        dir = 1
        while q:
            l = []
            for i in range(len(q)):
                n = q.popleft()
                if n:
                    q.append(n.left)
                    q.append(n.right)
                    l.append(n.val)
            if dir == -1:
                l.reverse()
            dir = dir * -1

            if l: res.append(l)
        return res
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        res = []

        q = deque() #double ended queue
        q.append(root) #append first level

        while q:
            q_len = len(q) #no. of elements in q at any given level
            level = [] #to store all children from next level

            for i in range(q_len):

                node = q.popleft() #note popleft

                #for every popped node at a level, append its children in q
                #q_len with take care we never traverse more than len of prev level
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
                    
            # after every iteration, append level list to main list
            if level:
                res.insert(0, level)

        return res
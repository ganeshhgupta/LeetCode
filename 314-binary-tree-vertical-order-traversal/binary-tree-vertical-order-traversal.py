# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        #bfs to preserve height

        if not root:
            return []

        cols = defaultdict(list)
        q = deque([(root, 0)]) #send a tuple

        while q:
            qLen = len(q)
            for i in range(qLen):
                node, col = q.popleft()
                if node:
                    cols[col].append(node.val)  #no level list need, direct append to cols[col]
                if node.left:
                    q.append([node.left, col - 1])
                if node.right:
                    q.append([node.right, col + 1])
        print( list(cols) )
        return [cols[x] for x in sorted(cols)]


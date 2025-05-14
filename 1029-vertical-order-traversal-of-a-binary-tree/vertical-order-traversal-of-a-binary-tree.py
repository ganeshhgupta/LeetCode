# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return []

        map = defaultdict(list)
        q = deque([(root, 0, 0)])

        while q:
            node, row, col = q.popleft()
            if node:
                map[col].append((row, node.val))
                q.append((node.left, row + 1, col - 1))
                q.append((node.right, row + 1, col + 1))
        if map:
            print(map)
            res = []
            for i in sorted(map):
                map[i].sort()
                res.append([val for row, val in map[i]])
            return res
        else:
            return []
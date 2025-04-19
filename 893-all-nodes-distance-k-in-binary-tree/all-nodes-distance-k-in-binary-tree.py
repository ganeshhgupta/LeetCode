# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        
        #convert tree to graph using bfs + creating a two-way adjacency list

        g = defaultdict(list)
        q = deque([root])

        while q:
            node = q.popleft()
            if node:
                if node.left:
                    g[node].append(node.left)
                    g[node.left].append(node)
                    q.append(node.left)
                if node.right:
                    g[node].append(node.right)
                    g[node.right].append(node)
                    q.append(node.right)

        visit = set ([target]) #starting point
        res = []
        q = deque([(target, 0)])
        while q:
            node, dist = q.popleft()
            if node:
                if dist == k:
                    res.append(node.val)
                else:
                    for edge in g[node]:
                        if edge not in visit:
                            visit.add(edge)
                            q.append([edge, dist + 1])

        return res


            
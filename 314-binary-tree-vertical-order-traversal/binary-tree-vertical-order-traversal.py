class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []

        map = defaultdict(list)
        q = deque([(root, 0)])

        while q:
            node, col = q.popleft()
            if node:
                map[col].append(node.val)

                q.append((node.left, col - 1))
                q.append((node.right, col + 1))
        if map:
            return [map[i] for i in sorted(map)]
        else:
            return []
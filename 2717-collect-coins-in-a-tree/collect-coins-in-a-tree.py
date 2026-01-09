class Solution:
    def collectTheCoins(self, coins: List[int], edges: List[List[int]]) -> int:
        n = len(coins)
        if n == 1:
            return 0

        # Build graph
        graph = defaultdict(list)
        degree = [0] * n
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            degree[u] += 1
            degree[v] += 1

        # 1) Remove leaf nodes with no coins
        q = deque()
        for i in range(n):
            if degree[i] == 1 and coins[i] == 0:
                q.append(i)

        while q:
            node = q.popleft()
            degree[node] = 0
            for nei in graph[node]:
                if degree[nei] > 0:
                    degree[nei] -= 1
                    if degree[nei] == 1 and coins[nei] == 0:
                        q.append(nei)

        # 2) Remove one more layer: leaf + parent
        q = deque()
        for i in range(n):
            if degree[i] == 1:
                q.append(i)

        # Remove exactly two layers
        for _ in range(2):
            size = len(q)
            for _ in range(size):
                node = q.popleft()
                degree[node] = 0
                for nei in graph[node]:
                    if degree[nei] > 0:
                        degree[nei] -= 1
                        if degree[nei] == 1:
                            q.append(nei)

        # 3) Count remaining nodes
        remaining = sum(1 for i in range(n) if degree[i] > 0)

        if remaining <= 1:
            return 0

        return (remaining - 1) * 2

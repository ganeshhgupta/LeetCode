
class Solution:
    def palindromePath(
        self,
        n: int,
        edges: list[list[int]],
        s: str,
        queries: list[str]
    ) -> list[bool]:

        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        parent = [-1] * n
        depth = [0] * n
        size = [1] * n
        heavy = [-1] * n

        # Build rooted tree
        order = [0]
        for u in order:
            for v in adj[u]:
                if v == parent[u]:
                    continue
                parent[v] = u
                depth[v] = depth[u] + 1
                order.append(v)

        # Find heavy child
        for u in reversed(order):
            best = 0
            for v in adj[u]:
                if parent[v] == u:
                    size[u] += size[v]
                    if size[v] > best:
                        best = size[v]
                        heavy[u] = v

        # Heavy-light decomposition
        head = [0] * n
        pos = [0] * n
        timer = 0

        for u in order:
            if parent[u] == -1 or heavy[parent[u]] != u:
                v = u
                while v != -1:
                    head[v] = u
                    pos[v] = timer
                    timer += 1
                    v = heavy[v]

        # Iterative segment tree
        base = 1
        while base < n:
            base *= 2

        seg = [0] * (2 * base)
        chars = list(s)

        for u in range(n):
            seg[base + pos[u]] = (
                1 << (ord(chars[u]) - ord('a'))
            )

        for i in range(base - 1, 0, -1):
            seg[i] = seg[2 * i] ^ seg[2 * i + 1]

        def update(u, c):
            chars[u] = c
            p = base + pos[u]
            seg[p] = 1 << (ord(c) - ord('a'))

            p //= 2
            while p:
                seg[p] = seg[2 * p] ^ seg[2 * p + 1]
                p //= 2

        def range_xor(l, r):
            l += base
            r += base
            result = 0

            while l <= r:
                if l & 1:
                    result ^= seg[l]
                    l += 1

                if not (r & 1):
                    result ^= seg[r]
                    r -= 1

                l //= 2
                r //= 2

            return result

        def path_xor(u, v):
            result = 0

            while head[u] != head[v]:
                if depth[head[u]] < depth[head[v]]:
                    u, v = v, u

                result ^= range_xor(
                    pos[head[u]], pos[u]
                )
                u = parent[head[u]]

            if depth[u] > depth[v]:
                u, v = v, u

            result ^= range_xor(pos[u], pos[v])
            return result

        ans = []

        for q in queries:
            parts = q.split()

            if parts[0] == "update":
                u = int(parts[1])
                update(u, parts[2])
            else:
                u = int(parts[1])
                v = int(parts[2])

                mask = path_xor(u, v)
                ans.append(
                    (mask & (mask - 1)) == 0
                )

        return ans

class Solution:
    def palindromePath(self, n, edges, s, queries):
        
        g = [[] for _ in range(n)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        par, dep, sz, heavy = [-1]*n, [0]*n, [1]*n, [-1]*n
        order = [0]

        for u in order:
            for v in g[u]:
                if v != par[u]:
                    par[v] = u
                    dep[v] = dep[u] + 1
                    order.append(v)

        for u in order[::-1]:
            for v in g[u]:
                if par[v] == u:
                    sz[u] += sz[v]
                    if heavy[u] == -1 or sz[v] > sz[heavy[u]]:
                        heavy[u] = v

        head, pos = [0]*n, [0]*n
        t = 0
        for u in order:
            if par[u] == -1 or heavy[par[u]] != u:
                v = u
                while v != -1:
                    head[v], pos[v] = u, t
                    t += 1
                    v = heavy[v]

        bit = [0]*(n+1)
        s = list(s)

        def add(i, x):
            i += 1
            while i <= n:
                bit[i] ^= x
                i += i & -i

        def pref(i):
            x = 0
            while i > 0:
                x ^= bit[i]
                i -= i & -i
            return x

        def path(u, v):
            x = 0
            while head[u] != head[v]:
                if dep[head[u]] < dep[head[v]]:
                    u, v = v, u
                x ^= pref(pos[u]+1) ^ pref(pos[head[u]])
                u = par[head[u]]
            if dep[u] > dep[v]:
                u, v = v, u
            return x ^ pref(pos[v]+1) ^ pref(pos[u])

        for u, c in enumerate(s):
            add(pos[u], 1 << (ord(c)-97))

        ans = []
        for q in queries:
            op, u, v = q.split()
            u = int(u)
            if op == "update":
                add(pos[u], (1 << (ord(s[u])-97)) ^
                            (1 << (ord(v)-97)))
                s[u] = v
            else:
                x = path(u, int(v))
                ans.append(x & (x-1) == 0)

        return ans
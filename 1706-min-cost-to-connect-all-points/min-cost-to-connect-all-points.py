class UF:
    def __init__(self, n):
        self.par = list(range(n))
        self.rank = [1] * n

    def find(self, x):
        while x != self.par[x]:
            self.par[x] = self.par[self.par[x]]
            x = self.par[x]
        return x

    def union(self, a, b):
        a, b = self.find(a), self.find(b)

        if a == b:
            return False

        if self.rank[a] < self.rank[b]:
            a, b = b, a

        self.par[b] = a
        self.rank[a] += self.rank[b]
        return True


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        n = len(points)
        edges = []

        for i in range(n):
            for j in range(i + 1, n):
                cost = abs(points[i][0] - points[j][0]) + \
                       abs(points[i][1] - points[j][1])
                edges.append((cost, i, j))

        edges.sort()

        uf = UF(n)
        res = 0
        count = 0

        for cost, i, j in edges:
            if uf.union(i, j):
                res += cost
                count += 1

                if count == n - 1:
                    break

        return res
class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:

        # O(E α(n)), O(E)
        if len(connections) < n - 1:
            return -1

        uf = UnionFind(n)

        components = n

        for a, b in connections:
            if uf.union(a, b):
                components -= 1

        return components - 1
        
        
class UnionFind:

    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX == rootY:
            return False

        if self.rank[rootX] < self.rank[rootY]:
            rootX, rootY = rootY, rootX

        self.parent[rootY] = rootX
        self.rank[rootX] += self.rank[rootY]

        return True



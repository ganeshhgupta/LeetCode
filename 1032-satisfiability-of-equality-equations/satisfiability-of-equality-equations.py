class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:

        uf = UnionFind(26)

        for eq in equations:
            if eq[1] == '=':
                uf.union(ord(eq[0]) - ord('a'), ord(eq[3]) - ord('a'))

        for eq in equations:
            if eq[1] == '!':
                if uf.find(ord(eq[0]) - ord('a')) == uf.find(ord(eq[3]) - ord('a')):
                    return False

        return True
        
class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.rank = [1] * n

    def find(self, x):
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)

        if px == py:
            return False

        # attach smaller tree under larger tree
        if self.rank[px] < self.rank[py]:
            self.par[px] = py
        elif self.rank[px] > self.rank[py]:
            self.par[py] = px
        else:
            self.par[py] = px
            self.rank[px] += 1

        return True

        if pa != pb:
            self.par[pa] = pb



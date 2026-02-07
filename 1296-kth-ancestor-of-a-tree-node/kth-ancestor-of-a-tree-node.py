class TreeAncestor:
    def __init__(self, n: int, parent: list[int]):
        
        LOG = 16  # because 2^16 > 5 * 10^4
        self.up = [[-1] * n for _ in range(LOG)]
        
        # Base case: 2^0 ancestor (direct parent)
        for i in range(n):
            self.up[0][i] = parent[i]
        
        # Build binary lifting table
        for j in range(1, LOG):
            for i in range(n):
                if self.up[j - 1][i] != -1:
                    self.up[j][i] = self.up[j - 1][self.up[j - 1][i]]
    
    def getKthAncestor(self, node: int, k: int) -> int:
        j = 0
        while node != -1 and k > 0:
            if k & 1:
                node = self.up[j][node]
            k = k // 2
            j += 1

        return node

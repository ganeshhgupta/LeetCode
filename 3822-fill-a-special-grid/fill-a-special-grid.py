class Solution:
    def specialGrid(self, n: int) -> List[List[int]]:
        
        # O(4n), O(4n)
        size = 2 ** n
        res = [[0] * size for s in range(size)]
        val = 0
        
        def fill(x, y, sz):
            nonlocal val
            if sz == 1: # does't start filling till we reach res[0][n-1] top-right
                res[x][y] = val
                val += 1
                return
            
            half = sz // 2

            fill(x, y+half, half)
            fill(x+half, y+half, half)
            fill(x+half, y, half)
            fill(x, y, half)
        
        fill(0, 0, size)
        return res


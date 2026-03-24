class Solution:

    def constructProductMatrix(self, grid):

        # 238. Product of Array Except Self
        # O(m.n), O(m.n)
        
        MOD = 12345
        rows, cols = len(grid), len(grid[0])

        # Flatten grid
        arr = [num for row in grid for num in row]
        n = len(arr)

        # Prefix and suffix products with modulo
        pre = [1] * n
        post = [1] * n

        for i in range(1, n):
            pre[i] = (pre[i-1] * arr[i-1]) % MOD

        for i in range(n-2, -1, -1):
            post[i] = (post[i+1] * arr[i+1]) % MOD

        # Build result array
        res_flat = [(pre[i] * post[i]) % MOD for i in range(n)]

        # Convert back to grid
        res = []
        for i in range(0, n, cols):
            res.append(res_flat[i:i+cols])

        return res
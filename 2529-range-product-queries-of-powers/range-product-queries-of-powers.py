class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        
        # O(b + q * b), b = set bits in n, q = queries, O(b) for storing the powers of two (p).
        MOD = 10**9 + 7

        p = []
        i = 0
        while n:
            if n & 1:
                p.append(2**i)
            n >>= 1
            i += 1

        res = []
        for i, j in queries:
            cur = 1
            for k in range(i, j+1):
                cur *= p[k]

            res.append(cur % MOD)
        return res
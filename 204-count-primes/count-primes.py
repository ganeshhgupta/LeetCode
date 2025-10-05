class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0

        s = [True] * n
        s[0] = s[1] = False # 0, 1 are neither prime not comp

        for i in range(2, int(n ** 0.5) + 1):
            if s[i]:
                for j in range( i * i, n, i ):
                        s[j] = False
        
        return sum(s)

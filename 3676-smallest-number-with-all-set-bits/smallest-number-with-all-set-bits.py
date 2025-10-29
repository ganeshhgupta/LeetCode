class Solution:
    def smallestNumber(self, n: int) -> int:
        
        res = 1
        for i in range(n):
            res *= 2
            if res > n:
                return res - 1
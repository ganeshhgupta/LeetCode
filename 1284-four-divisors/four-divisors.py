class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        
        def ifFour(n):
            count = []
            for i in range(1, int(n ** 0.5) + 1):
                if n % i == 0:
                    count.append(i)
                    if i != n // i:
                        count.append(n // i)
                    if len(count) > 4:
                        return 0
            
            if len(count) == 4:
                return sum(count)
            return 0
        
        res = 0
        for n in nums:
            res += ifFour(n)
        
        return res

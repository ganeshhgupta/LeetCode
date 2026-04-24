class Solution:
    def countPermutations(self, complexity: List[int]) -> int:
        MOD = 10**9 + 7
        
        for i in range(1, len(complexity)):
            if complexity[i] <= complexity[0]:
                return 0
        
        # just factorial sum % mod
        res = 1
        for i in range(1, len(complexity)):
            res = (res * i) % MOD
        
        return res
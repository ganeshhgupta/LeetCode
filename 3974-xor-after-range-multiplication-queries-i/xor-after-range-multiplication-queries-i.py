class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        
        # O(q * n), O(1)
        
        MOD = 10**9 + 7
        
        def sim(l, r, k, v):
            for i in range(l, r + 1, k):
                nums[i] = (nums[i] * v) % MOD
        
        for l, r, k, v in queries:
            sim(l, r, k, v)

        res = 0
        for x in nums:
            res ^= x
        
        return res
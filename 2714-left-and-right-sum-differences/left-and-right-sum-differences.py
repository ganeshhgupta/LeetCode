class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        
        # O(n), O(n)
        
        n = len(nums)
        ls = [0] * n
        rs = [0] * n
        res = [0] * n

        for i in range(1, n):
            ls[i] = ls[i-1] + nums[i-1]

        for i in range(n - 2, -1 ,-1):
            rs[i] = rs[i+1] + nums[i+1]

        for i in range(n):
            res[i] = abs( ls[i] - rs[i] )
        
        return res
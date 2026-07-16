class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        
        n = len(nums)
        curr_max = nums[0]
        prefixGcd = []

        for i in range(n):
            curr_max = max(curr_max, nums[i])
            prefixGcd.append(gcd(curr_max, nums[i]))
        
        prefixGcd = sorted(prefixGcd)
        res = 0

        for i in range(n//2):
            res += (gcd(prefixGcd[i], prefixGcd[n-1-i]))
        
        return res



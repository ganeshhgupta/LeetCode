class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        # sliding, O(n), O(1)

        curr = 0
        res = float('inf')
        i = 0

        for j in range(len(nums)):
            curr += nums[j]

            while curr >= target:
                res = min(res, j - i + 1)
                curr -= nums[i]
                i += 1
        
        return 0 if res == float('inf') else res

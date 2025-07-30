class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        res = maxx = curr = 0
        for num in nums:
            if maxx < num:
                maxx = num
                res = curr = 0

            if maxx == num:
                curr += 1
            else:
                curr = 0

            res = max(res, curr)
        return res
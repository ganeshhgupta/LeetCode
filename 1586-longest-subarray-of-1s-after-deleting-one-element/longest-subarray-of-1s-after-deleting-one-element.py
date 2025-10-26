class Solution:
    def longestSubarray(self, nums: List[int]) -> int:

        # O(n), O(1)
        
        left = 0
        zero_count = 0
        res = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zero_count += 1

            while zero_count > 1:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1

            # window length minus 1 because we delete one element
            res = max(res, right - left)

        return res

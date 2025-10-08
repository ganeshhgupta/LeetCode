class Solution:
    def longestSubsequence(self, nums: list[int]) -> int:
        total_xor = 0
        non_zero_count = 0
        
        for x in nums:
            total_xor ^= x
            if x != 0:
                non_zero_count += 1
        
        if non_zero_count == 0:
            return 0
        
        if total_xor != 0:
            return len(nums)
        else:
            return len(nums) - 1

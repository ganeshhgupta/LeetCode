class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        
        l, r = 0, 0
        longest = 0
        zeroes = 0
        for r in range( len(nums) ):
            zeroes += (1 if nums[r] == 0 else 0)

            while zeroes > 1:
                zeroes -= (1 if nums[l] == 0 else 0)
                l += 1
                
            longest = max(longest, r - l)
        return longest
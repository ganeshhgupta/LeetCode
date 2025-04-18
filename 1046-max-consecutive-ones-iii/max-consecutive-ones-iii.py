class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        
        #sliding window, shift l till num zeroes <= k
        max_w = zeroes = 0
        l = 0

        for r in range(len(nums)):
            if nums[r] == 0:
                zeroes += 1
            
            while zeroes > k:
                if nums[l] == 0:
                    zeroes -= 1
                l +=1

            max_w = max(max_w, r - l + 1)

        return max_w
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        LIS = [nums[0]]

        for n in nums:

            l, r = 0, len(LIS)
            while l < r:
                m = l + (r - l) // 2

                if LIS[m] < n:
                    l = m + 1
                else:
                    r = m
            
            if l == len(LIS):
                LIS.append(n)
            else:
                LIS[l] = n
        
        return len(LIS)
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        # O(n log n), O(len(LIS) = n)

        # loop across main array, initial LIS = first element of main array
        # for every value n, do bisect_left to see where can you insert it into the LIS
        # If it's larger than all elements, append it (len(LIS) increases), else, replace the first element >= it

        LIS = [nums[0]]

        for n in nums:

            left, right = 0, len(LIS)
            
            while left < right:
                mid = left + (right - left) // 2
                
                if LIS[mid] < n:
                    left = mid + 1
                else:
                    right = mid
        
            if left == len(LIS):
                LIS.append(n)
            else:
                LIS[left] = n
        
        return len(LIS)

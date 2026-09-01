class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        # O(n log n), O(len(LIS) = n)

        # loop across main array, initial LIS = first element of main array
        # for every value n, do bisect_left to see where can you insert it into the LIS
        # If it's larger than all elements, append it (len(LIS) increases), else, replace the first element >= it

        LIS = [nums[0]]

        for n in nums:
            
            i = bisect_left(LIS, n)

            if i == len(LIS):
                LIS.append(n)
            else:
                LIS[i] = n

        return len(LIS)

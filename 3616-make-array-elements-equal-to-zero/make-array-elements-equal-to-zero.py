class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        
        # O(n), O(1) intuition: pointer bouncing L-R and breaking blocks game

        maxSum = sum(nums)
        leftSum = 0
        res = 0
        
        for n in nums:
            if n == 0:
                if leftSum == maxSum:
                    res += 2  # both
                elif leftSum + 1 == maxSum or leftSum == maxSum + 1:
                    res += 1  # one direction
            
            leftSum += n
            maxSum -= n
        
        return res
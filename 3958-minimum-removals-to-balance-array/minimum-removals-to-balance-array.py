class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:

        '''
        Sort the array
        Use two pointers i (min) and j (max)
        Expand j while condition holds
        Shrink i when needed
        Track largest valid window
        Time: O(n log n)
        Space: O(1)
        '''
        
        nums.sort()
        n = len(nums)

        res = n
        j = 0

        for i in range(n):
            while j < n and nums[j] <= nums[i] * k:
                j += 1

            kept = j - i
            res = min(res, n - kept)

        return res

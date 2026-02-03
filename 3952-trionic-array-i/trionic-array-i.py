class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 4:
            return False

        # check strictrly increasing before p
        p = 0
        while p < n - 1 and nums[p] < nums[p + 1]:
            p += 1
        if not p or p == n - 1:
            return False    

        # check strictly decreasing between p and q
        m = p
        while m < n - 1 and nums[m] > nums[m + 1]:
            m += 1
        if m == p or m == n - 1:
            return False
            
        # check strictly increasing after q
        q = m
        while q < n - 1 and nums[q] < nums[q + 1]:
            q += 1
        
        return q == n - 1
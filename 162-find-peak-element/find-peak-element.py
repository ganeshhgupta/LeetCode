class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r) // 2 + 1
            if nums[m -1] > nums[m]:
                r = m - 1
            else:
                l = m

        return l

'''
Why do we do r = m and not r = m - 1?
When nums[m] > nums[m + 1], this means there's a descending slope — the peak lies at m or to the left of m, so we keep m in the search by doing r = m.

If you did r = m - 1, you might skip over the peak — especially if m itself is the peak.
'''
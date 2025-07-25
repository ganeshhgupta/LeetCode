class Solution(object):
    def maxSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxx = min(nums)
        s = set()
        for n in nums:
            if n > 0:
                s.add(n)
            else:
                maxx = max(maxx, n)
        res = sum(s)
        return res if res > 0 else maxx
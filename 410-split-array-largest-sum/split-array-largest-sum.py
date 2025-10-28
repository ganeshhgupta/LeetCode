class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        
        # O(n log(sum(nums))), O(1)
        # bin search bw max val and sum of nums
        # canSplit counts no. of subbrays whose cur < maxVal
        l, r = max(nums), sum(nums)

        def canSplit(maxVal):
            count = 1
            cur = 0
            for n in nums:
                cur += n
                if cur > maxVal:
                    count += 1
                    cur = n
            
            return count <= k # '<=' cause if there's more, we can shift r = m - 1
        
        res = 0
        while l <= r:
            m = l + (r-l) // 2
            if canSplit(m):
                res = m
                r = m - 1
            else:
                l = m + 1
        
        return res
        

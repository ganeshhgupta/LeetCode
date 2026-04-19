class Solution:
    def minAbsDifference(self, nums, goal):
        
        # O(n.2^(n/2)), O(2^n) doesn't seem good
        
        def subset_sums(arr):
            res = [0]
            for num in arr:
                res += [num + x for x in res]
            return res
        
        n = len(nums)

        a1 = sorted(subset_sums(nums[:n//2]))
        a2 = sorted(subset_sums(nums[n//2:]))
        
        res = float('inf')

        for i, v1 in enumerate(a1):

            target = goal - v1
            j = bisect_left(a2, target)

            # check j (just >= target)
            if j < len(a2):
                res = min(res, abs(v1 + a2[j] - goal))

            # check j-1 (just < target)
            if j > 0:
                res = min(res, abs(v1 + a2[j-1] - goal))
        
        return res
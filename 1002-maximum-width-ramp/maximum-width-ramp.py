class Solution:
    def maxWidthRamp(self, nums):
        n = len(nums)
        st = []
        
        # Step 1: Build a stack of candidate indices where values are strictly decreasing
        # These are the best possible left endpoints, smaller values give better chances for nums[i] <= nums[j]
        
        for i in range(n):
            if not st or nums[i] < nums[st[-1]]:
                st.append(i)

        print(st)
        res = 0
        
        # Step 2: traverse from right
        for j in range(n - 1, -1, -1):
            while st and nums[st[-1]] <= nums[j]:
                i = st.pop()
                res = max(res, j - i)
        
        return res
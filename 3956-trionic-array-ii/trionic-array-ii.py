class Solution:
    def maxSumTrionic(self, nums):
        
        n = len(nums)
        res = -10**30
        l = p = q = 0

        curr = nums[0]

        for r in range(1, n):
            curr += nums[r]

            # strict condition broken
            if nums[r] == nums[r - 1]:
                l = p = q = r
                curr = nums[r]
                continue

            # going down
            if nums[r] < nums[r - 1]:
                # flip: increasing -> decreasing
                if r > 1 and nums[r - 2] < nums[r - 1]:
                    p = r - 1

                    # move l up to q (old valley)
                    while l < q:
                        curr -= nums[l]
                        l += 1

                    # drop negative prefix of first increasing part
                    while l + 1 < p and nums[l] < 0:
                        curr -= nums[l]
                        l += 1

            # going up
            else:
                # flip: decreasing -> increasing
                if r > 1 and nums[r - 2] > nums[r - 1]:
                    q = r - 1

                # valid trionic window
                if l < p < q:
                    res = max(res, curr)

        return res

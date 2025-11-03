class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()
        if p == 0:
            return 0

        def can_form(m):

            i, cnt = 0, 0
            n = len(nums)
            while i < n - 1:
                if nums[i+1] - nums[i] <= m:
                    cnt += 1
                    i += 2
                else:
                    i += 1
                if cnt >= p:
                    return True
            return False

        l, r = 0, 10**9
        res = r
        while l <= r:
            mid = (l + r) // 2
            if can_form(mid):
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        return res

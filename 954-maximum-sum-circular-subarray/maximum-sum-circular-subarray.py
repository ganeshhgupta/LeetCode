class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:

        n = len(nums)
        doubled = nums + nums

        prefix = [0] * (2 * n + 1)
        for i in range(2 * n):
            prefix[i+1] = prefix[i] + doubled[i]

        dq = deque()  # sliding window minimum prefix sum
        res = nums[0]

        for r in range(1, 2 * n + 1):
            # add l = r-1 to window
            l = r - 1
            while dq and prefix[dq[-1]] >= prefix[l]:
                dq.pop()
            dq.append(l)

            # evict indices outside window of size n
            while dq[0] < r - n:
                dq.popleft()

            # best subarray ending at r = prefix[r] - min prefix in window
            res = max(res, prefix[r] - prefix[dq[0]])

        return res
class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:

        n = len(nums)
        mod = 10**9 + 7

        dp = [0] * n + [1]

        maxq = deque()
        minq = deque()
        left = -1

        for i, v in enumerate(nums):
            
            while maxq and nums[maxq[-1]] <= v:
                maxq.pop()
            maxq.append(i)

            while minq and nums[minq[-1]] >= v:
                minq.pop()
            minq.append(i)

            while nums[minq[0]] + k < nums[maxq[0]]:
                if minq[0] < maxq[0]:
                    left = minq.popleft()
                else:
                    left = maxq.popleft()

            dp[i] = ((dp[i-1] << 1) - dp[left - 1]) % mod

        return (dp[n - 1] - dp[n - 2]) % mod

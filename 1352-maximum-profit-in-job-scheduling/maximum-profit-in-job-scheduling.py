class Solution:
    def jobScheduling(self, startTime, endTime, profit):

        jobs = sorted(zip(startTime, endTime, profit))
        starts = [job[0] for job in jobs]

        n = len(jobs)
        dp = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            s, e, p = jobs[i]

            j = bisect_left(starts, e, i + 1)
            dp[i] = max(p + dp[j], dp[i + 1])

        return dp[0]
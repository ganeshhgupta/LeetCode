class Solution:
    def minimumDifference(self, nums: List[int]) -> int:

        # O(n.2^n), O(2^v)
        # extension of https://leetcode.com/problems/closest-subsequence-sum/description/
        # only diff: bisect_left in right(n-k)

        n = len(nums) // 2
        S = sum(nums)

        def subset_sums(arr): # enumerates all possible sums for any k values in an array, k = 1 to len(arr)
            sums = [[] for _ in range(len(arr) + 1)]
            sums[0] = [0]
            for num in arr:
                for k in range(len(arr) - 1, -1, -1):
                    sums[k + 1] += [num + x for x in sums[k]]
            return sums

        left_sums = subset_sums(nums[:n])
        right_sums = subset_sums(nums[n:])

        #print(n)
        #print(left_sums)
        #print(right_sums)

        ans = float('inf')

        for k in range(n + 1):
            a1 = left_sums[k]
            a2 = sorted(right_sums[n - k])

            for v1 in a1:
                target = S / 2 - v1
                j = bisect_left(a2, target)

                if j < len(a2):
                    ans = min(ans, abs(2 * (v1 + a2[j]) - S))
                if j > 0:
                    ans = min(ans, abs(2 * (v1 + a2[j - 1]) - S))

        return ans
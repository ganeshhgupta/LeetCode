class Solution:
    def findMaxLength(self, nums: List[int]) -> int:

        pre = {0: -1}   # prefix_sum -> earliest index
        curr = res = 0

        for i, n in enumerate(nums):
            curr += 1 if n == 1 else -1

            if curr in pre:
                res = max(res, i - pre[curr])
            else:
                pre[curr] = i

        return res

from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        curr = sum(nums[:k])
        maxx = curr
        for i in range(k , len(nums)):
            curr = curr + nums[i] - nums[i - k]
            maxx = max(maxx, curr)
        return maxx/k
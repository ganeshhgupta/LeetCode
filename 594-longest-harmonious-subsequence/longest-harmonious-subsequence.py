from collections import Counter
from typing import List

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        count = Counter(nums)
        longest = 0
        for num in count:
            if num + 1 in count:
                longest = max(longest, count[num] + count[num + 1])
        return longest

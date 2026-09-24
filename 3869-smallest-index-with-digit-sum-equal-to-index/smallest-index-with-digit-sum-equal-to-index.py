class Solution:
    def smallestIndex(self, nums: List[int]) -> int:

        for i, x in enumerate(nums):
            if sum(int(j) for j in list(str(x))) == i:
                return i
        return -1     
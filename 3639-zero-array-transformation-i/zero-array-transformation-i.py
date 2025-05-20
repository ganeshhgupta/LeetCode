class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:

        n, m = len(nums), len(queries)
        diff=[0]*(n+1)

        for l, r in queries:
            diff[l]+=1
            diff[r+1]-=1

        curr = 0
        for i, val in enumerate(nums):
            curr += diff[i]
            if val > curr:
                return False

        return True

        
class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        
        res, pre = 0, 0
        c = Counter({0: 1})
        for n in nums:
            pre += n
            res += c[pre - goal]
            c[pre] += 1

        return res
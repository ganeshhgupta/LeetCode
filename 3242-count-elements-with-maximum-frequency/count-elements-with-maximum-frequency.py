class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        c = Counter(nums)
        c = sorted(c.values(), reverse=True)
        res = c[0]
        for i in range(len(c) - 1):
            if c[i] != c[i+1]:
                break
            res += c[i]
        return res
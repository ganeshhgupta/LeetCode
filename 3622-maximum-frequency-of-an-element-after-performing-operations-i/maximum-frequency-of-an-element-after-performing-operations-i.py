class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        
        # O(M * log n) M = max(nums), n = len(nums) , O(n)

        nums.sort()
        count = Counter(nums)

        def maxFreq(n):
            left = bisect_left(nums, n - k)
            right = bisect_right(nums, n + k)

            range = right - left - count[n]
            return min (range, numOperations) + count[n] 

        res = 0
        for i in range(1, max(nums) + 1):
            res = max(res, maxFreq(i))
        
        return res
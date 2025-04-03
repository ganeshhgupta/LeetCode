class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return 0
        sum = 0
        prefix_max, suffix_max = [0] * n, [0] * n

        prefix_max[0] = nums[0]
        for i in range(1, n):
            prefix_max[i] = max(prefix_max[i-1], nums[i])

        suffix_max[n-1] = nums[n-1]
        for i in range(n-2, -1, -1):
            suffix_max[i] = max(suffix_max[i+1], nums[i])

        #print(prefix_max, suffix_max)

        for i in range(n-2):
            sum = max(sum, (prefix_max[i] - nums[i+1]) * suffix_max[i+2])

        return sum
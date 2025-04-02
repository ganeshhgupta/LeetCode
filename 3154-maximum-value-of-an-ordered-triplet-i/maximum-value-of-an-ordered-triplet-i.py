class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return 0
        sum = 0

        #embarrasing..
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                for k in range(j + 1, n):
                    if i < j < k:
                        sum = max(sum, (nums[i] - nums[j]) * nums[k])

        return sum 




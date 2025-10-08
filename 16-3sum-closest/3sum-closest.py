class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
        # O(n²), O(1)
        nums.sort()
        n = len(nums)
        self.closest = float('inf')

        def twoSumII(i, num):
            l, r = i, n - 1
            while l < r:
                curr = num + nums[l] + nums[r]
                if abs(curr - target) < abs(self.closest - target): self.closest = curr

                if curr < target: l += 1
                elif curr > target: r -= 1
                else: return target
            return self.closest

        for i in range(n - 2):
            twoSumII(i + 1, nums[i])

        return self.closest

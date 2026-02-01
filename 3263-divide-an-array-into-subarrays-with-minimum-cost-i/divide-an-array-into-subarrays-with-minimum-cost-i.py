class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        n = len(nums)

        if n <= 3:
            return sum(nums)

        heap = nums[1:]
        heapq.heapify(heap)

        res = nums[0]
        res += heapq.heappop(heap)
        res += heapq.heappop(heap)

        return res

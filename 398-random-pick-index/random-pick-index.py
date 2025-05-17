class Solution:

    def __init__(self, nums: List[int]):
        self.map = defaultdict(list)
        self.nums = nums
        for i, n in enumerate(self.nums):
            self.map[n].append(i)

    def pick(self, target: int) -> int:
        indices = self.map[target]
        return random.choice(indices)



# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
class Solution:

    def __init__(self, w: List[int]):
        self.pre_sum = [w[0]]
        for i in range(1, len(w)):
            self.pre_sum.append(self.pre_sum[-1] + w[i])
        self.total = self.pre_sum[-1]

    def pickIndex(self) -> int:
        target = random.randint(1, self.total)
        l, r = 0, len(self.pre_sum) - 1

        while l < r:
            mid = (l + r) // 2
            if self.pre_sum[mid] < target:
                l = mid + 1
            else:
                r = mid

        return l



# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
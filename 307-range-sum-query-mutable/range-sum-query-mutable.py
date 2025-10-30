class NumArray:

    def __init__(self, nums: List[int]):

        # O(n), O(n)
        self.n = len(nums)
        self.tree = [0] * (2 * self.n)

        for i in range(self.n):
            self.tree[self.n + i] = nums[i]
        
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = self.tree[2*i] + self.tree[2*i + 1]

    def update(self, index: int, val: int) -> None:

        # O(log n), O(1)  ← Fixed!

        i = index + self.n
        self.tree[i] = val

        # update the parents:

        while i > 1:
            if i % 2 == 0:
                self.tree[i//2] = self.tree[i] + self.tree[i+1]
            else:
                self.tree[i//2] = self.tree[i] + self.tree[i-1]
            i//=2    

    def sumRange(self, left: int, right: int) -> int:

        # O(log n), O(1)

        l = left + self.n
        r = right + self.n + 1
        res = 0

        while l < r:
            if l % 2 == 1:
                res += self.tree[l]
                l += 1

            if r % 2 == 1:
                r -= 1
                res += self.tree[r]

            l//=2
            r//=2

        return res
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        #sliding
        c, f = defaultdict(int), fruits
        l, res = 0, 0

        for r in range(len(f)):
            c[f[r]] += 1

            while len(c) > 2:
                c[f[l]] -= 1
                if c[f[l]] == 0:
                    del c[f[l]]
                l += 1

            res = max(res, r - l + 1)

        return res

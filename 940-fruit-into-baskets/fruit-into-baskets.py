class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        
        # form a contiguous subarray with atmost 2 distinct fruits
        # O(n), O(1)

        c = defaultdict(int)
        l = cur = res = 0

        for r in range(len(fruits)):
            c[fruits[r]] += 1
            cur += 1

            while len(c) > 2:
                c[fruits[l]] -=1
                cur -= 1
                if not c[fruits[l]]: c.pop(fruits[l])
                l += 1

            res = max(res, cur)
        return res

class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        MOD = 10 ** 9 + 7
        res = total = 0

        y_levels = defaultdict(int)

        for y, y in points:
            y_levels[y] += 1

        for y, count in y_levels.items():
            lines = count * (count - 1) // 2
            res = (res + total * lines) % MOD
            total = (total + lines) % MOD
        return res
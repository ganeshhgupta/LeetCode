class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        
        cnt = Counter(power)
        vals = sorted(cnt.keys())

        @lru_cache(None)
        def dfs(i):
            if i >= len(vals):
                return 0

            # Option 1: skip current value
            skip = dfs(i + 1)

            # Option 2: take current value and jump to next valid
            j = i + 1
            while j < len(vals) and vals[j] <= vals[i] + 2:
                j += 1
            take = vals[i] * cnt[vals[i]] + dfs(j)

            return max(skip, take)

        return dfs(0)

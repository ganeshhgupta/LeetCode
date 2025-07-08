class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        # Sort events by start time
        events.sort(key=lambda x: x[0])
        starts = [e[0] for e in events]
        n = len(events)

        @lru_cache(None)
        def dfs(i: int, remaining: int) -> int:
            if i == n or remaining == 0:
                return 0

            # Skip current event
            skip = dfs(i + 1, remaining)

            # Take current event
            # Find next event that starts after events[i] ends (non-overlapping)
            next_i = bisect_left(starts, events[i][1] + 1)
            take = events[i][2] + dfs(next_i, remaining - 1)

            return max(skip, take)

        return dfs(0, k)

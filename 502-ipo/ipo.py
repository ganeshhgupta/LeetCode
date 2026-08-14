class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        
        projects = sorted(zip(capital, profits))
        mh = []                                     # max-heap (cap, profit)

        i = 0

        for _ in range(k):

            # Add every project we can currently afford
            while i < len(projects) and projects[i][0] <= w:
                heapq.heappush(mh, -projects[i][1])
                i += 1

            # No project is affordable
            if not mh:
                break

            # Pick the highest-profit affordable project
            w += -heapq.heappop(mh)

        return w



class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        # O(n), O(n)

        res = []
        i = 0
        n = len(intervals)

        new = newInterval
        intv = intervals

        # Before overlap
        while i < n and intv[i][1] < new[0]:
            res.append(intv[i])
            i += 1

        # Overlap + merge
        while i < n and intv[i][0] <= new[1]:
            new[0] = min(new[0], intv[i][0])
            new[1] = max(new[1], intv[i][1])
            i += 1

        res.append(new)

        # After overlap
        while i < n:
            res.append(intv[i])
            i += 1

        return res
class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:

        # O(F log F + P log F), O(F)
        starts = sorted(s for s, e in flowers)
        ends = sorted(e for s, e in flowers)

        ans = []

        for t in people:
            # Flowers that have started by time t
            started = bisect_right(starts, t)

            # Flowers that ended before time t
            ended = bisect_left(ends, t)

            ans.append(started - ended)

        return ans
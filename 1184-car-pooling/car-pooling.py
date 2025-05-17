class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:

        li = []
        for t in trips:
            p, s, e = t
            li.append([s, p])
            li.append([e, -p])
        li = sorted(li)
        curr = 0
        for i, j in li:
            curr += j
            if curr > capacity:
                return False
        return True
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        
        # O(n), O(n)
        
        li = []

        for p, s, e in trips:
            li.append((s, p))
            li.append((e, -p))
        
        li.sort()

        curr = 0
        for intv, count in li:
            curr += count
            if curr > capacity:
                return False

        return True

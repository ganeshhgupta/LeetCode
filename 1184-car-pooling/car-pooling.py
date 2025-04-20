class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        
        li = []
        for t in trips:
            p, s, e = t
            li.append([s, p])
            li.append([e, p * -1])

        li = sorted(li)
        print(li)
        
        curr = 0
        for i in li:
            _, p = i
            curr += p
            print(curr)
            if curr > capacity:
                return False
        return True
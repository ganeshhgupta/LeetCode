class Solution:
    def reorganizeString(self, s: str) -> str:
        
        # O(nlogk), O(n)
        
        c = Counter(s)
        res = []

        for k, v in c.items():
            if v > (len(s) + 1) // 2:
                return ""

        
        # max heap (hence -ve sign)
        mh = [(-v, k) for k, v in c.items()] 
        heapq.heapify(mh)
        prev = (0, '')

        while mh:

            count, char = heapq.heappop(mh)
            res.append(char)

            count += 1 # since -ve, we +1 instead of -1

            if prev[0] < 0:
                heapq.heappush(mh, prev)
            
            prev = (count, char)

        return "".join(res)
